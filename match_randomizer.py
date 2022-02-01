import json
import random
from team_data_extractor import run_extractor

try:
    with open("teams.json", "r", encoding="utf-8") as read_file:
        team_list = json.load(read_file)
except FileNotFoundError:
    run_extractor()
    with open("teams.json", "r", encoding="utf-8") as read_file:
        team_list = json.load(read_file)


def set_filters(teams, rating_min, rating_max, exlusion_leagues) -> list:
    filtered_teams = []
    for team in teams:
        if team["rating"] >= rating_min and team["rating"] <= rating_max and team["league"] not in exlusion_leagues:
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


def run_randomizer(rating_min=0, rating_max=5, exlusion_leagues=[]):
    get_random_match(
        set_filters(teams=team_list, rating_min=rating_min, rating_max=rating_max, exlusion_leagues=exlusion_leagues))
