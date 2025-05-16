import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Chargement des données globales d’équipes
pkl_path = r'C:\Users\User\Documents\Cours\nosql\data\fbref_data\global_team_stats_fbref.pkl'

with open(pkl_path, 'rb') as f:
    global_team_stats = pickle.load(f)

df = pd.DataFrame(global_team_stats).transpose()
df.columns = [f'{int(col)}-{int(col)+1}' for col in df.columns]

def compare_teams(team1, team2, season):
    if season not in df.columns:
        print(f"Saison non trouvée : {season}")
        return

    stats1 = df[season].get(team1)
    stats2 = df[season].get(team2)

    if stats1 is None or stats2 is None:
        print("Nom d’équipe non trouvé. Vérifiez les noms.")
        return

    stat_keys = list(stats1.keys())
    values1 = [float(stats1[k]) if isinstance(stats1[k], (int, float, str)) and str(stats1[k]).replace('.', '', 1).isdigit() else 0 for k in stat_keys]
    values2 = [float(stats2[k]) if isinstance(stats2[k], (int, float, str)) and str(stats2[k]).replace('.', '', 1).isdigit() else 0 for k in stat_keys]

    angles = np.linspace(0, 2 * np.pi, len(stat_keys), endpoint=False).tolist()
    values1 += values1[:1]
    values2 += values2[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    ax.plot(angles, values1, label=team1, color='blue')
    ax.fill(angles, values1, alpha=0.25, color='blue')

    ax.plot(angles, values2, label=team2, color='red')
    ax.fill(angles, values2, alpha=0.25, color='red')

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(stat_keys, fontsize=9)
    ax.set_title(f'Comparaison {team1} vs {team2} ({season})', fontsize=14)
    ax.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    teams = list(df.index)
    print("Équipes disponibles :")
    for t in teams:
        print(f'- {t}')

    team1 = input("Choisissez la première équipe : ")
    team2 = input("Choisissez la deuxième équipe : ")
    season = input(f"Choisissez la saison parmi {list(df.columns)} : ")

    compare_teams(team1, team2, season)