
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Seaborn Exercises
# 
# Time to practice your new seaborn skills! Try to recreate the plots below (don't worry about color schemes, just the plot itself.

# ## The Data
# 
# We will be working with a famous titanic data set for these exercises. Later on in the Machine Learning section of the course, we will revisit this data, and use it to predict survival rates of passengers. For now, we'll just focus on the visualization of the data with seaborn:

# In[19]:

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[9]:

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
sns.set_style('whitegrid')


# In[28]:

titanic = sns.load_dataset('titanic')


# In[40]:

titanic.head()


# # Exercises
# 
# ** Recreate the plots below using the titanic dataframe. There are very few hints since most of the plots can be done with just one or two lines of code and a hint would basically give away the solution. Keep careful attention to the x and y labels for hints.**
# 
# ** *Note! In order to not lose the plot image, make sure you don't code in the cell that is directly above the plot, there is an extra cell above that one which won't overwrite that plot!* **

# In[10]:

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')
sns.jointplot(x='fare',y='age',data=titanic)


# In[41]:




# In[12]:

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')
sns.distplot(titanic['fare'],kde=False)


# In[44]:




# In[15]:

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')
sns.boxplot(x='class',y='age',data=titanic)


# In[45]:




# In[16]:

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')
sns.swarmplot(x='class',y='age',data=titanic)


# In[46]:




# In[18]:

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')
sns.countplot(x='sex',data=titanic)


# In[47]:




# In[19]:

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')
tit = titanic.corr()
sns.heatmap(tit)


# In[48]:




# In[37]:

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
titanic = sns.load_dataset('titanic')
g = sns.FacetGrid(data=titanic,col='sex')
g.map(sns.distplot,'age',kde=False)


# In[49]:




# # Great Job!
# 
# ### That is it for now! We'll see a lot more of seaborn practice problems in the machine learning section!
