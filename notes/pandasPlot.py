import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df1_file = '/Users/tylerdiderich/Desktop/python_bootcamp/Python-for-Data-Visualization/Pandas-Built-in-Data-Viz/df1'
df2_file = '/Users/tylerdiderich/Desktop/python_bootcamp/Python-for-Data-Visualization/Pandas-Built-in-Data-Viz/df2'
df3_file = '/Users/tylerdiderich/Desktop/python_bootcamp/Python-for-Data-Visualization/Pandas-Built-in-Data-Viz/df3'

df1 = pd.read_csv(df1_file,index_col=0)
df2 = pd.read_csv(df2_file,index_col=0)
df3 = pd.read_csv(df3_file,index_col=0)

###*** DATA VIZ IN PANDAS
### all matplot lib args can be added to pandas plots

### histogram
# hist = df1['A'].plot.hist()

### area (has stacked option)
# area = df1['A'].plot.area(stacked=True)

### line plot
# line = df1.plot.line(x=df1.index,y='B')

### scatter
# scat = df1.plot.scatter(x='A',y='B',s=df1['C']*100)

### box plots
# box = df1.plot.box()

### hex plot
# hex = df1.plot.hexbin(x='a',y='b',gridsize=25)

### kernel density
# kde = df1.plot.density()
