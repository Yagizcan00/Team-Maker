import pandas as pd

'''
# Görkem abinin puanlaması
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
'''

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
        "Topu Kullanma Becerisi": 2,
        "Topsuz Alanda Hücum Becerisi": 2,
        "Birebir Savunma Becerisi": 2,
        "Takım Savunması Becerisi": 2,
    },
    {
        "İsim": "Cihan",
        "Topu Kullanma Becerisi": 4,
        "Topsuz Alanda Hücum Becerisi": 3,
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
    "topsuz_alanda_hücum_becerisi": 1.2,
    "birebir_savunma_becerisi": 1.3,
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
    lambda row: "Savunma" if row["Genel Savunma Becerisi"] > row["Genel Hücum Becerisi"] else "Hücum",
    axis=1
)

# Dengeli takım oluşturma
def balance_teams(df, num_teams=2, min_defenders=3, min_attackers=3):
    teams = {f"Team {i+1}": [] for i in range(num_teams)}
    df_sorted = df.sort_values(by=["Genel Hücum Becerisi", "Genel Savunma Becerisi"], ascending=False)

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