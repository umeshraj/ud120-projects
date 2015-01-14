#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#finding the number of people in the dataset
numRows = len(enron_data)

#how many features for each person
allKeys = enron_data.keys()
numFeatues = len(enron_data[allKeys[1]])

#how many pois are there?
numPOI = 0
for key in enron_data.keys():
    if enron_data[key]['poi'] is True:
        numPOI +=1
print "The number of POIs is %d" %numPOI
        