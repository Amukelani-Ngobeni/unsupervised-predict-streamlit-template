
We will be going over the modelling processes we used to create different types of Recommender Systems. The Recommender Systems were movie systems which were created using data from Movielens,TMDB and IMDB. Both Content Based and Collaborative Based models were used leading to very interesting results..

# Collaborative Based Filtering

## Modelling
Initialising a reader to read in and load data from the train df for use in our Models.

```python
reader = Reader(rating_scale = (0.5, 5))
data = Dataset.load_from_df(train[['userId','movieId','rating']], reader)
```

### Splitting the ratings dataset into train and test sets
We split the data into a train and test set so we can train our models usings the train set.This split helps us test to see how well the models perform when we run then on the test set which is 20% of the whole dataset. We use a random_state of 42 so the results can be replicated else where if needed.

```python
train_set = data.build_full_trainset()
trainset,testset = train_test_split(data,test_size=0.2,random_state=42)
```
---
---

## K-NN Based Algorithms

In order to use the various k-NN models, we need to create a subset of our train dataset as this model cannot handle the full dataset unlike the SVD model.


This subset will include the most common users and movies.

Find the common ids of movies and users to add to the subset dataset
We will be taking the 2700 of the top users and 650 of the top movies. This will be used to create a subset df. We would have reduced the train dataset to ~430000 rows

```python
uid= [u for u,c in Counter(train.userId).most_common(2700)]
mid = [m for m,c in Counter(train.movieId).most_common(650)]

subset_df = train[train.userId.isin(uid) & train.movieId.isin(mid)]
```
Initialising a reader to read in and load data from the subset train. Then we load the data from the subset dataframe and split the subset dataset into training and testing 

```python
reader = Reader(rating_scale = (0.5, 5))
subset_data = Dataset.load_from_df(subset_df[['userId','movieId','rating']], reader)

subset_train,subset_test = train_test_split(subset_data, test_size = 0.2, random_state = 42)
```


### KNNWithMeans Algorithm

Now we can explore the KNNWithMeans algorithm and see how the cosine similarity it applies for both user and item based  collaborative filtering works on our subset of data, by viewing the RMSE.

First we will apply the item-based algorithm of the KNNWithMeans.

We initialise KNNWithMeans model using cosine similarity matrix item-based approach. Then fit the model to training subset and make predictions. We then calculate the RMSE of the model

```python
KNN_item = KNNWithMeans(sim_options = {"name" : "cosine", "user_based" : False})
KNN_item.fit(subset_train)
predictions_knn_item = KNN_item.test(subset_test)
rmse_knn_item = accuracy.rmse(predictions_knn_item)
print('RMSE:',rmse_knn_item)
```
```python
RMSE: 0.7902127881187059
```

We repeat the same process but for a KNNWithMeans user-based algorithm

```python
KNN_user = KNNWithMeans(sim_options = {"name" : "cosine", "user_based" : True})
KNN_user.fit(subset_train)
predictions_knn_user = KNN_user.test(subset_test)
rmse_knn_user = accuracy.rmse(predictions_knn_user)
print('RMSE:',rmse_knn_user)
```

```python
RMSE: 0.801282884986959
```

### KNNBasic Algorithm

We will be following similar steps as the KnnWithMeans model to see how the KnnBasic performs.

Starting with the item-based approach.

The process will be followed as before

```python
knnbasic_item = KNNBasic(sim_options = {"name" : "cosine", "user_based" : False})
knnbasic_item.fit(subset_train)
predictions_knnbasic_item = knnbasic_item.test(subset_test)
rmse_knnbasic_item = accuracy.rmse(predictions_knnbasic_item)
print('RMSE:',rmse_knnbasic_item)
```
```python
RMSE: 0.8751269517416773
```

Now to apply the KnnBasic user-based algorithm.

```python
knnbasic_user = KNNBasic(sim_options = {"name" : "cosine", "user_based" : True})
knnbasic_user.fit(subset_train)
predictions_knnbasic_user = knnbasic_user.test(subset_test)
rmse_knnbasic_user = accuracy.rmse(predictions_knnbasic_user)
print('RMSE:',knnbasic_user)
```
```python
RMSE: 0.9026392370515729
```

### KNN Model Performance 

Let us view the results of the item based and user based approaches of the KNNWithMeans algorithm and the KNNBasic Algorithm.

We start by visualising and comparing the RMSE of the KNNWithMeans and the KNNBasic model

We then create a line plot of RMSE of k-NN models user and item based
