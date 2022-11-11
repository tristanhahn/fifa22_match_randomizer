import requests
import json
from bs4 import BeautifulSoup
from datetime import date


def get_teams(html):
    team_result = []
    team_data = html.find_all("tr")
    for team in team_data:
        team_name_link = team.find("a", class_="link-team")
        if team_name_link != None:
            team_name = team_name_link.get("title")
            team_name = team_name.replace(" FIFA 23", "")
        team_league_link = team.find("a", class_="link-league")
        if team_league_link != None:
            team_league = team_league_link.get("title")
        team_rating_list = team.find("span", class_="star")
        if team_rating_list != None:
            team_rating_full_stars = team_rating_list.findAll("i", class_="fas fa-star fa-lg")
            team_rating_half_stars = team_rating_list.findAll("i", class_="fas fa-star-half-alt fa-lg")
            if len(team_rating_half_stars) == 1:
                team_rating = len(team_rating_full_stars) + 0.5
            else:
                team_rating = len(team_rating_full_stars)
        if team_name_link != None and team_rating_list != None:
            team_result.append(dict(team=team_name, rating=team_rating, league=team_league))
    return team_result


def create_team_soup(url):
    page = requests.get(url=url)
    html = page.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find("table", class_="table table-striped table-teams")


def get_next_page(url):
    page = requests.get(url=url)
    html = page.text
    soup = BeautifulSoup(html, 'html.parser')
    next_page_data = soup.find("ul", class_="pagination justify-content-between")
    for element in next_page_data:
        if element.text == "Next Page":
            return True
        elif element.text == "Previous Page":
            continue
        else:
            return False


def check_if_extractor_already_run_today():
    try:
        with open("last_data_pull.json", "r", encoding="utf-8") as read_file:
            data = json.load(read_file)
        if data["last_pull_date"] == str(date.today()):
            return True
        else:
            False
    except json.JSONDecodeError:
        return False
    except FileNotFoundError:
        return False


def run_extractor():
    print("Updating teams data")
    counter = 1
    teams = []
    check = True
    base_url = "https://www.fifaindex.com/teams/?page="
    while check == True:
        url = base_url + str(counter)
        check = get_next_page(url)
        teams = teams + get_teams(create_team_soup(url))
        counter = counter + 1

    with open('teams.json', mode='w+', encoding='utf-8') as f:
        json.dump(teams, f, ensure_ascii=False, indent=4)
    with open('last_data_pull.json', mode='w+', encoding='utf-8') as f1:
        json.dump({'last_pull_date': str(date.today())}, f1, ensure_ascii=False, indent=4)
    print("Teams data updated")
