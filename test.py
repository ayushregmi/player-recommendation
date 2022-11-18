from bs4 import BeautifulSoup
import pandas as pd
import requests
import warnings

warnings.filterwarnings('ignore')

url = "https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats"

html = requests.get(url=url).text

soup = BeautifulSoup(html, "html.parser")
table = soup.find("tbody")
rows = table.find_all("tr")

df = pd.DataFrame(columns=['index', 'name', 'country', 'position', 'club', 'league', 'games_played', 'games_started', 'minutes_played', 'minutes_per_90', 'goals', 'assists', 'non_penalty_goals', 'penalty_goals', 'penalty_attempted', 'yellow_cards', 'red_card', 'goals_per_90', 'assits_per_90', 'non_penalty_goals_per_90'])

for row in rows:
    try:
        if row['class']:
            continue
    except:
        index = int(row.find("th").text)
        values = row.find_all("td")
        name = values[0].find('a').text
        country = values[1].text.split(' ')[len(values[1].text.split(' ')) - 1]
        position = values[2].text.split(',')
        club = values[3].text
        league = values[4].find('a').text
        games_played = int(values[7].text)
        games_started = int(values[8].text)
        minutes_played = int(''.join(values[9].text.split(',')))
        minutes_per_90 = float(values[10].text)
        goals = int(values[11].text) 
        assists = int(values[12].text)
        non_penalty_goals = int(values[13].text)
        penalty_goals = int(values[14].text)
        penalty_attempted = int(values[15].text)
        yellow_cards = int(values[16].text)
        red_card = int(values[17].text)
        goals_per_90 = float(values[18].text)
        assits_per_90 = float(values[19].text)
        non_penalty_goals_per_90 = float(values[20].text)

        # stats.append([index, name, country, position, club, league, games_played, games_started, minutes_played, minutes_per_90, goals, assists, non_penalty_goals, penalty_goals, penalty_attempted, yellow_cards, red_card, goals_per_90, assits_per_90, non_penalty_goals_per_90])
        df.append([index, name, country, position, club, league, games_played, games_started, minutes_played, minutes_per_90, goals, assists, non_penalty_goals, penalty_goals, penalty_attempted, yellow_cards, red_card, goals_per_90, assits_per_90, non_penalty_goals_per_90], ignore_index = True)
        
print(df.head())