import pandas as pd
import numpy as np
from plotly import __version__
import cufflinks as cf
from plotly.offline import *
from plotly.graph_objs import *

cf.go_offline()

###*** DATA VIZ IN PLOTLY AND CUFFLINKS

### get DATA
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})

### plotly plots
df.iplot(kind='scatter',x='A',y='B')
