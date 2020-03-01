# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:27:53 2019

@author: Thuuri
"""

def get_12_rolling(stock, start, end):

    # paketit
    from pandas_datareader import data as pdr
    import yfinance as yf
    import matplotlib.pyplot as plt
    import seaborn as sns
    from datetime import datetime
    
    # tama paiva
    
    now = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
    
    # seaborn tyyli
    sns.set_style('whitegrid')
    
    # fix
    yf.pdr_override()
    
    # osake
    # stock = 'OUT1V.HE'
    
    # data
    data = pdr.get_data_yahoo(stock, start=start, end=end)
    
    # valitaan sulkuhinta ja voluumi
    df_focus = data[['Close', 'Volume']]
    
    # muunnetaan paivadata kuukaudeksi - keskiarvo
    df_month = df_focus.resample('M').mean()
    
    # lasketaan rullaavat 12kk keskiarvot
    df_rolling_12 = df_month.rolling(window = 12).mean()
    
    # tehdaan kuvaaja
    plt.plot(df_focus.Close)
    plt.plot(df_rolling_12.Close)
    plt.title(stock + ' data 12m moving avg, ' + now)
    plt.xticks(rotation = 45)
    plt.show()
