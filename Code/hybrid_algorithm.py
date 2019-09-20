# -*- coding: utf-8 -*-
from math import sqrt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# film=pd.read_csv('../Dataset/data_content.csv',delimiter=';') #dataset of film

# import os
# import sys
# os.chdir('..')
# cwd = os.getcwd() + '/Dataset'
# sys.path.insert(0, cwd)
# from recommendation_data import dataset

# usr_rating=pd.DataFrame(dataset) #dataset of user's rating

class JulHybrid():
    """docstring for ClassName"""
    def __init__(self, film, dataset):
        self.dataset = dataset
        self.film = film
        self.usr_rating = pd.DataFrame(dataset)
        
    # function description: get recommended film from the similarities between the films -> this is why it called 'content based'
    def content_based(self, person, min_content_score):

        #1 - START - check in usr_rating, get movies that the person did not watch yet
        k=0
        not_watch=[]
        for i in self.usr_rating[person]:
            if i==0:
                not_watch.append(self.usr_rating.index[k])
                k=k+1
            else:
                k=k+1
        # 1 - END - not_watch will filled by movies that the person did not watch yet
        # example: not_watch = ['Aladdin', 'Bumi Manusia', 'Dua Garis Biru', 'The Lion King']
        
        # 2 - START - Convert a collection of raw documents (movie description) to a matrix of TF-IDF features.
        tf = TfidfVectorizer(analyzer='word',
                                 ngram_range=(1, 3),
                                 min_df=0,
                                 stop_words='english')
        tfidf_matrix = tf.fit_transform(self.film['Description'])
        # 2 - END - a matrix of TF-IDF features
        # tfidf = [0.2847195009092169, 0.2847195009092169, 0.32024359109404055 ..........]
        
        # 3 - START - Compute similarities between movies
        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
        # 3 - END - Matrix with similarities between movies. see the output of cosine_similarities at : https://imgur.com/GOW1KmH
        # so from this matrix, we conclude that bumi manusia and dua garis biru is similar (dilihat dari deskripsinya)
        
        # 4 - START - Create dataframe from cosine similarities
        new = pd.DataFrame(cosine_similarities,index=self.film['Film'],columns=self.film['Film'])
        # 4 - END - see the output of new at : https://imgur.com/c3405is
        
        # 5 - START - create dataframe of not watched films, compute the mean score(similarity), and sort it as ascending
        final = pd.DataFrame(new[not_watch].mean().sort_values(ascending=False),columns=['Score'])
        # 5 - END - see the output of final at : https://imgur.com/x27svfw
        
        # 6 - START - from final, filter it, and get the film which have score(similarty) greater that min_content_score
        final2 = final[final.Score>=min_content_score]
        indeks = final2.index
        
        return indeks
        # 6 - END - return the filterred films
        
    def person_correlation(self, person1, person2):

       # To get both rated items
        both_rated = {}
        for item in self.dataset[person1]:
            if item in self.dataset[person2]:
                both_rated[item] = 1

        number_of_ratings = len(both_rated)

        # Checking for ratings in common
        if number_of_ratings == 0:
            return 0

        # Add up all the preferences of each user
        person1_preferences_sum = sum([self.dataset[person1][item] for item in both_rated])
        person2_preferences_sum = sum([self.dataset[person2][item] for item in both_rated])

        # Sum up the squares of preferences of each user
        person1_square_preferences_sum = sum([pow(self.dataset[person1][item],2) for item in both_rated])
        person2_square_preferences_sum = sum([pow(self.dataset[person2][item],2) for item in both_rated])

        # Sum up the product value of both preferences for each item
        product_sum_of_both_users = sum([self.dataset[person1][item] * self.dataset[person2][item] for item in both_rated])

        # Calculate the pearson score
        numerator_value = product_sum_of_both_users - (person1_preferences_sum*person2_preferences_sum/number_of_ratings)
        denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/number_of_ratings))

        if denominator_value == 0:
            return 0
        else:
            r = numerator_value / denominator_value
            return r

    def user_recommendations(self, person, min_content_score):

        # Gets recommendations for a person by using a weighted average of every other user's rankings
        totals = {}
        simSums = {}
        rankings_list =[]
        for other in self.dataset:
            # don't compare me to myself
            if other == person:
                continue
            sim = self.person_correlation(person,other)
            #print ">>>>>>>",sim. see the output at : 

            # ignore scores of zero or lower
            if sim <=0: 
                continue
            for item in self.dataset[other]:

                # only score movies i haven't seen yet
                if item not in self.dataset[person] or self.dataset[person][item] == 0:

                # Similrity * score
                    totals.setdefault(item,0)
                    totals[item] += self.dataset[other][item]* sim
                    # sum of similarities
                    simSums.setdefault(item,0)
                    simSums[item]+= sim
        # final output of simSums : https://imgur.com/ENrTS3h
        
        # Create the normalized list
        rankings = [(total/simSums[item],item) for item,total in totals.items()]
        #sorting and reversing, means sort it descending
        rankings.sort(reverse=True)

        # START - loop through user based recommendation list, and check if it is also recommended
        # by content based recommendation ->>> the hybrid is here! we menggabungkan user based recommendation and content based recommendation
        new_rankings = []
        content_based_recommendation_list = self.content_based(person,min_content_score)
        for i in rankings:
            if i[1] in content_based_recommendation_list:
                new_rankings.append(i[1])
        # END
            
        return new_rankings

    def predict(self, person='jul', min_content_score=0.1):
        return self.user_recommendations(person,min_content_score)

# print('List of user : ', self.usr_rating.columns)

# name = input('Your name :')
# min_content_score = input('Minimum Score Film :')
# recommendation = predict(name,float(min_content_score))
# print(recommendation)