import seaborn as sns
import matplotlib.pyplot as plt

###*** practice matrix plots

### pre-loaded datasets
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

### correlations with tips, make heatmap

# tc = tips.corr()
# heat = sns.heatmap(tc,annot=True,cmap='coolwarm')

### matrix heat map with flights

piv = flights.pivot_table(index='month',columns='year',values='passengers')

# pivheat = sns.heatmap(piv,cmap='magma',linecolor='white',linewidth=1)

### CLUSTER PLOTS

# clust = sns.clustermap(piv,cmap='coolwarm')

###*** REGRESSION PLOTS

### reg plot
# reg = sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'])
# reg2 = sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time')

####*** GRIDS SECTION - customize instead of standard pairplot
iris = sns.load_dataset('iris')

# grid = sns.PairGrid(iris)
# grid.map_diag(sns.distplot)
# grid.map_upper(plt.scatter)
# grid.map_lower(sns.kdeplot)

# g2 = sns.FacetGrid(data=tips,col='time',row='smoker')
# g2.map(sns.distplot,'total_bill')

sns.plt.show()
