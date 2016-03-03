import sys
from time import time
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

#Load training and testing data
X = pd.read_csv("X_whole.csv")
y = pd.read_csv("y_whole.csv").pop('SLIDE')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

#Define Model
clf = RandomForestClassifier(n_estimators=1000)

#Fit Data to Model
t0 = time()
clf.fit(X_train, y_train)
print ("Training time:", round(time() - t0, 3), "s")

#Predict on test set
t1 = time()
pred = clf.predict(X_test)
print ("predicting time:", round(time() - t1, 3), "s")

#Compare prediction to test labels
print(accuracy_score(pred, y_test))

importances = clf.feature_importances_
std = np.std([tree.feature_importances_ for tree in clf.estimators_],axis=0)
indices = np.argsort(importances)[::-1]

print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()
