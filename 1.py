import requests
import pandas as pd
from bs4 import BeautifulSoup

all_stats_url = 'https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats', 
shooting_url = 'https://fbref.com/en/comps/Big5/shooting/players/Big-5-European-Leagues-Stats',
passing_url = 'https://fbref.com/en/comps/Big5/passing/players/Big-5-European-Leagues-Stats',
pass_types_url = 'https://fbref.com/en/comps/Big5/passing_types/players/Big-5-European-Leagues-Stats',
goal_shot_creation_url = 'https://fbref.com/en/comps/Big5/gca/players/Big-5-European-Leagues-Stats',
defense_url = 'https://fbref.com/en/comps/Big5/defense/players/Big-5-European-Leagues-Stats',
possession_url = 'https://fbref.com/en/comps/Big5/possession/players/Big-5-European-Leagues-Stats',
play_time_url = 'https://fbref.com/en/comps/Big5/playingtime/players/Big-5-European-Leagues-Stats'




