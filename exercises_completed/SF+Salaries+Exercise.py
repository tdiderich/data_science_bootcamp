
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[1]:

import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[2]:

sal = pd.read_csv('Salaries.csv')


# ** Check the head of the DataFrame. **

# In[3]:

sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[4]:

sal.info()


# **What is the average BasePay ?**

# In[5]:

sal['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[6]:

sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[9]:

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[12]:

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# In[13]:

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**

# In[19]:

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[20]:

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[23]:

sal.groupby(['Year']).mean()['BasePay']


# In[24]:

sal.groupby(['Year']).mean()['BasePay']


# In[ ]:




# ** How many unique job titles are there? **

# In[25]:

sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[27]:

sal['JobTitle'].value_counts()[0:5]


# In[28]:

sal['JobTitle'].value_counts()[0:5]


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[51]:

sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[68]:

sal[sal['JobTitle'].str.contains('Chief')].count()[0]


# In[21]:




# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[76]:

sal['title_len'] = len(sal['JobTitle'])
sal[['title_len','TotalPayBenefits']].corr()


# In[78]:

sal['title_len'].corr(sal['TotalPayBenefits'])


# # Great Job!
