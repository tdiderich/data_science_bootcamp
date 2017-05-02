###*** categorical plots in seaborn
import seaborn as sns
import numpy as np

### load tips
tips = sns.load_dataset('tips')

### male/female total bills barplot
# barplot = sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std)

### count plot
# count = sns.countplot(x='sex',data=tips)

###box plot
# box = sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')

###violin plots, distributions on the side
# sns.violinplot(x='day',y='total_bill',data=tips,hue='smoker')

### strip plot
# sns.stripplot(x='day',y='total_bill',data=tips,jitter=True)

### swarm plot
# sns.swarmplot(x='day',y='total_bill',data=tips)

sns.plt.show()
