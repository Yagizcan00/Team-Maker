import pandas as pd

# Görkem abinin puanlaması
players_data = [
    {
        "İsim": "Yağızcan",
        "Top Becerisi": 2,
        "Topsuz Becerisi": 4,
        "Birebir Savunma": 5,
        "Takım Savunma": 5,
    },
    {
        "İsim": "Samet",
        "Top Becerisi": 5,
        "Topsuz Becerisi": 5,
        "Birebir Savunma": 1,
        "Takım Savunma": 1,
    },
    {
        "İsim": "Oğuzcan",
        "Top Becerisi": 2,
        "Topsuz Becerisi": 2,
        "Birebir Savunma": 1,
        "Takım Savunma": 1,
    },
    {
        "İsim": "Muhammed",
        "Top Becerisi": 4,
        "Topsuz Becerisi": 2,
        "Birebir Savunma": 2,
        "Takım Savunma": 3,
    },
    {
        "İsim": "Nurullah",
        "Top Becerisi": 3,
        "Topsuz Becerisi": 4,
        "Birebir Savunma": 5,
        "Takım Savunma": 4,
    },
    {
        "İsim": "Yasin",
        "Top Becerisi": 3,
        "Topsuz Becerisi": 3,
        "Birebir Savunma": 2,
        "Takım Savunma": 3,
    },
    {
        "İsim": "Oğuzhan",
        "Top Becerisi": 1,
        "Topsuz Becerisi": 3,
        "Birebir Savunma": 2,
        "Takım Savunma": 3,
    },
    {
        "İsim": "Cihan",
        "Top Becerisi": 5,
        "Topsuz Becerisi": 3,
        "Birebir Savunma": 4,
        "Takım Savunma": 3,
    },
    {
        "İsim": "İlker",
        "Top Becerisi": 3,
        "Topsuz Becerisi": 3,
        "Birebir Savunma": 3,
        "Takım Savunma": 3,
    },
    {
        "İsim": "Cengiz",
        "Top Becerisi": 1,
        "Topsuz Becerisi": 1,
        "Birebir Savunma": 4,
        "Takım Savunma": 2,
    },
    {
        "İsim": "Kerem",
        "Top Becerisi": 3,
        "Topsuz Becerisi": 3,
        "Birebir Savunma": 3,
        "Takım Savunma": 3,
    },
    {
        "İsim": "Emre",
        "Top Becerisi": 1,
        "Topsuz Becerisi": 3,
        "Birebir Savunma": 3,
        "Takım Savunma": 2,
    },
    {
        "İsim": "Görkem",
        "Top Becerisi": 5,
        "Topsuz Becerisi": 5,
        "Birebir Savunma": 4,
        "Takım Savunma": 2,
    },
    {
        "İsim": "Reşat",
        "Top Becerisi": 5,
        "Topsuz Becerisi": 5,
        "Birebir Savunma": 4,
        "Takım Savunma": 3,
    },
]


# Yağızın puanlaması
players_data = [
    {
        "İsim": "Yağızcan",
        "Top Becerisi": 2,
        "Topsuz Becerisi": 2,
        "Birebir Savunma": 5,
        "Takım Savunma": 4,
    },
    {
        "İsim": "Samet",
        "Top Becerisi": 4,
        "Topsuz Becerisi": 3,
        "Birebir Savunma": 2,
        "Takım Savunma": 2,
    },
    {
        "İsim": "Oğuzcan",
        "Top Becerisi": 2,
        "Topsuz Becerisi": 2,
        "Birebir Savunma": 1,
        "Takım Savunma": 2,
    },
    {
        "İsim": "Muhammed",
        "Top Becerisi": 2,
        "Topsuz Becerisi": 2,
        "Birebir Savunma": 3,
        "Takım Savunma": 3,
    },
    {
        "İsim": "Nurullah",
        "Top Becerisi": 3,
        "Topsuz Becerisi": 3,
        "Birebir Savunma": 5,
        "Takım Savunma": 4,
    },
    {
        "İsim": "Yasin",
        "Top Becerisi": 3,
        "Topsuz Becerisi": 3,
        "Birebir Savunma": 2,
        "Takım Savunma": 3,
    },
    {
        "İsim": "Oğuzhan",
        "Top Becerisi": 2,
        "Topsuz Becerisi": 2,
        "Birebir Savunma": 2,
        "Takım Savunma": 2,
    },
    {
        "İsim": "Cihan",
        "Top Becerisi": 4,
        "Topsuz Becerisi": 3,
        "Birebir Savunma": 3,
        "Takım Savunma": 2,
    },
    {
        "İsim": "İlker",
        "Top Becerisi": 2,
        "Topsuz Becerisi": 1,
        "Birebir Savunma": 3,
        "Takım Savunma": 4,
    },
    {
        "İsim": "Cengiz",
        "Top Becerisi": 1,
        "Topsuz Becerisi": 2,
        "Birebir Savunma": 2,
        "Takım Savunma": 3,
    },
    {
        "İsim": "Kerem",
        "Top Becerisi": 2,
        "Topsuz Becerisi": 3,
        "Birebir Savunma": 2,
        "Takım Savunma": 2,
    },
    {
        "İsim": "Emre",
        "Top Becerisi": 1,
        "Topsuz Becerisi": 1,
        "Birebir Savunma": 4,
        "Takım Savunma": 3,
    },
    {
        "İsim": "Görkem",
        "Top Becerisi": 5,
        "Topsuz Becerisi": 5,
        "Birebir Savunma": 4,
        "Takım Savunma": 2,
    },
    {
        "İsim": "Reşat",
        "Top Becerisi": 5,
        "Topsuz Becerisi": 5,
        "Birebir Savunma": 2,
        "Takım Savunma": 3,
    },
]


# Çarpanlar
multipliers = {
    "top_becerisi": 1.4,
    "topsuz_becerisi": 1.2,
    "birebir_savunma": 1.3,
    "takim_savunma": 1.5,
}

# DataFrame oluşturma
df = pd.DataFrame(players_data)

# Hücum ve savunma becerilerini hesaplama
df["Asıl Hücum Becerisi"] = (
    df["Top Becerisi"] * multipliers["top_becerisi"]
    + df["Topsuz Becerisi"] * multipliers["topsuz_becerisi"]
)
df["Asıl Savunma Becerisi"] = (
    df["Birebir Savunma"] * multipliers["birebir_savunma"]
    + df["Takım Savunma"] * multipliers["takim_savunma"]
)

# Pozisyona göre etiketleme
df["Pozisyon"] = df.apply(
    lambda row: (
        "Savunma"
        if row["Asıl Savunma Becerisi"] > row["Asıl Hücum Becerisi"]
        else "Hücum"
    ),
    axis=1,
)


# Dengeli takım oluşturma
def balance_teams(df, num_teams=2, min_defenders=3, min_attackers=3):
    teams = {f"Team {i+1}": [] for i in range(num_teams)}
    df_sorted = df.sort_values(
        by=["Asıl Hücum Becerisi", "Asıl Savunma Becerisi"], ascending=False
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
