"""Calling out the function to extract the data from wikipedia for the year 2020"""

from mainData import generate_movie_data

url_2020 = "https://en.wikipedia.org/wiki/List_of_American_films_of_2020"
data_2020 = generate_movie_data(url_2020)
