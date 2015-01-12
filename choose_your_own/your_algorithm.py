#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

def trainTestAccuracy(name, clf):
    clf.fit(features_train, labels_train)
    accuracy = clf.score(features_test, labels_test)
    print "Accuracy of %s is %f " %(name, accuracy)

    

#testing Naive Bayes
from sklearn.naive_bayes import GaussianNB
clfNB = GaussianNB()
trainTestAccuracy('Naive Bayes', clfNB)

#testing SVM
from sklearn.svm import SVC
clfSVC = SVC() 
trainTestAccuracy('SVM', clfSVC)   


# testing the KNN 
from sklearn.neighbors import KNeighborsClassifier
clfKNN = KNeighborsClassifier(n_neighbors=1)
trainTestAccuracy('KNN', clfKNN) 

#testing the adaboost algo
from sklearn.ensemble import AdaBoostClassifier
clfAdaBoost = AdaBoostClassifier()
trainTestAccuracy('AdaBoost', clfAdaBoost) 

#testing Random forest algo
from sklearn.ensemble import RandomForestClassifier
clfRandForest = RandomForestClassifier()
trainTestAccuracy('Random Forest', clfRandForest) 


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
