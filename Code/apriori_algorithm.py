# -*- coding: utf-8 -*-
from apyori import apriori

class JulApriori(): 

    def __init__ (self,  support=0.1,  confidence=1, lift=1, length=1): 
        self.min_support = support 
        self.min_confidence = confidence
        self.min_lift = lift
        self.min_length = length

    def fit(self, data): 
        rows_count = data.shape[0]
        columns_count = data.shape[1]

        records = []
        for i in range(rows_count):
            records.append([str(data.values[i,j]) for j in range(columns_count)])

        self.association_rules = apriori(records, min_support=self.min_support, min_confidence=self.min_confidence, min_lift=self.min_lift, min_length=self.min_length)
        self.association_results = list(self.association_rules)

    def result(self):
        for item in self.association_results:
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
