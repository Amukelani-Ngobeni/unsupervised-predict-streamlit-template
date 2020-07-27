
#### Most Popular Movies by Count of Ratings


**Rockstar** is the most popular movie by the TMDB Popularity Score. **Wonder Woman** and **Beauty and the Beast**, two extremely successful woman centric movies come in second and third respectively.


```python
df['rating_count'].describe()
```




    count    9.601947e+06
    mean     6.277069e+03
    std      6.584404e+03
    min      1.000000e+02
    25%      1.500000e+03
    50%      4.054000e+03
    75%      8.803000e+03
    max      3.283100e+04
    Name: rating_count, dtype: float64



As with popularity scores, the distribution of vote counts is extremely skewed with the median vote count standing at a paltry 10 votes. The most votes a single movie has got stands at 14,075. TMDB Votes, therefore, are not as potent and suggestive as its IMDB Counterpart. Nevertheless, let us check which the most voted on movies on the website are.

#### Most Voted on Movies


```python
df['mean_rating'] = df['mean_rating'].replace(0, np.nan)
df['mean_rating'].describe()
```




    count    9.601947e+06
    mean     3.548030e+00
    std      4.472693e-01
    min      1.011236e+00
    25%      3.281949e+00
    50%      3.622649e+00
    75%      3.879545e+00
    max      4.517084e+00
    Name: mean_rating, dtype: float64



Figure 3: TMDB Users ratings can be seen as fair. The mean rating is **3.3** on a scale of 5. 75% of films have a 3.7 score or higher. 

Let us check what the most critically acclaimed movies as per TMDB are. We will only consider those movies that have more than 2000 votes (similar to IMDB's criteria of 5000 votes in selecting its top 250).

