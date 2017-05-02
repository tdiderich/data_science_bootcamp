import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


# get data and split for test/train
df = pd.read_csv('kyphosis.csv')
X = df.drop('Kyphosis', axis=1)
y = df['Kyphosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# decision tree classifier
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
pred_dtree = dtree.predict(X_test)
print(confusion_matrix(y_test, pred_dtree))
print(classification_report(y_test, pred_dtree))

# random forrests classifier
forest = RandomForrestClassifier(n_estimators=200)
forest.fit(X_train, y_train)
pred_forest = forest.predict(X_test)
print(confusion_matrix(y_test, pred_forest))
print(classification_report(y_test, pred_forest))
