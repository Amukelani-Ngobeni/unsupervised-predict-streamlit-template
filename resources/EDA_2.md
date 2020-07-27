

### Vote Average and Vote Count

We will analyse movies based on their ratings. We will try to gain a deeper understanding of ratings score and the count of those ratings in order to get a better ranking of the movies.


```python
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



Figure 2.1-Figure 2.3: All movies have a rating score less than 5 (the 75th percentile is at 3.8795). The **Max Rating is 4.51** and **the lowest is 1.01**

The rating score has a mean of  **3.5** and maximum values of **4.5**. (Movies with less than 100 ratings have been removed.) 




