import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import datetime
import pandas_datareader.data as web
style.use('ggplot')

start = datetime.datetime(2019, 1, 1)
end = datetime.datetime.now()

df = pd.read_csv('RELIANCE.csv',parse_dates = True, index_col= 0)

#=====Calculate open high low close(ohlc)=========
#===This is done for adjusted close that means ======
#==stock which have been split can also be evaluated===
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()
#====This resapmled data at 10days=====
df_ohlc.reset_index(inplace = True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

# print(df_ohlc.head())

axis1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
axis1.xaxis_date()
axis2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex =axis1)

candlestick_ohlc(axis1,df_ohlc.values,width =2,colorup = 'g')
axis2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)

plt.show()
