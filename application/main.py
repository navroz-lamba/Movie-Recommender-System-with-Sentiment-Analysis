import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import bs4 as bs
import urllib.request
import joblib
import requests


def create_similarity():
    data = pd.read_csv('datasets/main_data.csv')
    data.comb.fillna('', inplace=True)
    # creating a count matrix
    tfidf = CountVectorizer()
    count_matrix = tfidf.fit_transform(data['comb'])
    # creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return data, similarity


def rcmd(movie):
    movie = movie.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()

    if movie not in data['movie_title'].unique():
        return('Sorry! The movie you requested is not in our database.')
             
    else:
        idx = data.loc[data['movie_title'] == movie].index[0]
        lst = list(enumerate(similarity[idx]))
        lst = sorted(lst, key=lambda x : x[1], reverse=True)
        lst = lst[1:11] # top 10
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movie_title'][a])
        return l # list of top 10 recommended movies
    

# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["', '')
    my_list[-1] = my_list[-1].replace('"]', '')
    return my_list


# for autocomplete
def get_suggestions():
    data = pd.read_csv('datasets/main_data.csv')
    print(data['movie_title'][0])
    return list(data['movie_title'].str.capitalize())
