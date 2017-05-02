###***learning seaborn lib

import seaborn as sns

# tips is a pre-loaded dataset
tips = sns.load_dataset('tips')

### visualize a distribution
# distplot = sns.distplot(tips['total_bill'],kde=False,bins=30)

### joint plot is scatter plot comparing two columns of data
# jointplot = sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')

###pair plot compares all values
# pairplot = sns.pairplot(tips,hue='sex',palette='coolwarm')

###rug plots like a vertical histogram
# rug = sns.rugplot(tips['total_bill'])

### learning about the normal distribution

### import stuff
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

### create dataset of 25 random numbers
dataset = np.random.randn(25)

###rug plot of the numbers
sns.rugplot(dataset)

### get min/max
x_min = dataset.min() - 2
x_max = dataset.max() + 2

### array with 100 equally spread points
x_axis = np.linspace(x_min,x_max,100)

### random url set bandwidth var
url = 'https://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'
bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**0.2

### empty Kernel
kernel_list = []

### loop through list to add data points to dataset
### use stats lib to create normal distributions
for data_points in dataset:
    kernel = stats.norm(data_points,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color='grey',alpha=0.5)


plt.ylim(0,1)

### sum array / use matplotlib to graph normal distributions
sum_of_kde = np.sum(kernel_list,axis=0)
fig = plt.plot(x_axis,sum_of_kde,color='indianred')
sns.rugplot(dataset,c='indianred')
plt.yticks([])
plt.suptitle('Sum of the Basis Functions')

plt.show()
sns.plt.show()
