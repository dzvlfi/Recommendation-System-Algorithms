import pandas as pd
from apyori import apriori
import os

#load data from dataset
os.chdir('..')
df = pd.read_csv(os.getcwd() + '/Dataset/apriori-dataset.csv')
#drop timestamp column
df = df.drop(columns=['Timestamp','Name'])

rows_count = df.shape[0]
columns_count = df.shape[1]

records = []
for i in range(rows_count):
    records.append([str(df.values[i,j]) for j in range(columns_count)])

association_rules = apriori(records, min_support=0.1, min_confidence=1, min_lift=1, min_length=1)
association_results = list(association_rules)

for item in association_results:
	# first index of the inner list
	# Contains base item and add item
    pair = item[0] 
    items1 = [x for x in pair]

    if len(items1) == 2:
        print("Rule: " + items1[0] + " -> " + items1[1])
    elif len(items1) == 3:
        print("Rule: " + items1[0] + " -> " + items1[1] + " -> " + items1[2])
	#print("Rule: " + items[0] + " -> " + items[1])

	#second index of the inner list
    print("Support: " + str(item[1]))

	#third index of the list located at 0th
	#of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")