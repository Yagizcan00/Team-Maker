import pandas as pd

# Görkem Abinin Puanlaması
görkem_players_data = [
    {
        "İsim": "Yağızcan",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 4,
        "Birebir Savunma Yapma Becerisi": 5,
        "Takım Halinde Savunma Yapma Becerisi": 5,
    },
    {
        "İsim": "Samet",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Yapma Becerisi": 1,
        "Takım Halinde Savunma Yapma Becerisi": 1,
    },
    {
        "İsim": "Muhammed",
        "Topu Kullanma Becerisi": 4,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Yapma Becerisi": 2,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
    {
        "İsim": "Nurullah",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 4,
        "Birebir Savunma Yapma Becerisi": 5,
        "Takım Halinde Savunma Yapma Becerisi": 4,
    },
    {
        "İsim": "Yasin",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 2,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
    {
        "İsim": "Oğuzhan",
        "Topu Kullanma Becerisi": 1,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 2,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
    {
        "İsim": "Cihan",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 4,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
    {
        "İsim": "İlker",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 3,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
    {
        "İsim": "Kerem",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 3,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
    {
        "İsim": "Emre",
        "Topu Kullanma Becerisi": 1,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 3,
        "Takım Halinde Savunma Yapma Becerisi": 2,
    },
    {
        "İsim": "Görkem",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Yapma Becerisi": 4,
        "Takım Halinde Savunma Yapma Becerisi": 2,
    },
    {
        "İsim": "Reşat",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Yapma Becerisi": 4,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
    {
        "İsim": "Batu",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Yapma Becerisi": 4,
        "Takım Halinde Savunma Yapma Becerisi": 2,
    },
    {
        "İsim": "Ali",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 2,
        "Takım Halinde Savunma Yapma Becerisi": 1,
    },
]

# Yağızın Puanlaması
yagiz_players_data = [
    {
        "İsim": "Yağızcan",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Yapma Becerisi": 4,
        "Takım Halinde Savunma Yapma Becerisi": 5,
    },
    {
        "İsim": "Samet",
        "Topu Kullanma Becerisi": 4,
        "Topsuz Alanda Hücum Becerisi": 4,
        "Birebir Savunma Yapma Becerisi": 3,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
    {
        "İsim": "Muhammed",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Yapma Becerisi": 4,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
    {
        "İsim": "Nurullah",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 4,
        "Takım Halinde Savunma Yapma Becerisi": 4,
    },
    {
        "İsim": "Yasin",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 3,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
    {
        "İsim": "Oğuzhan",
        "Topu Kullanma Becerisi": 1,
        "Topsuz Alanda Hücum Becerisi": 1,
        "Birebir Savunma Yapma Becerisi": 2,
        "Takım Halinde Savunma Yapma Becerisi": 2,
    },
    {
        "İsim": "Cihan",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 3,
        "Takım Halinde Savunma Yapma Becerisi": 2,
    },
    {
        "İsim": "İlker",
        "Topu Kullanma Becerisi": 1,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Yapma Becerisi": 4,
        "Takım Halinde Savunma Yapma Becerisi": 4,
    },
    {
        "İsim": "Kerem",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 2,
        "Takım Halinde Savunma Yapma Becerisi": 2,
    },
    {
        "İsim": "Emre Turan",
        "Topu Kullanma Becerisi": 1,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Yapma Becerisi": 4,
        "Takım Halinde Savunma Yapma Becerisi": 4,
    },
    {
        "İsim": "Görkem",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Yapma Becerisi": 4,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
    {
        "İsim": "Batu",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Yapma Becerisi": 4,
        "Takım Halinde Savunma Yapma Becerisi": 4,
    },
    {
        "İsim": "Ali",
        "Topu Kullanma Becerisi": 3,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Yapma Becerisi": 2,
        "Takım Halinde Savunma Yapma Becerisi": 2,
    },
    {
        "İsim": "Metehan",
        "Topu Kullanma Becerisi": 4,
        "Topsuz Alanda Hücum Becerisi": 4,
        "Birebir Savunma Yapma Becerisi": 3,
        "Takım Halinde Savunma Yapma Becerisi": 3,
    },
]

# Çarpanlar
multipliers = {
    "topu_kullanma_becerisi": 2.0,
    "topsuz_alanda_hücum_becerisi": 1.6,
    "birebir_savunma_yapma_becerisi": 1.7,
    "takim_halinde_savunma_yapma_becerisi": 1.8,
}

# DataFrame oluşturma
df = pd.DataFrame(yagiz_players_data)

# Hücum ve savunma becerilerini hesaplama
df["Genel Hücum Becerisi"] = (
    df["Topu Kullanma Becerisi"] * multipliers["topu_kullanma_becerisi"]
    + df["Topsuz Alanda Hücum Becerisi"] * multipliers["topsuz_alanda_hücum_becerisi"]
)
df["Genel Savunma Becerisi"] = (
    df["Birebir Savunma Yapma Becerisi"] * multipliers["birebir_savunma_yapma_becerisi"]
    + df["Takım Halinde Savunma Yapma Becerisi"]
    * multipliers["takim_halinde_savunma_yapma_becerisi"]
)

# Pozisyona göre etiketleme
df["Pozisyon"] = df.apply(
    lambda row: (
        "Hücum"
        if row["Genel Hücum Becerisi"] > row["Genel Savunma Becerisi"]
        else "Savunma"
    ),
    axis=1,
)


# Dengeli takım oluşturma
def balance_teams(df, num_teams=2, min_defenders=3, min_attackers=3):
    # Genel Oyuncu Becerisi hesaplama
    df["Genel Oyuncu Becerisi"] = (
        df["Genel Savunma Becerisi"] + df["Genel Hücum Becerisi"]
    )

    teams = {f"Team {i+1}": [] for i in range(num_teams)}

    # Pozisyona göre oyuncuları ayırma
    defenders = df[df["Pozisyon"] == "Savunma"].sort_values(
        by="Genel Oyuncu Becerisi", ascending=False
    )
    attackers = df[df["Pozisyon"] == "Hücum"].sort_values(
        by="Genel Oyuncu Becerisi", ascending=False
    )

    # Takımlara savunma oyuncuları dağıtma (1. takımdan başlayarak)
    team_cycle_defense = iter(teams.keys())
    while not defenders.empty:
        try:
            team = next(team_cycle_defense)
        except StopIteration:
            team_cycle_defense = iter(teams.keys())
            team = next(team_cycle_defense)

        teams[team].append(defenders.iloc[0].to_dict())
        defenders = defenders.iloc[1:]

    # Takımlara hücum oyuncuları dağıtma (2. takımdan başlayarak)
    team_cycle_offense = iter(
        list(teams.keys())[1:] + list(teams.keys())[:1]
    )  # 2. takımdan başla
    while not attackers.empty:
        try:
            team = next(team_cycle_offense)
        except StopIteration:
            team_cycle_offense = iter(list(teams.keys())[1:] + list(teams.keys())[:1])
            team = next(team_cycle_offense)

        teams[team].append(attackers.iloc[0].to_dict())
        attackers = attackers.iloc[1:]

    # Kalan oyuncuları sıralayıp 2. takımdan başlayarak dağıtma
    remaining_players = pd.concat([defenders, attackers]).sort_values(
        by="Genel Oyuncu Becerisi", ascending=False
    )
    team_cycle_remaining = iter(list(teams.keys())[1:] + list(teams.keys())[:1])

    while not remaining_players.empty:
        try:
            team = next(team_cycle_remaining)
        except StopIteration:
            team_cycle_remaining = iter(list(teams.keys())[1:] + list(teams.keys())[:1])
            team = next(team_cycle_remaining)

        teams[team].append(remaining_players.iloc[0].to_dict())
        remaining_players = remaining_players.iloc[1:]

    return teams


# Takımları oluştur
balanced_teams = balance_teams(df, num_teams=2, min_defenders=3, min_attackers=3)

# Takımları görüntüleme
for team_name, players in balanced_teams.items():
    print(f"\n{team_name} Players:")
    print(pd.DataFrame(players))

# Takımları yalnızca oyuncu isimleriyle görüntüleme
for team_name, players in balanced_teams.items():
    print(f"\n{team_name} Players:")
    player_names = [player["İsim"] for player in players]
    print(pd.DataFrame(player_names, columns=["İsim"]))

# Takımların Genel Takım Puanlarını hesaplama ve gösterme
for team_name, players in balanced_teams.items():
    total_team_score = sum(player["Genel Oyuncu Becerisi"] for player in players)
    print(f"\n{team_name} Genel Takım Puanı: {total_team_score}")
