"""Calling out the function to extract the data from wikipedia for the year 2018"""

from mainData import generate_movie_data

url_2018 = "https://en.wikipedia.org/wiki/List_of_American_films_of_2018"
data_2018 = generate_movie_data(url_2018)
