import requests
import json
from bs4 import BeautifulSoup

CHECK = True
URL = "https://www.fifaindex.com/teams/?page="


def get_teams(html):
    team_result = []
    team_data = html.find_all("tr")
    for team in team_data:
        team_name_link = team.find("a", class_="link-team")
        if team_name_link != None:
            team_name = team_name_link.get("title")
            team_name = team_name.replace(" FIFA 22", "")
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


def run_extractor(check, base_url):
    counter = 1
    teams = []
    while check == True:
        url = base_url + str(counter)
        check = get_next_page(url)
        teams = teams + get_teams(create_team_soup(url))
        counter = counter + 1
        print(teams)
    with open('teams.json', 'w', encoding='utf-8') as f:
        json.dump(teams, f, ensure_ascii=False, indent=4)


run_extractor(CHECK, URL)
