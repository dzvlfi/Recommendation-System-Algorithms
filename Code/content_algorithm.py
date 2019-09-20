# -*- coding: utf-8 -*-
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

class JulContentBased():
    """docstring for Content"""

    def __init__(self, df):
        self.df_new = df[['jenis','genre','rating','duration']]
        self.df_new.index = df['movie']
        self.scal = MinMaxScaler()
        self.df_new = self.scal.fit_transform(self.df_new)
        self.cosine_sim = cosine_similarity(self.df_new,self.df_new)
        self.indices = df['movie']

    def predict(self, nama_film):
        rujukan = self.recommendations(nama_film, self.indices, self.cosine_sim)
        return rujukan
        
    def recommendations(self, title, indices, cosine_sim):

        recommended_movies = []
        # gettin the index of the movie that matches the title
        idx = indices[indices == title].index[0]

        # creating a Series with the similarity scores in descending order
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

        # getting the indexes of the 3 most similar movies
        top = list(score_series.iloc[1:4].index)
        
        # populating the list with the titles of the best 3 matching movies
        for i in top:
            recommended_movies.append(indices[i])
            
        return recommended_movies