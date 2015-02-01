#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

#remove the TOTAL outlier key
#remove this key
data_dict.pop('TOTAL', 0)

data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# find the person who's salary >2e7
#for key in data_dict:
#    #print key
#    person = data_dict[key]
#    salary = person['salary']
#    if salary != 'NaN':
#        if salary > 2e7:
#            print key

#find the people that made a bonus > 6mil and salary over million
for person in data_dict:
    salary = data_dict[person]['salary']
    bonus = data_dict[person]['bonus']
    if salary != "NaN" and bonus != "NaN":
        if (salary > 1e6) and (bonus >5e6):
            print ("Name: %s; Salary: %d, Bonus: %d") %(person, salary, bonus)

