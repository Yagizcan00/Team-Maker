import pandas as pd

"""
# Görkem Abinin Puanlaması
players_data = [
    {
        "İsim": "Yağızcan",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 4,
        "Birebir Savunma Becerisi": 5,
        "Takım Savunması Becerisi": 5,
    },
    {
        "İsim": "Samet",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Becerisi": 1,
        "Takım Savunması Becerisi": 1,
    },
    {
        "İsim": "Oğuzcan",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Becerisi": 1,
        "Takım Savunması Becerisi": 1,
    },
    {
        "İsim": "Muhammed",
        "Topu Kullanma Becerisi": 4,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Becerisi": 2,
        "Takım Savunması Becerisi": 3,
    },
    {
        "İsim": "Nurullah",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 4,
        "Birebir Savunma Becerisi": 5,
        "Takım Savunması Becerisi": 4,
    },
    {
        "İsim": "Yasin",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 2,
        "Takım Savunması Becerisi": 3,
    },
    {
        "İsim": "Oğuzhan",
        "Topu Kullanma Becerisi": 1,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 2,
        "Takım Savunması Becerisi": 3,
    },
    {
        "İsim": "Cihan",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 4,
        "Takım Savunması Becerisi": 3,
    },
    {
        "İsim": "İlker",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 3,
        "Takım Savunması Becerisi": 3,
    },
    {
        "İsim": "Cengiz",
        "Topu Kullanma Becerisi": 1,
        "Topsuz Alanda Hücum Becerisi": 1,
        "Birebir Savunma Becerisi": 4,
        "Takım Savunması Becerisi": 2,
    },
    {
        "İsim": "Kerem",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 3,
        "Takım Savunması Becerisi": 3,
    },
    {
        "İsim": "Emre",
        "Topu Kullanma Becerisi": 1,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 3,
        "Takım Savunması Becerisi": 2,
    },
    {
        "İsim": "Görkem",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Becerisi": 4,
        "Takım Savunması Becerisi": 2,
    },
    {
        "İsim": "Reşat",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Becerisi": 4,
        "Takım Savunması Becerisi": 3,
    },
]
"""

# Yağızın Puanlaması
players_data = [
    {
        "İsim": "Yağızcan",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Becerisi": 4,
        "Takım Savunması Becerisi": 5,
    },
    {
        "İsim": "Samet",
        "Topu Kullanma Becerisi": 4,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 2,
        "Takım Savunması Becerisi": 2,
    },
    {
        "İsim": "Oğuzcan",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Becerisi": 1,
        "Takım Savunması Becerisi": 2,
    },
    {
        "İsim": "Muhammed",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Becerisi": 3,
        "Takım Savunması Becerisi": 3,
    },
    {
        "İsim": "Nurullah",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 4,
        "Takım Savunması Becerisi": 4,
    },
    {
        "İsim": "Yasin",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 3,
        "Takım Savunması Becerisi": 3,
    },
    {
        "İsim": "Oğuzhan",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Becerisi": 2,
        "Takım Savunması Becerisi": 2,
    },
    {
        "İsim": "Cihan",
        "Topu Kullanma Becerisi": 4,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Becerisi": 3,
        "Takım Savunması Becerisi": 2,
    },
    {
        "İsim": "İlker",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Becerisi": 4,
        "Takım Savunması Becerisi": 4,
    },
    {
        "İsim": "Cengiz",
        "Topu Kullanma Becerisi": 1,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Becerisi": 2,
        "Takım Savunması Becerisi": 3,
    },
    {
        "İsim": "Kerem",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 2,
        "Takım Savunması Becerisi": 2,
    },
    {
        "İsim": "Emre",
        "Topu Kullanma Becerisi": 1,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Becerisi": 4,
        "Takım Savunması Becerisi": 4,
    },
    {
        "İsim": "Görkem",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Becerisi": 4,
        "Takım Savunması Becerisi": 2,
    },
    {
        "İsim": "Reşat",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Becerisi": 2,
        "Takım Savunması Becerisi": 3,
    },
]

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


# Pozisyona göre etiketleme (Hücum, Savunma, İki Yönlü)
def determine_position(row, threshold=1):
    if abs(row["Genel Hücum Becerisi"] - row["Genel Savunma Becerisi"]) <= threshold:
        return "İki Yönlü"
    elif row["Genel Hücum Becerisi"] > row["Genel Savunma Becerisi"]:
        return "Hücum"
    else:
        return "Savunma"


# Yeni pozisyonları belirle
df["Pozisyon"] = df.apply(determine_position, axis=1)


# Dengeli takım oluşturma
def balance_teams(df, num_teams=2, min_defenders=3, min_attackers=3):
    teams = {f"Team {i+1}": [] for i in range(num_teams)}
    df_sorted = df.sort_values(
        by=["Genel Hücum Becerisi", "Genel Savunma Becerisi"], ascending=False
    )

    # Savunma, hücum ve iki yönlü oyuncuları ayır
    defenders = df_sorted[df_sorted["Pozisyon"] == "Savunma"]
    attackers = df_sorted[df_sorted["Pozisyon"] == "Hücum"]
    two_way_players = df_sorted[df_sorted["Pozisyon"] == "İki Yönlü"]

    # İki yönlü oyuncuları hem savunma hem de hücum gruplarına ekle
    defenders = pd.concat([defenders, two_way_players])
    attackers = pd.concat([attackers, two_way_players])

    # Minimum savunma ve hücum oyuncusu atama
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
    remaining_players = pd.concat([defenders, attackers]).drop_duplicates()
    for i, player in enumerate(remaining_players.to_dict("records")):
        teams[f"Team {i % num_teams + 1}"].append(player)

    return teams


# Takımları oluştur
balanced_teams = balance_teams(df)

# Takımları yazdır ve puanları göster
for team_name, players in balanced_teams.items():
    total_offense = sum(player["Genel Hücum Becerisi"] for player in players)
    total_defense = sum(player["Genel Savunma Becerisi"] for player in players)

    print(f"\n{team_name} Oyuncuları:")
    for player in players:
        print(player["İsim"])

    print(
        f"{team_name} - Toplam Hücum Puanı: {total_offense}, Toplam Savunma Puanı: {total_defense}"
    )


# Takımları görüntüleme
for team_name, players in balanced_teams.items():
    print(f"\n{team_name} Players:")
    print(pd.DataFrame(players))

# Takımları yalnızca oyuncu isimleriyle görüntüleme
for team_name, players in balanced_teams.items():
    print(f"\n{team_name} Players:")
    player_names = [player["İsim"] for player in players]
    print(pd.DataFrame(player_names, columns=["İsim"]))