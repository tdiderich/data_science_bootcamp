import pandas as pd
import numpy as np
import natplotlib.pyplot as plt
import seaborn as sns
from sklean.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklean.metrics import classification_report, confusion_matrix
from sklearn.cross_validation import train_test_split

# get data
df = pd.read_csv('Classified Data', index_col=0)

#set scaler and set data up for analysis
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))
df_feat = pd.DataFrame(scaled_features, columns=df.columns[0:-1])

# split for train/test
X = df_feat
y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# create mocdel and predicitions
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
pred = knn.predict(x_test)

# test results
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

# test various kneighbor values 1-40
error_rate = []

for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

# test results
plt.figure(figsize=(10,6))
plt.plot(range(1,40), error_rate, color='blue', linestyle='dashed', marker='o',
        markerfacecolor='red', markersize=10)
plt.title('')
