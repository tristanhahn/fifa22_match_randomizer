import json
import random

with open("teams.json", "r", encoding="utf-8") as read_file:
    team_list = json.load(read_file)


def set_filters(teams, rating, exlusion_leagues):
    filtered_teams = []
    for team in teams:
        if team["rating"] >= rating and team["league"] not in exlusion_leagues:
            filtered_teams.append(team)

    return filtered_teams


def get_random_match(teams):
    number_of_teams = len(teams)
    team_1 = teams.pop(random.randint(0, number_of_teams))
    teams_with_similar_rating = [d for d in teams if
                                 d['rating'] in [team_1["rating"], team_1["rating"] - 0, team_1["rating"] + 0]]
    number_of_teams_with_similar_rating = len(teams_with_similar_rating)
    team_2 = teams_with_similar_rating.pop(random.randint(0, number_of_teams_with_similar_rating))
    print(team_1["team"] + " (" + str(team_1["rating"]) + ")" + " (" + team_1["league"] + ")" + " vs " + team_2[
        "team"] + " (" + str(team_2["rating"]) + ")" + " (" + team_2["league"] + ")")


league_exclusion_list = ["Mexico Liga MX (1)", "CONMEBOL Sudamericana", "Argentina Primera División (1)",
                         "Brazil Serie A (1)", "CONMEBOL Libertadores", "USA Major League Soccer (1)",
                         "Saudi Pro League (1)", "Brazil Serie A (1)"]


get_random_match(set_filters(teams = team_list, rating = 3.5, exlusion_leagues=league_exclusion_list))
