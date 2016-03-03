import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

#Load training and testing data
X = pd.read_csv('X.csv')
y = pd.read_csv('y.csv').pop('SLIDE')

#Define Model
model = LogisticRegression(multi_class = 'multinomial')
model = model.fit(X, y)

score = model.score(X, y)

print score
