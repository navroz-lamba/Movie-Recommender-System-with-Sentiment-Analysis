""" This file generates a csv with movies released until the year 2016 """

import pandas as pd
import numpy as np

data = pd.read_csv('datasets/movie_metadata.csv')


data = data[['director_name', 'actor_1_name', 'actor_2_name',
            'actor_3_name', 'genres', 'movie_title']]


def wrangle(X):
    # remove the pipe symbol for seperation in genres
    X['genres'] = X['genres'].str.replace('|', ' ')

    # strip '\xa0' from all the titles in the dataset
    X['movie_title'] = X['movie_title'].str.strip('\xa0')

    X['movie_title'] = X['movie_title'].str.lower()

    # replace all the Nan values with 'unkownn'
    cols = ['director_name', 'actor_3_name', 'actor_2_name', 'actor_1_name', 
            'movie_title', 'genres']
    for col in cols:
        X[col] = X[col].replace(np.nan, 'unknown')

    return X


data_2016 = wrangle(data)

# Making a column with a combination of all the information
# which will be useful later for our recommender system
data_2016['comb'] = data_2016['actor_1_name'] + ' ' + \
    data_2016['actor_2_name'] + ' ' + data_2016['actor_3_name'] \
    + ' ' + data_2016['director_name'] + ' ' + data_2016['genres']
