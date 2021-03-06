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

# finding the number of people in the dataset
numRows = len(enron_data)

# how many features for each person
allKeys = enron_data.keys()
numFeatues = len(enron_data[allKeys[1]])

# how many pois are there?
numPOI = 0
for value in enron_data.values():
    if value['poi'] is True:
        numPOI += 1
print "The number of POIs is %d" %numPOI

# find the number of poi names from the ../final_project/poi_names.txt file
numPOI = 0
poiFileName = "../final_project/poi_names.txt"
with open(poiFileName) as f:
    for line in f:
        if "(y)" in line or "(n)" in line:
            numPOI += 1
print "Number of POIs from poi_names.txt is %d" %numPOI

# total value of stock for James Prentice
personName = "PRENTICE JAMES"
personTotalStockValue = enron_data[personName]["total_stock_value"]
print "The total stock value for %s was %f" %(personName, personTotalStockValue)

# number of emails to poi from Wesley Colwell
personName = 'COLWELL WESLEY'
featureName = "from_this_person_to_poi"
featureVal = enron_data[personName][featureName]
print "The %s for %s was %d" %(featureName, personName, featureVal)

# value of stock options exercised by Jeffrey Skilling
personName = "SKILLING JEFFREY K"
featureName = "exercised_stock_options"
featureVal = enron_data[personName][featureName]
print "The %s for %s was %d" %(featureName, personName, featureVal)

# who took home the most money
personNameList = ["SKILLING JEFFREY K", "LAY KENNETH L", "FASTOW ANDREW S"]
featureName = "total_payments"
for person in personNameList:
    featureVal = enron_data[person][featureName]
    print "%s took home %d" %(person, featureVal)

# how many people have a quantified salary
print "\n\n"
featureName = "salary"
numWithSalary = 0
numWithEmail = 0
for person in enron_data.values():
    salary = person["salary"]
    emailAddress = person["email_address"]
    if salary != 'NaN':
        numWithSalary+=1
    if emailAddress != "NaN":
        numWithEmail += 1
    print "%s %s %d %d" %(salary, emailAddress, numWithSalary, numWithEmail)
print  "There are %d people with quantified salary" %numWithSalary
print  "There are %d people with known email" %numWithEmail

#number of people with nan for total_payments
numNanTotalPayments = 0
for person in enron_data.values():
    if person["total_payments"] == 'NaN':
        numNanTotalPayments += 1
numPeople = len(enron_data)
nanPercent = float(numNanTotalPayments)/numPeople * 100
print "%d of %d (or %f%%) have 'NaN' for total_payments" %(numNanTotalPayments, numPeople, nanPercent)

# number of POIs with nan for total payment
numPOINanTotalPayments = 0
numPOI = 0
for person in enron_data.values():
    if (person["poi"] == True):  # count number of POIs
        numPOI += 1        
        if person["total_payments"]=="NaN":  # number of POI+NanTotalPayment
            numPOINanTotalPayments += 1
poiNanPercent = float(numPOINanTotalPayments)/numPOI * 100
print "%d of %d (or %f%%) POIs have NaN for total payments" %(numPOINanTotalPayments, numPOI, nanPercent)
        
# adding 10 Nans all of which are POIs 
newNumPeople = numPeople + 10
newNumPOI = numPOI + 10
#print "now %d/%d of people had Nan. %d/%d POIs have nan" %(numPOI)