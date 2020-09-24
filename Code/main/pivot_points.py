import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
df = pd.read_csv('RELIANCE.csv',parse_dates = True, index_col= 0,)
def ppsr(df):
    """Calculate Pivot Points, Supports and Resistances for given data

    :param df: pandas.DataFrame
    :return: pandas.DataFrame
    """
    PP = pd.Series((df['High'] + df['Low'] + df['Close']) / 3)
    R1 = pd.Series(2 * PP - df['Low'])
    S1 = pd.Series(2 * PP - df['High'])
    R2 = pd.Series(PP + df['High'] - df['Low'])
    S2 = pd.Series(PP - df['High'] + df['Low'])
    R3 = pd.Series(df['High'] + 2 * (PP - df['Low']))
    S3 = pd.Series(df['Low'] - 2 * (df['High'] - PP))
    psr = {'PP': PP, 'R1': R1, 'S1': S1, 'R2': R2, 'S2': S2, 'R3': R3, 'S3': S3}
    PSR = pd.DataFrame(psr)
    df = df.join(PSR)
    return df

df = ppsr(df)
print(df)
axis1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
axis2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex =axis1)

axis1.plot(df.index.month, df['PP'],color = 'black')
axis1.plot(df.index.month, df['R1'],color = 'red')
axis1.plot(df.index.month, df['S1'],color = 'green')
axis1.plot(df.index.month, df['R2'],color = 'blue')
axis1.plot(df.index.month, df['S2'],color = 'pink')
axis1.plot(df.index.month, df['R3'],color = 'yellow')
axis1.plot(df.index.month, df['S3'],color = 'brown')
axis2.bar(df.index.month, df['Volume'])
plt.legend()
plt.show()
