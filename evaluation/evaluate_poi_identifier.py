#!/usr/bin/python


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
### it's all yours from here forward!  
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features, labels)  # train and test on entire set
score = clf.score(features, labels)

print "Score on full data is %f" %score

## now we do train/test split
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
score = clf.score(features_test, labels_test)
print "Score on test data is %f" %score

# number of poi's predicted on test set
predLabels = clf.predict(features_test)
numPoi = sum(predLabels)
print "num. of pois predicted in test set is %d" %numPoi
numTest = len(features_test)
print "num of people in test set is %d" %numTest

# if it predicted all zero
numActualPoi = sum(labels_test)
acc = (numTest - numActualPoi)/float(numTest)
print "Accuracy if it predicted all to be 0 is %f" %acc

#any true positives?
predPOILocs = np.argwhere(predLabels == 1)
truePOILocs = np.argwhere(np.array(labels_test) == 1)

#compute precision adn recall
from sklearn.metrics import precision_score, recall_score
precScore = precision_score(labels_test, predLabels)
recScore = recall_score(labels_test, predLabels)
print "Precision: %f, Recall%f" %(precScore, recScore)