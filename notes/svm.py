import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# get data
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
cancer.keys()

df_feat = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])

# train/test/split
from sklearn.model_selection import train_test_split

X = df_feat
y = cancer['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# section vector model
from sklearn.svm import SVC

model = SVC()
model.fit(X_train, y_train)

predicitions = model.predict(X_Test)

# test results
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, pred_dtree))
print(classification_report(y_test, pred_dtree))

# get better results by finding best parameters
from sklearn.model_selection import GridSearchCV

param_grid = {'C':[0.1, 1, 10, 100, 1000], 'gamma':[1, 0.1, 0.01, 0.001, 0.0001]}
grid = GridSearchCV(SVC(), param_grid, verbose=3)
print(grid.best_params_)
print(grid.best_estimator_)

# adapt model after grid search
grid_pred = grid.pred(X_test)
print(confusion_matrix(y_test, grid_pred))
print(classification_report(y_test, grid_pred))
