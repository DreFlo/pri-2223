import pandas as pd
import json
from datetime import datetime

titles_df = pd.read_csv('data/processed_titles.csv')

credits_df = pd.read_csv('data/processed_credits.csv')

genres_df = pd.read_csv('data/genres.csv')

scores_df = pd.read_csv('data/scores.csv')

json_titles = []

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(counter=0)
def add_id_to_credits(row):
    add_id_to_credits.counter += 1
    credit_id_str = 'credit_' + row['id'] + '_' + str(add_id_to_credits.counter)
    return credit_id_str

def get_genres(dict):
    genres = []
    for key in dict.keys():
        if dict[key] == 1:
            genres.append(key)
    return genres

def title_to_json(row):
    title = {}

    title['id'] = row['id']
    title['title'] = row['title']
    title['type'] = row['type']
    title['description'] = row['description']
    title['release_year'] = row['release_year']
    title['age_certification'] = row['age_certification']
    title['runtime'] = row['runtime']
    title['seasons'] = int(row['seasons']) if not pd.isnull(row['seasons']) else None

    title['genres'] = get_genres(genres_df.loc[genres_df['id'] == title['id']].loc[:, genres_df.columns!='id'].to_dict(orient='records')[0])

    title['content_type'] = 'parentDocument'

    title['_childDocuments_'] = credits_df.loc[credits_df['id'] == title['id']].loc[:, credits_df.columns!='id'].to_dict(orient='records')

    scores_dict = scores_df.loc[scores_df['id'] == title['id']].loc[:, scores_df.columns!='id'].to_dict(orient='records')[0]

    for key in scores_dict.keys():
        title[key] = scores_dict[key]

    json_titles.append(title)

credits_df['credit_id'] = credits_df.apply(add_id_to_credits, axis=1)

titles_df.apply(title_to_json, axis=1)

json_string = json.dumps(json_titles, indent=4).replace('NaN', 'null').replace('credit_id', 'id')

with open('titles.json', 'w') as f:
    f.write(json_string)