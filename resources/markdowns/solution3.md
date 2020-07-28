# Content Based Recommender System

The content based recommender system built below uses a cosine similarity matrix to find similarities in movies based on three previously watched movies. The recommender system relies on the properties of the movies in the dataset to make comparisons. 

We will be using the movie data (genre) as well as the imdb data set (actors, directors and the keywords).

## Data Preprocessing

We now split genre data into individual words and create a separate column for the year

```python
movies_data['year'] = movies_data.title.str.extract('(\(\d\d\d\d\))',expand=False)
movies_data['year'] = movies_data.year.str.extract('(\d\d\d\d)',expand=False)
movies_data.year.fillna(value=0,inplace=True)

movies_data['title_101'] = movies_data.title.str.replace('(\(\d\d\d\d\))', '')

movies_data['title_gen_yr'] = pd.Series(movies_data[['title_101', 'genres',
                                'year']].values.tolist()).str.join(' ')

movies_data.genres = movies_data['title_gen_yr']
movies_data.drop(['title_101','year','title_gen_yr'],axis=1,inplace=True)
```

In the code cell below, we define a recommender_ function which creates a list of the top movies to recommend. The selection is based on the cosine similarity between the selected movies and the rest of the movies in the dataset. This function is defined within a content_based_recommendation function which uses the recommender_ function to compile the top_n movies that the user would likely be willing to watch.

### Making Predictions

Make predictions of the movies that the user might like to watch, given three movies that they have watched before. We select 3 movies (movies that have been watched before) and display the names of the movies selected

```python
watched_movies = [movies_data.title[565],
              movies_data.title[5951],
              movies_data.title[50101]]

# display the names of the movies selected
count = ['first','second','third']
for i,movie_name in enumerate(watched_movies):
    print(f'The {count[i]} movie:\t{movie_name}')
```

```python
The first movie:	Foreign Student (1994)
The second movie:	May (2002)
The third movie:	Hotel Salvation (2016)
```

We now ouput the top_n recommended movies returned by the content based algorithm

```python
recommended_movies = content_based_recommendation(movie_list=watched_movies,top_n=10)
print(recommended_movies)
```

```python
['Seance on a Wet Afternoon (1964)',
 'Crowd, The (1928)',
 'House of Games (1987)',
 'Highway 61 (1991)',
 'Happy Birthday to Me (1981)',
 'Lancelot of the Lake (Lancelot du Lac) (1974)',
 'Going Ape! (1981)',
 'Explorers (1985)',
 'Man-Thing (2005)',
 'Bittersweet Life, A (Dalkomhan insaeng) (2005)']
```

Given the movies Foreign Student (1994), May (2002) and Hotel Salvation (2016), the content_based_recommendation function was able to make predictions of the top 10 movies that the user might also like to watch. This is based on the cosine similarities of the movies selected.