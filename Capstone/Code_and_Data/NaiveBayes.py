import sys
from time import time
from collections import Counter
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#Load training and testing data
features_train = pd.read_csv('X.csv')
features_test = pd.read_csv('X_test.csv')
labels_train = pd.read_csv('y.csv').pop('SLIDE')
labels_test = pd.read_csv('y_test.csv').pop('SLIDE')

#Define Model
clf = GaussianNB()

#Fit Data to Model
t0 = time()
clf.fit(features_train, labels_train)
print ("Training time:", round(time() - t0, 3), "s")

#Predict on test set
t1 = time()
pred = clf.predict(features_test)
print ("predicting time:", round(time() - t1, 3), "s")

#Compare prediction to test labels
print(accuracy_score(pred, labels_test))
