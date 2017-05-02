
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Logistic Regression Project 
# 
# In this project we will be working with a fake advertising data set, indicating whether or not a particular internet user clicked on an Advertisement. We will try to create a model that will predict whether or not they will click on an ad based off the features of that user.
# 
# This data set contains the following features:
# 
# * 'Daily Time Spent on Site': consumer time on site in minutes
# * 'Age': cutomer age in years
# * 'Area Income': Avg. Income of geographical area of consumer
# * 'Daily Internet Usage': Avg. minutes a day consumer is on the internet
# * 'Ad Topic Line': Headline of the advertisement
# * 'City': City of consumer
# * 'Male': Whether or not consumer was male
# * 'Country': Country of consumer
# * 'Timestamp': Time at which consumer clicked on Ad or closed window
# * 'Clicked on Ad': 0 or 1 indicated clicking on Ad
# 
# ## Import Libraries
# 
# **Import a few libraries you think you'll need (Or just import them as you go along!)**

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# ## Get the Data
# **Read in the advertising.csv file and set it to a data frame called ad_data.**

# In[2]:

ads = pd.read_csv('advertising.csv')


# **Check the head of ad_data**

# In[3]:

ads.head()


# ** Use info and describe() on ad_data**

# In[4]:

ads.info()


# In[5]:

ads.describe()


# ## Exploratory Data Analysis
# 
# Let's use seaborn to explore the data!
# 
# Try recreating the plots shown below!
# 
# ** Create a histogram of the Age**

# In[8]:

ads['Age'].plot.hist(bins=30)


# In[48]:




# **Create a jointplot showing Area Income versus Age.**

# In[9]:

sns.jointplot(x='Age',y='Area Income',data=ads)


# In[64]:




# **Create a jointplot showing the kde distributions of Daily Time spent on site vs. Age.**

# In[12]:

sns.jointplot(x='Age',y='Daily Time Spent on Site',data=ads,kind='kde',color='r')


# In[66]:




# ** Create a jointplot of 'Daily Time Spent on Site' vs. 'Daily Internet Usage'**

# In[14]:

sns.jointplot(x='Daily Internet Usage',y='Daily Time Spent on Site',data=ads,color='g')


# In[72]:




# ** Finally, create a pairplot with the hue defined by the 'Clicked on Ad' column feature.**

# In[20]:

sns.pairplot(ads,hue='Clicked on Ad')


# In[84]:




# # Logistic Regression
# 
# Now it's time to do a train test split, and train our model!
# 
# You'll have the freedom here to choose columns that you want to train on!

# ** Split the data into training set and testing set using train_test_split**

# In[29]:

ads.corr()


# In[33]:

X = ads[['Age','Male','Daily Time Spent on Site']]
y = ads['Clicked on Ad']


# In[32]:

from sklearn.model_selection import train_test_split


# In[34]:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)


# ** Train and fit a logistic regression model on the training set.**

# In[36]:

from sklearn.linear_model import LogisticRegression


# In[41]:

model = LogisticRegression()
model.fit(X_train, y_train)


# ## Predictions and Evaluations
# ** Now predict values for the testing data.**

# In[44]:

guesswho = model.predict(X_test)


# In[45]:




# ** Create a classification report for the model.**

# In[46]:

from sklearn.metrics import classification_report


# In[48]:

classification_report(y_test, guesswho)


# ## Great Job!
