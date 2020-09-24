import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
df = pd.read_csv('RELIANCE.csv',parse_dates = True, index_col= 0)
def macd(df, n_fast, n_slow):
    """Calculate MACD, MACD Signal and MACD difference

    :param df: pandas.DataFrame
    :param n_fast:
    :param n_slow:
    :return: pandas.DataFrame
    """
    EMAfast = pd.Series(df['Close'].ewm(span=n_fast, min_periods=n_slow).mean())
    EMAslow = pd.Series(df['Close'].ewm(span=n_slow, min_periods=n_slow).mean())
    MACD = pd.Series(EMAfast - EMAslow, name='MACD')
    MACDsign = pd.Series(MACD.ewm(span=9, min_periods=9).mean(), name='MACDsign')
    MACDdiff = pd.Series(MACD - MACDsign, name='MACDdiff')
    df = df.join(MACD)
    df = df.join(MACDsign)
    df = df.join(MACDdiff)
    return df
#==============================================================
df = macd(df,12,26)
print(df)
axis1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
axis2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex =axis1)
axis1.plot(df.index, df['Adj Close'])
axis1.plot(df.index, df['Close'])
axis2.plot(df.index, df['MACD'],color = 'red')
axis2.plot(df.index, df['MACDsign'],color = 'yellow')
axis2.plot(df.index, df['MACDdiff'],color = 'green')
plt.legend()
plt.show()
