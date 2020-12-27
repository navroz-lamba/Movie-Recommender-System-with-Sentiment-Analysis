# Content Based Movie Recommender System with sentiment analysis using AJAX
Python Framework Frontend API

Content Based Recommender System recommends movies similar to the movie user likes, and analyses the sentiments on the reviews given by the user for that movie.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api. Also, using the IMDB id of the movie in the API, I performed web scraping using beautifulsoup4 to extract the reviews given by the user on the IMDB site, and performed sentiment analysis on those reviews.

Check out the live demo: 

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

Similarity Score :
How does it decide which item is most similar to the item user likes? Here we use the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

image

More about Cosine Similarity : Understanding the Math behind Cosine Similarity

Sources of the datasets
IMDB 5000 Movie Dataset
The Movies Dataset
List of movies in 2018
List of movies in 2019
List of movies in 2020
