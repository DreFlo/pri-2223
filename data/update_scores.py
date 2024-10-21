from math import nan
import math
import requests
from bs4 import BeautifulSoup
import csv
import sys
import pandas as pd

print('Updating scores')

csv_list = [['id', 'imdb_id', 'imdb_score', 'imdb_votes', 'tmdb_score', 'tmdb_popularity']]

with open(sys.argv[1], 'r') as temp_scores:
    scores_csv = csv.reader(temp_scores)
    next(scores_csv)

    for row in scores_csv:
        imdb_score_final = float(row[2]) if row[2] != '' else None
        imdb_votes_final = int(float(row[3].replace(",", ""))) if row[3] != '' else None

        if type(row[1]) == str:
            imdb_url = "https://www.imdb.com/title/" + str(row[1]) + "/ratings/?ref_=tt_ov_rt"
            imdb_page = requests.get(imdb_url)
            imdb_soup = BeautifulSoup(imdb_page.text, 'html.parser')
            imdb_movie_data = imdb_soup.find('td', attrs = {'class': 'ratingTable Selected'})
            
            if imdb_movie_data is not None:
                imdb_score = imdb_movie_data.find('div', 'bigcell')
                imdb_votes = imdb_movie_data.find('div', 'smallcell')
                imdb_score_final = float(imdb_score.text.strip()) if imdb_score is not None else None
                imdb_votes_final = int(imdb_votes.text.strip().replace(",", "")) if imdb_votes is not None else None
        
        tmdb_id = row[0]
        tmdb_url = 'https://www.themoviedb.org/'

        if tmdb_id[0:2] == 'tm':
            tmdb_url += 'movie/' + tmdb_id[2:]
        elif tmdb_id[0:2] == 'ts':
            tmdb_url += 'tv/' + tmdb_id[2:]

        tmdb_page = requests.get(tmdb_url)
        tmdb_soup = BeautifulSoup(tmdb_page.text, 'html.parser')

        tmdb_score_info = tmdb_soup.find('div', attrs={'class', 'user_score_chart'})

        tmdb_score = float(row[4]) if row[4] != '' else None

        if tmdb_score_info is not None:
            tmdb_score = float(tmdb_score_info['data-percent']) / 10

        csv_list.append([row[0], row[1], imdb_score_final, imdb_votes_final, tmdb_score, float(row[5]) if row[5] != '' else None])

        print(row[0] + '\n')

with open('scores.csv', 'w', newline='') as scores:
    csv_writer = csv.writer(scores)
    csv_writer.writerows(csv_list)

print('Scores updated')
