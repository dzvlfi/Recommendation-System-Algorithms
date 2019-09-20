import pandas as pd
from apriori_algorithm import JulApriori
from content_algorithm import JulContentBased
import os
os.chdir('..')

#Collaborative, user based
df_apriori = pd.read_csv(os.getcwd() + '/Dataset/apriori-dataset.csv')
df_apriori = df_apriori.drop(columns=['Timestamp','Name'])

julori = JulApriori()
julori.fit(df_apriori)
julori.result()

#Content based
df = pd.read_csv(os.getcwd() + '/Dataset/cont-dataset.csv')

julcontent = JulContentBased(df)
print('Recommendation by content based: ',julcontent.predict('Avenger'))