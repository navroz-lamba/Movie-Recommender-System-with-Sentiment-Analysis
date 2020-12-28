"""Calling out the function to extract the data from wikipedia for the year 2019"""

from mainData import generate_movie_data

url_2019 = "https://en.wikipedia.org/wiki/List_of_American_films_of_2019"
data_2019 = generate_movie_data(url_2019)
