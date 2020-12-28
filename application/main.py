import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def create_similarity():
    data = pd.read_csv('main_data.csv')
    data['comb'].fillna(" ", inplace=True)
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])
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
        cos_score = list(enumerate(similarity[idx]))
        cos_score = sorted(cos_score, key=lambda x : x[1], reverse=True)
        cos_score = cos_score[1:11]  # top 10
        top_10 = []
        for i in range(len(cos_score)):
            movie_indices = cos_score[i][0]
            top_10.append(data['movie_title'][movie_indices])
        return top_10  # list of top 10 recommended movies
    

# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["', '')
    my_list[-1] = my_list[-1].replace('"]', '')
    return my_list


# for autocomplete
def get_suggestions():
    data = pd.read_csv('main_data.csv')
    return list(data['movie_title'].str.capitalize())
