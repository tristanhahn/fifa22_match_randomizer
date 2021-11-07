import json
import random

with open("teams.json", "r", encoding="utf-8") as read_file:
    teams = json.load(read_file)


def set_rating(teams, rating):
    filtered_teams = []
    for team in teams:
        if team["rating"] >= rating:
            filtered_teams.append(team)
    return filtered_teams


def get_random_match(teams):
    number_of_teams = len(teams)
    team_1 = teams.pop(random.randint(0, number_of_teams))
    teams_with_similar_rating = [d for d in teams if
                                 d['rating'] in [team_1["rating"], team_1["rating"] - 0.5, team_1["rating"] + 0.5]]
    number_of_teams_with_similar_rating = len(teams_with_similar_rating)
    team_2 = teams_with_similar_rating.pop(random.randint(0, number_of_teams_with_similar_rating))
    print(team_1["team"] + " (" + str(team_1["rating"]) + ")" + " (" + team_1["league"] + ")" + " vs " + team_2[
        "team"] + " (" + str(team_2["rating"]) + ")" + " (" + team_2["league"] + ")")


get_random_match(set_rating(teams, 3.5))
