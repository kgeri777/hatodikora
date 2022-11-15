import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_risk_free_rate():
    df = pd.read_csv('DTB3.csv')
    df.index = pd.to_datetime(df['DATE'])
    df = df[['DTB3']]
    df.columns = ['risk_free']
    msk = df['risk_free']!='.'
    df = df[msk]
    df=df.astype(float)
    df=df/252
    return df
df = get_risk_free_rate()
print(df)


# filename = 'BRK-B.csv'
# df = pd.read_csv(filename)
# df['ret_log'] = np.log(df['Adj Close']/df['Adj Close'].shift(1))
# df.index=pd.to_datetime(df['Date'])
# t_day_in_year = 252
# vol_windows_in_y = [0.25, 1, 3, 10]
# cols=[]
# for year in vol_windows_in_y:
    # col = 'vol_rolling_' + str(year) + 'y'
    # cols.append(col)
    # df[col] = np.sqrt(252) * df['ret_log'].rolling(int(year*t_day_in_year)).std()
    # df['avg_return_' + str(year) + 'y'] = 252 * df['ret_log'].rolling(int(year*t_day_in_year)).mean()
# df['vol_rolling_1y'] = df['ret_log'].rolling(252).std()
# df['vol_rolling_2y'] = df['ret_log'].rolling(504).std()
# df[['vol_rolling_1y','vol_rolling_2y']].plot()
# plt.show()

# df['avg_return_1y'].plot()
# plt.show()
