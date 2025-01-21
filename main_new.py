import json

# Oyuncu bilgilerini JSON dosyasından okuyup listeleme
try:
    with open("oyuncular.json", "r", encoding="utf-8") as dosya:
        oyuncular = json.load(dosya)
except FileNotFoundError:
    print(
        "'oyuncular.json' dosyası bulunamadı. Lütfen dosyanın mevcut olduğundan emin olun."
    )
    oyuncular = []
except json.JSONDecodeError:
    print("'oyuncular.json' dosyası geçersiz formatta. Lütfen kontrol edin.")
    oyuncular = []

# Oyuncu bilgileri mevcutsa, listelere ayırma
if oyuncular:
    oyuncu_isimleri = [oyuncu["isim"] for oyuncu in oyuncular]
    oyuncu_puanlari = [oyuncu["puan"] for oyuncu in oyuncular]

    # Oyuncu bilgilerini ekrana yazdırma (örnek amaçlı)
    print("Oyuncu Listesi:")
    for isim, puan in zip(oyuncu_isimleri, oyuncu_puanlari):
        print(f"{isim}: {puan}")

# Çarpanlar
multipliers = {
    "topu_kullanma_becerisi": 1.4,
    "topsuz_alanda_hücum_becerisi": 1.3,
    "birebir_savunma_becerisi": 1.4,
    "takim_savunması_becerisi": 1.5,
}

# DataFrame oluşturma
df = pd.DataFrame(players_data)

# Hücum ve savunma becerilerini hesaplama
df["Genel Hücum Becerisi"] = (
    df["Topu Kullanma Becerisi"] * multipliers["topu_kullanma_becerisi"]
    + df["Topsuz Alanda Hücum Becerisi"] * multipliers["topsuz_alanda_hücum_becerisi"]
)
df["Genel Savunma Becerisi"] = (
    df["Birebir Savunma Becerisi"] * multipliers["birebir_savunma_becerisi"]
    + df["Takım Savunması Becerisi"] * multipliers["takim_savunması_becerisi"]
)

# Pozisyona göre etiketleme
df["Pozisyon"] = df.apply(
    lambda row: (
        "Savunma"
        if row["Genel Savunma Becerisi"] > row["Genel Hücum Becerisi"]
        else "Hücum"
    ),
    axis=1,
)


# Dengeli takım oluşturma
def balance_teams(df, num_teams=2, min_defenders=3, min_attackers=3):
    teams = {f"Team {i+1}": [] for i in range(num_teams)}
    df_sorted = df.sort_values(
        by=["Genel Hücum Becerisi", "Genel Savunma Becerisi"], ascending=False
    )

    # Savunma ve hücum oyuncuları
    defenders = df_sorted[df_sorted["Pozisyon"] == "Savunma"]
    attackers = df_sorted[df_sorted["Pozisyon"] == "Hücum"]

    # Takımlara savunma ve hücum oyuncuları dağıtma
    for i in range(min_defenders):
        for team in teams.keys():
            if not defenders.empty:
                teams[team].append(defenders.iloc[0].to_dict())
                defenders = defenders.iloc[1:]

    for i in range(min_attackers):
        for team in teams.keys():
            if not attackers.empty:
                teams[team].append(attackers.iloc[0].to_dict())
                attackers = attackers.iloc[1:]

    # Kalan oyuncuları sırayla dağıtma
    remaining_players = pd.concat([defenders, attackers])
    while not remaining_players.empty:
        for team in teams.keys():
            if not remaining_players.empty:
                teams[team].append(remaining_players.iloc[0].to_dict())
                remaining_players = remaining_players.iloc[1:]

    return teams


# Takımları oluştur
balanced_teams = balance_teams(df)

# Takımları görüntüleme
for team_name, players in balanced_teams.items():
    print(f"\n{team_name} Players:")
    print(pd.DataFrame(players))

# Takımları yalnızca oyuncu isimleriyle görüntüleme
for team_name, players in balanced_teams.items():
    print(f"\n{team_name} Players:")
    player_names = [player["İsim"] for player in players]
    print(pd.DataFrame(player_names, columns=["İsim"]))
