import pandas as pd
import sys
import os

os.chdir('Code')#change dir to Code folder for geting a Classes in that directory
dir = os.getcwd()
sys.path.insert(0, dir)
from apriori_algorithm import JulApriori
from content_algorithm import JulContentBased
from hybrid_algorithm import JulHybrid
from collaborative_algorithm import JulCollaborative
from ab_testing import JulABTesting

os.chdir('../Dataset')#change dir to Dataset folder for geting a dataset in that directory
dir = os.getcwd()
sys.path.insert(0, dir) #set work directory to folder dataset to import dataset with *.py extension
from recommendation_data import dataset #import some dataset with a dictionary type

df_abtesting = pd.read_csv('ab_data.csv').drop(columns='timestamp')
df_hybrid2 = pd.read_csv('data_content.csv',delimiter=';') #dataset of film to process an hybrid algorithm
df_apriori = pd.read_csv('apriori_dataset.csv').drop(columns=['Timestamp','Name'])
df_content = pd.read_csv('cont_dataset.csv')

#Collaborative, user based
print('+ Asosiasi barang dengan algoritma apriori: ')
julori = JulApriori()
julori.fit(df_apriori)
julori.result()

#Content based
print('+ Rekomendasi Content Based berdasarkan film Avenger: ')
julcontent = JulContentBased(df_content)
print(julcontent.predict('Avenger'))

print('=====================================')
#Collaborative
print('+ Collaborative Filtering: ')
julcollab = JulCollaborative(dataset)
recommendation, score = julcollab.user_recommendations('Dpv')
print('Rekomendasi dari pengguna untuk Dpv dengan skor masing-masing: ', score)
print('Korelasi pengguna antar Dpv and Star (kemiripan film): ', julcollab.person_correlation('Dpv', 'Star'))
print('Kesamaan pengguna dengan Dpv (2 pengguna): ', julcollab.most_similar_users('Dpv',2))

print('=====================================')
#Hybrid
print('+ Rekomendasi untuk pengguna jul dengan hybrid algorithm (minimumscore = 0.1):')
julhybrid = JulHybrid(film=df_hybrid2, dataset=dataset)
print(julhybrid.predict())

print('=====================================')
#A/B Testing
print('+ A/B Testing yang digunakan pada halaman website:')
julab = JulABTesting(0.05)
julab.fit(df_abtesting)
julab.predict()