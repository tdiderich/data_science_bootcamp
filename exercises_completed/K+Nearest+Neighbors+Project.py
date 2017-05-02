
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # K Nearest Neighbors Project 
# 
# Welcome to the KNN Project! This will be a simple project very similar to the lecture, except you'll be given another data set. Go ahead and just follow the directions below.
# ## Import Libraries
# **Import pandas,seaborn, and the usual libraries.**

# In[10]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
get_ipython().magic(u'matplotlib inline')


# ## Get the Data
# ** Read the 'KNN_Project_Data csv file into a dataframe **

# In[7]:

data = pd.read_csv('KNN_Project_Data')


# **Check the head of the dataframe.**

# In[8]:

data.head()


# # EDA
# 
# Since this data is artificial, we'll just do a large pairplot with seaborn.
# 
# **Use seaborn on the dataframe to create a pairplot with the hue indicated by the TARGET CLASS column.**

# In[11]:

sns.pairplot(data)


# # Standardize the Variables
# 
# Time to standardize the variables.
# 
# ** Import StandardScaler from Scikit learn.**

# In[12]:

#done at top


# ** Create a StandardScaler() object called scaler.**

# In[13]:

scaler = StandardScaler()


# ** Fit scaler to the features.**

# In[14]:

data_features = data.drop('TARGET CLASS', axis=1)
scaler.fit(data_features)


# **Use the .transform() method to transform the features to a scaled version.**

# In[17]:

scaled_features = scaler.transform(data.drop('TARGET CLASS', axis=1))


# **Convert the scaled features to a dataframe and check the head of this dataframe to make sure the scaling worked.**

# In[20]:

data_feat = pd.DataFrame(scaled_features, columns=data.columns[0:-1])
data_feat.head()


# # Train Test Split
# 
# **Use train_test_split to split your data into a training set and a testing set.**

# In[27]:

x = data_feat
y = data['TARGET CLASS']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)


# In[11]:




# # Using KNN
# 
# **Import KNeighborsClassifier from scikit learn.**

# In[28]:

# done at top


# **Create a KNN model instance with n_neighbors=1**

# In[30]:

knn = KNeighborsClassifier(n_neighbors=1)


# **Fit this KNN model to the training data.**

# In[36]:

knn.fit(x_train, y_train)


# # Predictions and Evaluations
# Let's evaluate our KNN model!

# **Use the predict method to predict values using your KNN model and X_test.**

# In[37]:

pred = knn.predict(x_test)


# ** Create a confusion matrix and classification report.**

# In[38]:

confusion_matrix(y_test, pred)


# In[39]:

classification_report(y_test, pred)


# In[18]:




# # Choosing a K Value
# Let's go ahead and use the elbow method to pick a good K Value!
# 
# ** Create a for loop that trains various KNN models with different k values, then keep track of the error_rate for each of these models with a list. Refer to the lecture if you are confused on this step.**

# In[41]:

err = []
for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train, y_train)
    pred_i = knn.predict(x_test)
    err.append(np.mean(pred_i != y_test))


# **Now create the following plot using the information from your for loop.**

# In[42]:

plt.figure(figsize=(10,6))
plt.plot(range(1,40), err, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)


# ## Retrain with new K Value
# 
# **Retrain your model with the best K value (up to you to decide what you want) and re-do the classification report and the confusion matrix.**

# In[48]:

knn = KNeighborsClassifier(n_neighbors=21)
knn.fit(x_train, y_train)
pred_21 = knn.predict(x_test)
confusion_matrix(y_test, pred_21)
classification_report(y_test, pred_21)


# # Great Job!
