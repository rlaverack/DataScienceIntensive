import sys
from time import time
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

xgboost_params = {
   "objective": "binary:logistic",
   "booster": "gbtree",
   "eval_metric": "auc",
   "eta": 0.01, # 0.06, #0.01,
   #"min_child_weight": 240,
   "subsample": 0.75,
   "colsample_bytree": 0.68,
   "max_depth": 7
}

#Load training and testing data
X = pd.read_csv("X_whole.csv")
y = pd.read_csv("y_whole.csv").pop('SLIDE')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

xgtrain = xgb.DMatrix(X_train.values, y_train.values)
xgtest = xgb.DMatrix(X_test.values)

print('Fit the model...')
boost_round = 5 #1800 CHANGE THIS BEFORE START
clf = xgb.train(xgboost_params,xgtrain,num_boost_round=boost_round,verbose_eval=True,maximize=False)

#Predict on test set
t1 = time()
print('Predict...')
pred = clf.predict(xgtest, ntree_limit=clf.best_iteration)
print ("predicting time:", round(time() - t1, 3), "s")

#Compare prediction to test labels
print(accuracy_score(pred, y_test))
