#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
CVal = 10000
clf = SVC(C=CVal, kernel='rbf') #make the classifier

#reducing the number of samples for speed
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100] 

#fit the classifier
clf.fit(features_train, labels_train) 
t0=time()
pred = clf.predict(features_test)
print "Training time", round(time()-t0,3), "s" 

accuracy = clf.score(features_test, labels_test)
print "The accuracy of this classifier is %f" %accuracy

idList = [10, 26, 50]
for id in idList:
    print "Prediction for %d element is %f" %(id, pred[id])

#number of emails predicted to be Chris
numChris = sum(pred == 1)
print "Number of emails predicted to be Chris(1.0) is %d" %numChris


#########################################################


