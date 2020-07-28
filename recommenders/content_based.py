"""

    Content-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `content_model` !!

    You must however change its contents (i.e. add your own content-based
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline content-based
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import operator 
import heapq

# Importing data
movies = pd.read_csv('./resources/data/movies.csv', sep = ',',delimiter=',')
ratings = pd.read_csv('./resources/data/ratings.csv')
movies.dropna(inplace=True)

def data_preprocessing(subset_size):
    """Prepare data for use within Content filtering algorithm.

    Parameters
    ----------
    subset_size : int
        Number of movies to use within the algorithm.

    Returns
    -------
    Pandas Dataframe
        Subset of movies selected for content-based filtering.

    """
    # Split genre data into individual words.
    movies['genres'] = movies['genres'].str.replace('|', ' ').str.lower()
    
    # create a separate column for the year
    movies['year'] = movies.title.str.extract('(\(\d\d\d\d\))',expand=False)
    movies['year'] = movies.year.str.extract('(\d\d\d\d)',expand=False)

    movies['title_101'] = movies.title.str.replace('(\(\d\d\d\d\))', '')

    movies['title_gen_yr'] = pd.Series(movies[['title_101', 'genres',
                                    'year']].values.tolist()).str.join(' ')

    movies.drop(['year','title_101'],axis=1,inplace=True)
#   data = pd.merge(left=ratings,right = movies,how='left',
#                on='movieId')
    
    # Subset of the data
    movies_subset = movies[:subset_size]
    return movies_subset

movies = data_preprocessing(len(movies))

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  

def content_model(movie_list,top_n=10):
    """Performs Content filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """
    
    def recommender_(start=0,end=10420):
        '''Creates a list of movies to recommend.
        
        Parameters
        ----------
        start: int
            Value to start slicing from.
        end: int
            Value to end slicing.
        
        Returns
        -------
        list (tuples)
            Returns a tuple with the movie name and the similarity score.
        '''
        # Initializing the empty list of recommended movies
        recommended_movies = []
        
        data = movies[start:end]
        
        # make sure the subset of data entails the selected movies
        search = [name for name in data.title]
        
        for movie_title in movie_list:
            if movie_title not in search:
                mini_data = movies[movies.title==movie_title]
                data = pd.concat([mini_data,data])
        
        # Instantiating and generating the tf-idf matrix
        indices = pd.Series(data.title)
        indices.index = [i for i in range(len(indices))]
        
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1,2),
                         min_df=0, stop_words='english')
        
        # with TF-IDF features as columns 
        tf_genre_matrix = tf.fit_transform(data.genres)
        cosine_sim = cosine_similarity(tf_genre_matrix, 
                                        tf_genre_matrix)

        # Getting the index of the movie that matches the title
        idx_1 = indices[indices == movie_list[0]].index[0]
        idx_2 = indices[indices == movie_list[1]].index[0]
        idx_3 = indices[indices == movie_list[2]].index[0]

        # Creating a Series with the similarity scores in descending order
        rank_1 = cosine_sim[idx_1]
        rank_2 = cosine_sim[idx_2]
        rank_3 = cosine_sim[idx_3]

        # Calculating the scores
        score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
        score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
        score_series_3 = pd.Series(rank_3).sort_values(ascending = False)

        # Getting the indexes of the 10 most similar movies
        listings = score_series_1.append(score_series_2).append(
                    score_series_3).sort_values(ascending = False)

        # Appending the index and similarity scores
        top_50_indexes = list(listings.iloc[0:50].index)
        top_50_values = list(listings.iloc[0:50].values)
        
        # find the top 50 scores without the selected movies
        top_50 = {}
        for i in range(50):
            if top_50_indexes[i] not in [idx_1,idx_2,idx_3]:
                top_50[top_50_indexes[i]] = top_50_values[i]
        
        # find the top_n movies
        top_10 = []
        for i,pair in enumerate(top_50.items()):
            if i<top_n:
                top_10.append((movies.title.loc[pair[0]],pair[-1]))
            else:
                break
            
        return top_10
    
    # create a start and end variable for slicing
    start, end = 0, 10420
    result = [] # empty list to store top movies
    
    # use the recommender function to find the top_n movies per subset
    for i in range(6):
        movies_found = recommender_(start,end)
        # check if the movie is notin the result list already
        for mov in movies_found:
            if mov[0] not in result:
                result.append(mov)
        end += 10420
        start += 10420
    
    # sort the movies according to similarity and return the top_n movies
    result = dict(sorted(dict(result).items(), key=lambda x:x[-1],
                         reverse=True))
        
    return [recommended for recommended in result.keys()][:top_n]