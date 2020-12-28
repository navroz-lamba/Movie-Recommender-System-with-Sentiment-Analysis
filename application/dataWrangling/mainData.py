"""This file consists of a function to generate movie data by scraping
    Wikipedia and using a third party API.
    Also, Generates a csv that contains the movie data through 2020"""

import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import ssl
# For our third party API
from tmdbv3api import TMDb
from tmdbv3api import Movie
import requests

# to load the credentials from env
load_dotenv()

# to fix url open Error
ssl._create_default_https_context = ssl._create_unverified_context

def generate_movie_data(url_link):
    if '2018' in url_link:
        df1 = pd.read_html(url_link, header=0)[2]
        df2 = pd.read_html(url_link, header=0)[3]
        df3 = pd.read_html(url_link, header=0)[4]
        df4 = pd.read_html(url_link, header=0)[5]
    else:
        df1 = pd.read_html(url_link, header=0)[3]
        df2 = pd.read_html(url_link, header=0)[4]
        df3 = pd.read_html(url_link, header=0)[5]
        df4 = pd.read_html(url_link, header=0)[6]

    # appending all the df to get a df with movies from Jan - Dec of 2018
    df = df1.append(df2.append(df3.append(df4, ignore_index=True),
                    ignore_index=True), ignore_index=True)

    # To get the information of genres we will use third party API, tmdb
    tmdb = TMDb()
    tmdb.api_key = os.getenv('TMDB_API_Key')
    tmdb_movie = Movie()

    def get_genre(x):
        genres = []
        result = tmdb_movie.search(x)
        if not result:
            print(f"'{x}' not found in TMDB")
        else:
            movie_id = result[0].id
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
            data_json = response.json()

            if data_json['genres']:
                for i in range(0, len(data_json['genres'])):
                    genres.append(data_json['genres'][i]['name'])

                return " ".join(genres)

            else:
                np.NaN


    df['genres'] = df['Title'].apply(lambda x: get_genre(str(x)))

    df = df[['Title', 'Cast and crew', 'genres']]

    # Extracting out the features from Cast and crew 

    def get_director(x):
        if " (director)" in x:
            return x.split(" (director)")[0]
        elif " (directors)" in x:
            return x.split(" (directors)")[0]
        else:
            return x.split(" (director/screenplay)")[0]


    df['director_name'] = df['Cast and crew'].apply(lambda x: get_director(str(x)))

    df['actor_1_name'] = df['Cast and crew'].map \
        (lambda x: (str(x).split("screenplay); ")[-1]).split(", ")[0])
    
    def get_actor2(x):
        if len((str(x).split("screenplay); ")[-1]).split(", ")) < 2:
            return np.NaN
        else:
            return ((str(x).split("screenplay); ")[-1]).split(", ")[1])


    df['actor_2_name'] = df['Cast and crew'].map(lambda x: get_actor2(x))

    def get_actor3(x):
        if len((str(x).split("screenplay); ")[-1]).split(", ")) < 3:
            return np.NaN
        else:
            return ((str(x).split("screenplay); ")[-1]).split(", ")[2])


    df['actor_3_name'] = df['Cast and crew'].apply(lambda x: get_actor3(x))

    df = df.rename(columns={'Title': 'movie_title'})

    new_df = df.loc[:, ['director_name', 'actor_1_name',
                    'actor_2_name', 'actor_3_name', 'genres', 'movie_title']]

    new_df['actor_2_name'] = new_df['actor_2_name'].replace(np.nan, 'unknown')
    new_df['actor_3_name'] = new_df['actor_3_name'].replace(np.nan, 'unknown')
    new_df['movie_title'] = new_df['movie_title'].str.lower()

    # Making a column with a combination of all the information 
    # which will be useful later for our recommender system
    new_df['comb'] = new_df['actor_1_name'] + ' ' + \
        new_df['actor_2_name'] + ' ' + new_df['actor_3_name'] \
        + ' ' + new_df['director_name'] + ' ' + new_df['genres']
    
    return new_df


if __name__ == '__main__':

    # To generate a csv with the movie data through 2020
    from data_thru_2016 import data_2016
    from data_2017 import data_2017
    from data_2018 import data_2018
    from data_2019 import data_2019
    from data_2020 import data_2020

    # appending all the datasets together
    main_data = data_2016.append(data_2017.append(data_2018.append
            (data_2019.append(data_2020, ignore_index=True), 
            ignore_index=True), ignore_index=True), ignore_index=True)
    
    # creating a csv
    main_data.to_csv('main_data.csv', index=False)
    print(main_data.shape)
