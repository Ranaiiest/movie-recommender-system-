import streamlit as st 
import pickle
import pandas as pd

def recommend(movie):
    # get the index of the movie
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    # sorting reverse order but the problem is index change ho jayga
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6] #we hv to sort
    # according to second wala number
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title) # print the first element from the tuple
    #now just convert this to a website
    return recommended_movies


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Enter the Movie Name :',
    movies['title'].values
)


if st.button('Recommend'):
    recommenations = recommend(selected_movie_name)
    for i in recommenations:
        st.write(i)