import pandas as pd
import numpy as np
from numpy.random import randn


###*** read/write to csv

# df.read_csv('pathtofile.csv')
# df.to_csv('pathtofile.csv')

# df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

# df.to_csv('~/Desktop/newFile.csv')

###*** web scraping from a link

#data = pd.read_html('http://www.espn.com/fantasy/football/story/_/id/16287927/2016-fantasy-football-rankings-top-300')
#df = pd.DataFrame(data[1])

###*** SQL & Pandas (better to use another lib for specific driver)

#from sqlalchemy import create_engine
#engine = create_engine('sqlite:///:memory:')
#df.to_sql('my_table',engine)
#sqldf = pd.read_sql('my_table',con=engine)
