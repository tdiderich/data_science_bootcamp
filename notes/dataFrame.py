import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

#indexing a data frame
col = df[['W','Z']]

#adding a column
df['new'] = randn(5,1)

#removing column (permanemt add inplace=True)
df.drop('W',axis=1)

#selecting rows
r = df.loc['A'] #key name
r2 = df.iloc[1] #numbered indexing

#select value in df
cell = df.loc['A','W']

#logical operators
booldf = df > 0

#condintional on single column
condw = df[df['W']>0]

#indexing columns based on condintional to get a series
condser = df[df['W']>0]['W']

#two conditions use (& not and), (| not or)
cond2 = df[(df['W']>0) & (df['new']>0)]

#changing index names
colnames = 'CA WI VA NY FL'.split()
df['States'] = colnames
df.set_index('States',inplace=True)

#new dataframe for multiindex levels
outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = (1,2,3,1,2,3)
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df2 = pd.DataFrame(randn(6,2),hier_index,['A','B'])
df2.index.names = ['Groups','Num']

#grabbing specific data points with multiple index levels (group index, row, col)
point = df2.loc['G1'].loc[2]['A']

#use .xs() method to get values from two different group indexes ex G1 & G2
g1g2 = df2.xs(1,level='Num')

#new dict + df for Groupby practice
data = {'Company':'GOOG GOOG MSFT MSFT FB FB'.split(),
        'Person':'Sam Charlie Amy Vanessa Carl Sarah'.split(),
        'Sales':[200,120,340,124,243,350]}
df3 = pd.DataFrame(data)

#group by company name + run method to get a data frame
byComp = df3.groupby('Company')
avg = byComp.mean()

#two dfs for .merge() practice
left = pd.DataFrame({'key1':'k0 k0 k1 k2'.split(),
                     'key2':'k0 k1 k0 k1'.split(),
                     'A':'a0 a1 a2 a3'.split(),
                     'B':'b0 b1 b2 b3'.split()})
right = pd.DataFrame({'key1':'k0 k1 k1 k2'.split(),
                     'key2':'k0 k0 k0 k0'.split(),
                     'C':'c0 c1 c2 c3'.split(),
                     'D':'d0 d1 d2 d3'.split()})

#merging left and right on key1/key2
merg = pd.merge(left,right,on=['key1','key2'])

#basic merge
merg1 = pd.merge(left,right)

#new dfs for join practice
left1 = pd.DataFrame({'C':'c0 c1 c2'.split(),
                     'D':'d0 d1 d2'.split()},
                     index=['k0','k1','k2'])
right1 = pd.DataFrame({'A':'a0 a1 a2'.split(),
                     'B':'b0 b1 b2'.split()},
                     index=['k0','k1','k2'])

#perfrom join df.joing(df1)

join = left1.join(right1)

#random operations to remember
df.unique() # gives uniques
df.nunique() # count of uniques
df.value_count() # gives all uniques
df.apply(#insert function here#) #run any function on
                                 #each element in the column
df.drop('col',axis=1) #drop column,
df.columns #array of columns
df.index #arrat of indexes
df.sort_values('col') #sort data by 'col'
df.isnull() #df of bools if null
df.pivot_table(values=,index=,columns=) #creates pivot table

print(join)
