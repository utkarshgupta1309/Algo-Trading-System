import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import pandas_datareader.data as web
style.use('ggplot')

start = datetime.datetime(2019, 1, 1)
end = datetime.datetime.now()

#======Code to download data============
df = web.DataReader("RELIANCE.NS", 'yahoo', start, end)
RELIANCE = df.to_csv('RELIANCE.csv')
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
#======================================

df = pd.read_csv('RELIANCE.csv',parse_dates = True, index_col= 0)
print(df)



#=================100 day moving average================
df['100ma'] = df['Adj Close'].rolling(window = 100).mean()
#print(df.tail())
df.dropna(inplace = True)
#========================================================


axis1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
axis2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex =axis1)
axis1.plot(df.index, df['Adj Close'])
axis1.plot(df.index, df['Close'])
axis1.plot(df.index, df['100ma'],color = 'red')
axis2.bar(df.index, df['Volume'])
plt.legend()
plt.show()
