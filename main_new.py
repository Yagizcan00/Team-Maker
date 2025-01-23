import pandas as pd

# Görkem Abinin Puanlaması
görkem_players_data = [
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

# Yağızın Puanlaması
yagiz_players_data = [
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
        "İsim": "Kerem",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 2,
        "Takım Savunması Becerisi": 2,
    },
    {
        "İsim": "Emre Turan",
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
    {
        "İsim": "Batu",
        "Topu Kullanma Becerisi": 5,
        "Topsuz Alanda Hücum Becerisi": 5,
        "Birebir Savunma Becerisi": 4,
        "Takım Savunması Becerisi": 5,
    },
    {
        "İsim": "Ali",
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 3,
        "Birebir Savunma Becerisi": 2,
        "Takım Savunması Becerisi": 1,
    },
]

# Çarpanlar
multipliers = {
    "topu_kullanma_becerisi": 5,
    "topsuz_alanda_hücum_becerisi": 3,
    "birebir_savunma_becerisi": 4,
    "takim_savunması_becerisi": 3,
}

# DataFrame oluşturma
df = pd.DataFrame(yagiz_players_data)

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

    # Takımlara savunma oyuncuları dağıtma
    for i in range(min_defenders):
        for team in teams.keys():
            if not defenders.empty:
                teams[team].append(defenders.iloc[0].to_dict())
                defenders = defenders.iloc[1:]

    # Takımlara hücum oyuncuları dağıtma
    for i in range(min_attackers):
        for team in teams.keys():
            if not attackers.empty:
                teams[team].append(attackers.iloc[0].to_dict())
                attackers = attackers.iloc[1:]

    # Kalan oyuncuları birleştir ve sırayla takımlara eşit şekilde dağıt
    remaining_players = pd.concat([defenders, attackers]).sort_values(
        by="Genel Oyuncu Becerisi", ascending=False
    )
    team_cycle = iter(teams.keys())
    while not remaining_players.empty:
        try:
            team = next(team_cycle)
        except StopIteration:
            team_cycle = iter(teams.keys())
            team = next(team_cycle)

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
