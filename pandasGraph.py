import pandas as pd 
import datetime
import pandas.io.data 
import matplotlib.pyplot as plt 

rows_list=[] 
df=pd.read_csv('./file1.csv' ,header=None,parse_dates=True,prefix='column')

for row in df.iterrows():
    if row[1][1]=='Beweging in de living':
        if row[1][2]=='OPEN': rows_list.append([row[1][0],'1'])
    else: rows_list.append([row[1][0],'0'])
df2 = pd.DataFrame(rows_list)
df3=df2.set_index(0)
print df3 
plt.plot(df3)
plt.show()
