
#### Earliest Movies Represented


The oldest movie, **Two Fencers**, a 1min | Short, Sport | 2 January 1891 (France) Shot of two people fencing.

The oldest film is Passage of Venus	from 1874. But due to our filtering, we have eliminated this film and anything before 1891. 


### Runtime

From its humble beginnings of 1 minute silent, black & white clips to epic 3 hour visual delights, movies have a come a long way in terms of runtime. In this section, let us try and gain some additional insights about the nature of movie lengths and their evolution over time.


```python
imdb_data['runtime'].describe()
```




    count    15189.000000
    mean       100.312331
    std         31.061707
    min          1.000000
    25%         89.000000
    50%         98.000000
    75%        109.000000
    max        877.000000
    Name: runtime, dtype: float64



The average length of a movie is about 1 hour and 40 minutes. The longest movie on record in this dataset is a **staggering 877 minutes (or 14.6 hours) long.**

We are aware that most movies are less than 5 hours (or 300 minutes) long. Let us plot a distribution of these mainstream movies.

Is there any meaningful relationship between runtime and budget? Let us find out!

Figure 6.1- Figure 6.2: There seems to be relationship between the two quantities. **The duration of a movie is independent of its success.** However, I have a feeling this might not be the case with duration and budget. A longer movie should entail a higher budget. Let us find out if this is really the case.

Let us check the average lengths of movies through time, right from the 1890s to current. It would be interesting to see how the appropriate length of a movie has changed as humans have more screens that want their eyeballs attention.

We notice that films started hitting the **60 minute mark as early as 1914**. Starting **1924**, films started having the traiditonal 90 minute duration and has remained more or less constant ever since.

Finally in this section, let us see the longest and the shortest movies of all time (with respect to the movies in the dataset). 

#### Shortest Movies

It seems that the duration of the shortest film has increased over the years, from around 2 minutes in the 1960s to 15 minutes in the 20s.

#### Longest Movies

Our longest movie is just over 360 minutes and most of the featured movies average just over 3 hrs in length.

