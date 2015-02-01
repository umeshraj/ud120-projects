#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### the words (features) and authors (labels), already largely processed
#words_file = "word_data_overfit.pkl" ### like the file you made in the last mini-project 
#authors_file = "email_authors_overfit.pkl"  ### this too
words_file = "../text_learning/your_word_data.pkl" ### like the file you made in the last mini-project 
authors_file = "../text_learning/your_email_authors.pkl"  ### this too

word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (remainder go into training)
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train).toarray()
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150]
labels_train   = labels_train[:150]



### your code goes here
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
trainScore = clf.score(features_train, labels_train)
print "Training score is %f" %trainScore

# important features and nmber of feature
featImp = clf.feature_importances_
import numpy as np
idx = np.argsort(featImp)  # sort and pick the largest value
largestIdx = idx[-1]
print "feature number %d, feature value: %f " %(largestIdx, featImp[largestIdx])

## get the feature name that is best discriminating the two emails
featureNames = vectorizer.get_feature_names()
maxDiscrimName = featureNames[largestIdx]
print "the most discriminative word is %s" %maxDiscrimName

#number of words with importance > 0.2
numImp = sum(featImp >0.2)
print "Num. words with importance > 0.2 is %d" %numImp

#accuracy of the decisions tree
testScore = clf.score(features_test, labels_test)
print "Test score is %f" %testScore