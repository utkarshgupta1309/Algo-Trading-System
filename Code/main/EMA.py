# Using Pandas to calculate a 100-days span EMA. adjust=False specifies that we are interested in the recursive calculation mode.
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
df = pd.read_csv('RELIANCE.csv',parse_dates = True, index_col= 0)
df['100ma'] = df['Adj Close'].rolling(window = 100).mean()
df.dropna(inplace = True)
#============Formula To calculate EMA========================
days = int(input("Enter number of days."))
df['EMA'] = df['Adj Close'].ewm(span= days, adjust=False).mean()
df.dropna(inplace = True)
#==============================================================
axis1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
axis2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex =axis1)
axis1.plot(df.index, df['Adj Close'])
axis1.plot(df.index, df['Close'])
axis1.plot(df.index, df['EMA'],color = 'red')
axis1.plot(df.index, df['100ma'],color = 'blue')
axis2.bar(df.index, df['Volume'])
plt.legend()
plt.show()
