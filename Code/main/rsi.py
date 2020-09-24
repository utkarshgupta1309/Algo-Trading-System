import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
df = pd.read_csv('RELIANCE.csv',parse_dates = True, index_col= 0)
n= int(5)
def relative_strength_index(df, n):
    """Calculate Relative Strength Index(RSI) for given data.

    :param df: pandas.DataFrame
    :param n:
    :return: pandas.DataFrame
    """
    i = 0
    UpI = [0]
    DoI = [0]
    while i + 1 <= df.index[-``]:
        UpMove = df.loc[i + 1, 'High'] - df.loc[i, 'High']
        DoMove = df.loc[i, 'Low'] - df.loc[i + 1, 'Low']
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)
        i = i + 1
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    PosDI = pd.Series(UpI.ewm(span=n, min_periods=n).mean())
    NegDI = pd.Series(DoI.ewm(span=n, min_periods=n).mean())
    RSI = pd.Series(PosDI / (PosDI + NegDI))
    df = df.join(RSI)
    return df
#==============================================================
df = relative_strength_index(df,20)
axis1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
axis2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex =axis1)
axis1.plot(df.index, df['Adj Close'])
axis1.plot(df.index, df['Close'])
axis1.plot(df.index, df['RSI'],color = 'green')
axis2.bar(df.index, df['Volume'])
plt.legend()
plt.show()
