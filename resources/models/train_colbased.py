"""

    Single Value Decomposition plus plus (SVDpp) model training.

    Author: Explore Data Science Academy.

    Description: Simple script to train and save an instance of the
    SVDpp algorithm on MovieLens data.

"""
# Script dependencies
import numpy as np
import pandas as pd
from surprise.prediction_algorithms import SVD
from surprise import Reader, Dataset
import pickle

# Importing datasets
# movies = pd.read_csv('movies.csv',encoding='Latin1')
train = pd.read_csv('ratings.csv')

def svd_pp(save_path):
    # Create Training set
    reader = Reader(rating_scale = (0.5, 5))
    data = Dataset.load_from_df(train[['userId','movieId','rating']], reader)
    train_set = data.build_full_trainset()

    # Create and Train Model
    model_tuned = SVD(n_factors = 90, n_epochs = 150, lr_all = 0.01, reg_all = 0.1)
    model_tuned.fit(train_set) 
    print (f"Training completed. Saving model to: {save_path}")

    return pickle.dump(model_tuned, open(save_path,'wb'))

if __name__ == '__main__':
    svd_pp('SVDT.pkl')
