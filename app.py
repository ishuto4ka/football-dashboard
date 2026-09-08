import pandas as pd

df = pd.read_csv("players.csv")

print(df)
import csv

players = []

with open("players.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            player = {
                "name": row["name"],
                "minutes": int(row["minutes"]),
                "distance": float(row["distance"]),
                "max_speed": float(row["max_speed"]),
                "sprints": int(row["sprints"])
        }

            players.append(player)
        except (ValueError, KeyError):
            print(f"Invalid numeric data for player: {row['name']}")

def find_fastest_player(players):
    fastest = players[0]
    for player in players:
        if player['max_speed'] > fastest['max_speed']:
            fastest = player
    return fastest

def average_distance(players):
    sum = 0
    for player in players:
        sum += player['distance']
    return sum / len(players)


avg = average_distance(players)
print(f"The average distance covered by players is: {avg:.2f} meters.")

