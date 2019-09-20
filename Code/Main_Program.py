import pandas as pd
from apriori_algorithm import JulApriori
from content_algorithm import JulContentBased
from hybrid_algorithm import JulHybrid
from collaborative_algorithm import JulCollaborative
import sys
import os
#change dir to main folder for geting a dataset in Dataset directory
os.chdir('..')
dir = os.getcwd() + '/Dataset/'

df_hybrid2 = pd.read_csv(dir + 'data_content.csv',delimiter=';') #dataset of film to process an hybrid algorithm
df_apriori = pd.read_csv(dir + 'apriori-dataset.csv').drop(columns=['Timestamp','Name'])
df_content = pd.read_csv(dir + 'cont-dataset.csv')

sys.path.insert(0, dir) #set work directory to folder dataset to import dataset with *.py extension
from recommendation_data import dataset #import some dataset with a dictionary type

#Collaborative, user based
print('+ Association with apriori: ')
julori = JulApriori()
julori.fit(df_apriori)
julori.result()

#Content based
print('+ Recommendation by content based Avenger: ')
julcontent = JulContentBased(df_content)
print(julcontent.predict('Avenger'))

print('=====================================')
#Collaborative
print('+ Collaborative Filtering: ')
julcollab = JulCollaborative(dataset)
recommendation, score = julcollab.user_recommendations('Dpv')
print('user recommendation for Dpv with score: ', score)
print('user correlation score between Dpv and Star: ', julcollab.person_correlation('Dpv', 'Star'))
print('users who have similarities with Dpv in genre film: ', julcollab.most_similar_users('Dpv',2))

print('=====================================')
#Hybrid
print('+ Recommendation user jul with hybrid algorithm (minimumscore = 0.1):')
julhybrid = JulHybrid(film=df_hybrid2, dataset=dataset)
print(julhybrid.predict())

