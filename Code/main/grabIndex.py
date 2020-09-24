import bs4 as bs #webscrapping with beautifulSoup
import datetime as dt
import os
import pandas as pd
import pandas_datareader as web
import pickle
import requests

def save_sensex_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_BSE_SENSEX_companies')
    soup = bs.BeautifulSoup(resp.text)
    table = soup.find('table',{'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        tickers.append(ticker)
    with open("sensextickers.pickle","wb") as f:
        pickle.dump(tickers,f)
    print(tickers)
    return tickers

#save_sensex_tickers()

def get_data_from_yahoo(reload_sensex=False):
    if reload_sensex:
        tickers = save_sensex_tickers()
    else:
        with open("sensextickers.pickle","rb") as f:
            tickers = pickle.load(f)
        if not os.path.exists('stocks_dfs'):
            os.makedirs('stock_dfs')

    start = dt.datetime(2019,1,1)
    end = dt.datetime(2020,1,1)

    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker,'yahoo',start,end)
            df.to_csv('stock_dfs/{csv}'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()
