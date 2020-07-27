"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview", "EDA"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    
    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "EDA":
        st.info("Explanatory Data Analysis")

        #Wordcloud visualizations
        eda_1 = open("resources/EDA_1.md","r")
        st.markdown(eda_1.read())
        st.image('resources/EDA_rec_files/EDA_rec_48_0.png',use_column_width=True)
        st.write('Figure 1.1')
        st.image('resources/EDA_rec_files/EDA_rec_50_0.png',use_column_width=True)
        st.write('Figure 1.2')

        #Vote count and average
        eda_2 = open("resources/EDA_2.md","r")
        st.markdown(eda_2.read())
        st.image('resources/EDA_rec_files/EDA_rec_66_0.png',use_column_width=True)
        st.write('Figure 2.1')
        st.image('resources/EDA_rec_files/EDA_rec_67_1.png',use_column_width=True)
        st.write('Figure 2.2')
        st.image('resources/EDA_rec_files/EDA_rec_69_0.png',use_column_width=True)
        st.write('Figure 2.3')

        #Popular movies by count
        eda_3 = open("resources/EDA_3.md","r")
        st.markdown(eda_3.read())
        st.image('resources/EDA_rec_files/EDA_rec_80_1.png',use_column_width=True)
        st.write('Figure 3')

        #Critical acclaimed
        eda_4 = open("resources/EDA_4.md","r")
        st.markdown(eda_4.read())
        st.image('resources/EDA_rec_files/EDA_rec_86_1.png',use_column_width=True)
        st.write('Figure 4.1')
        st.image('resources/EDA_rec_files/EDA_rec_88_1.png',use_column_width=True)
        st.write('Figure 4.2')

        #Movies by Year
        eda_5 = open("resources/EDA_5.md","r")
        st.markdown(eda_5.read())
        st.image('resources/EDA_rec_files/genre_86_1.png',use_column_width=True)
        st.write('Figure 5')

        #Runtime
        eda_6 = open("resources/EDA_6.md","r")
        st.markdown(eda_6.read())
        st.image('resources/EDA_rec_files/EDA_rec_102_1.png',use_column_width=True)
        st.write('Figure 6.1')
        st.image('resources/EDA_rec_files/EDA_rec_104_0.png',use_column_width=True)
        st.write('Figure 6.2')
        

        #Genres
        eda_7 = open("resources/EDA_7.md","r")
        st.markdown(eda_7.read())
        st.image('resources/EDA_rec_files/genre_131_0.png',use_column_width=True)
        st.write('Figure 7')
        
        #Users
        eda_8 = open("resources/EDA_8.md","r")
        st.markdown(eda_8.read())
        st.image('resources/EDA_rec_files/final_152_0.png',use_column_width=True)
        st.write('Figure 8.1')

        eda_9 = open("resources/EDA_9.md","r")
        st.markdown(eda_9.read())
        st.image('resources/EDA_rec_files/final_154_0.png',use_column_width=True)
        st.write('Figure 8.2')

        eda_10 = open("resources/EDA_10.md","r")
        st.markdown(eda_10.read())
        st.image('resources/EDA_rec_files/final_156_0.png',use_column_width=True)
        st.write('Figure 8.3')

        eda_11 = open("resources/EDA_11.md","r")
        st.markdown(eda_11.read())
        st.image('resources/EDA_rec_files/final_158_0.png',use_column_width=True)
        st.write('Figure 8.4.1')
        st.image('resources/EDA_rec_files/final_160_0.png',use_column_width=True)
        st.write('Figure 8.4.2')
        st.image('resources/EDA_rec_files/final_161_0.png',use_column_width=True)
        st.write('Figure 8.4.3')


    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
