# Content Based Movie Recommender System with sentiment analysis using AJAX
![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-green)
![API](https://img.shields.io/badge/API-TMDB-fcba03)

Content Based Recommender System recommends movies similar to the movie user likes, and analyses the sentiments on the reviews given by the user for that movie.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api. Also, using the IMDB id of the movie from the API, I performed web scraping using beautifulsoup4 to extract the reviews given by the user on the IMDB site, and performed sentiment analysis on those reviews.

Check out the live demo: 

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/67918990/103171183-14c80580-4818-11eb-9c5b-1f7e41362095.gif)

How to get the API key?
Create an account on https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved.

How to run the project?
• Install all the dependencies in the requirements.txt file.
• Clone this repository in your local system.
• Replace YOUR_API_KEY in the static/recommend.js file.
• Run mainData.py to generate a csv with the movie data all the way through 2020. 
• Open the command prompt from your project directory and run the command 'python run.py'.
• Go to your browser and type http://127.0.0.1:5000/ in the address bar.
• ALL SET! 

Content Bases Recommender System:
How does it decide which movie is most similar to the movie that user likes? 
I did that using the cosine-similarity. 

How does Cosine Similarity work?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

  ![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)
  
More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

### Sources of the datasets 

1. [IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)
2. [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
3. [List of movies in 2018](https://en.wikipedia.org/wiki/List_of_American_films_of_2018)
4. [List of movies in 2019](https://en.wikipedia.org/wiki/List_of_American_films_of_2019)
5. [List of movies in 2020](https://en.wikipedia.org/wiki/List_of_American_films_of_2020)
