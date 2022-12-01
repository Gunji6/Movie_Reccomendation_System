import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=553eb16269f3625abe4efc0cb2cc8438&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommend_movies = []
        recommend_movies_poster = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommend_movies.append(movies.iloc[i[0]].title)
            # fetch poster from API
            recommend_movies_poster.append(fetch_poster(movie_id))
        return recommend_movies , recommend_movies_poster
