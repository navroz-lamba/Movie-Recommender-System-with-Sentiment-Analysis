""" This file generates a csv with movies released in the year 2017 """

import numpy as np
import pandas as pd

import ast

credits = pd.read_csv('datasets/credits.csv')
meta = pd.read_csv('datasets/movies_metadata.csv')

meta['release_date'] = pd.to_datetime(meta['release_date'], errors='coerce')
meta['year'] = meta['release_date'].dt.year
# filtering out the data for the year 2017
meta_2017 = meta.loc[meta['year'] == 2017,  
    ['genres', 'id', 'title', 'year']]

# merging the credits and meta_2017 dataframes
meta_2017['id'] = meta_2017['id'].astype(int)
data = pd.merge(meta_2017, credits, on='id')

# Using the ast library to evaluate the string as a python expression
data['genres'] = data['genres'].apply(lambda x: ast.literal_eval(x))
data['cast'] = data['cast'].apply(lambda x: ast.literal_eval(x))
data['crew'] = data['crew'].apply(lambda x: ast.literal_eval(x))

# Extracting the information from genres, cast, crew


def make_genresList(x):
    gen = []
    for i in x:
        if i.get('name') == 'Science Fiction':
            scifi = 'Sci-Fi'
            gen.append(scifi)
        else:
            gen.append(i.get('name'))
    if gen == []:
        return np.NaN
    else:
        return ' '.join(gen)


data['genres_list'] = data['genres'].apply(lambda x: make_genresList(x))


def get_actor1(x):
    casts = []
    for i in x:
        casts.append(i.get('name'))
    if casts == []:
        return np.NaN
    else:
        return (casts[0])


data['actor_1_name'] = data['cast'].apply(lambda x: get_actor1(x))


def get_actor2(x):
    casts = []
    for i in x:
        casts.append(i.get('name'))
    if casts == [] or len(casts) <= 1:
        return np.NaN
    else:
        return (casts[1])


data['actor_2_name'] = data['cast'].apply(lambda x: get_actor2(x))


def get_actor3(x):
    casts = []
    for i in x:
        casts.append(i.get('name'))
    if casts == [] or len(casts) <= 2:
        return np.NaN
    else:
        return (casts[2])


data['actor_3_name'] = data['cast'].apply(lambda x: get_actor3(x))


def get_directors(x):
    directors = []
    for i in x:
        if i.get('job') == 'Director':
            directors.append(i.get('name'))
    if directors == []:
        return np.NaN
    else:
        return " ".join(directors)


data['director_name'] = data['crew'].map(lambda x: get_directors(x))

data_2017 = data[['director_name', 'actor_1_name', 'actor_2_name',
                'actor_3_name', 'genres_list', 'title']]
data_2017 = data_2017.dropna(axis=0, how='any')

# Making changes to match our other dataset with movies thru 2016 (data.csv)
data_2017 = data_2017.rename(columns={'genres_list':'genres', 'title':'movie_title'})
data_2017['movie_title'] = data_2017['movie_title'].str.lower()

# Making a column with a combination of all the information 
# which will be useful later for our recommender system
data_2017['comb'] = data_2017['actor_1_name'] + ' ' + \
    data_2017['actor_2_name'] + ' ' + data_2017['actor_3_name'] \
    + ' ' + data_2017['director_name'] + ' ' + data_2017['genres']
