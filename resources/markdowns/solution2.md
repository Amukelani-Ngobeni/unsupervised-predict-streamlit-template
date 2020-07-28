## Singular Value Decomposition (SVD) 

We will be using the full train set and test set we created earlier

We will start by initialising the SVD model and fitting the train set using the base model

```python
model = SVD()
model.fit(trainset)
```

Making predictions and calculating the local RMSE

```python
model.predict('userId','itemId')
predictions = model.test(testset)
base_rmse = accuracy.rmse(predictions)
print('RMSE:',base_rmse)
```
```python
RMSE: 0.8336512268872064
```

Now that we have established a baseline RMSE then we can perform hyperparameter tuning on our SVD model to achieve better results

### Hyperparameter Tuning 

Below we will use a GridSearchSV to optimise our SVD model by finding the optimal parameters. 

```python
param_grid = {'n_factors':[90,130],'n_epochs':[75,150],  
              'lr_all':[0.005,0.01],'reg_all':[0.02,0.1]}
gs = GridSearchCV(SVD, param_grid, measures=['rmse'], cv=3)
gs.fit(data)
params = gs.best_params['rmse']
```

Based on our GridSearch, we know that the optimal parameters are as follows: <br>
params = {'n_factors' : 90, 'n_epochs' : 150, 'lr_all' : 0.01, 'reg_all' : 0.1}   

Now we can user the parameters found above in our SVD model to see how it affects the RMSE.

```python
model_tuned = SVD(n_factors = 90, n_epochs = 150, lr_all = 0.01, reg_all = 0.1)
model_tuned.fit(trainset) 
```

Making predictions and calculating the local RMSE

```python
model_tuned.predict('userId','itemId')
predictions_tuned = model_tuned.test(testset)
tuned_rmse = accuracy.rmse(predictions_tuned)
print('RMSE:',tuned_rmse)
```

### Model Performance 

We will now take a look at theperformance of the SVD model before and after tuning it's parameters.

RMSE: 0.8342

RMSE: 0.8189

As we can see from the graph below, the RMSE of the SVD model has decreased after tuning it with parameters found in the GridSearchSV. For our Kaggle submission we will be using this tuned SVD model fitted on the full trainset as this will allow the model to predict more precisely since it is training on a larger dataset. For Streamlit we will be using the tuned SVD model fitted on the dataset given