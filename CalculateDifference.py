avg_stats = {
    "Win%": 60.76,
    "PP%": 20.35,
    "PK%": 81.03,
    "Points%": 65.35,
    "Div Rank": 2,
    "Conf Rank": 3.36
}

def distance_from_average(row):
    diff = 0
    for stat in avg_stats:
        diff += abs(row[stat] - avg_stats[stat])
    return diff

df_2024["DistanceFromWinnerProfile"] = df_2024.apply(distance_from_average, axis=1)

closest_teams = df_2024.sort_values(by="DistanceFromWinnerProfile")
closest_teams
