# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import os

#load data from dataset
os.chdir('..')
df = pd.read_csv(os.getcwd() + '/Dataset/cont-dataset.csv')

df_new = df[['jenis','genre','rating','duration']]
df_new.index = df['movie']

scal = MinMaxScaler()
df_new = scal.fit_transform(df_new)

#result_df = pd.DataFrame(
cosine_sim = cosine_similarity(df_new,df_new) #, columns=df['movie'], index=df['movie'])
indices = df['movie']
#print(result_df)

def recommendations(title, cosine_sim = cosine_sim):
    
    recommended_movies = []
    
    # gettin the index of the movie that matches the title
    idx = indices[indices == title].index[0]

    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    # getting the indexes of the 10 most similar movies
    top_10_indexes = list(score_series.iloc[1:11].index)
    
    # populating the list with the titles of the best 10 matching movies
    for i in top_10_indexes:
        recommended_movies.append(df['movie'][i]) #list(df.index)[i])
        
    return recommended_movies

rujukan = recommendations('Avenger')
print(rujukan)