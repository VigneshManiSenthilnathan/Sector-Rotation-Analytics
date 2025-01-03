import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import yfinance as yf
from textblob import TextBlob
import requests
from datetime import datetime, timedelta
from fredapi import Fred

import yaml
with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    fred_api_key = config['FRED_API_KEY']

fred = Fred(api_key=fred_api_key)

class DataCollector:
    def __init__(self):
        self.sector_etfs = {
            'XLE': 'Energy',
            'XLF': 'Financials',
            'XLK': 'Technology',
            'XLV': 'Healthcare',
            'XLI': 'Industrials',
            'XLP': 'Consumer Staples',
            'XLY': 'Consumer Discretionary',
            'XLB': 'Materials',
            'XLU': 'Utilities',
            'XLRE': 'Real Estate'
        }
    
    def get_sector_data(self, start_date, end_date):
        sector_data = pd.DataFrame()
        for ticker in self.sector_etfs:
            df = yf.download(ticker, start=start_date, end=end_date)
            sector_data = pd.concat([sector_data, df['Close']], axis=1)
        return sector_data

    def get_economic_indicators(self, start_date, end_date):
        metrics = ['GDP', 'UNRATE', 'FEDFUNDS']
        economic_data = pd.DataFrame()
        for metric in metrics:
            data = fred.get_series(metric, start_date, end_date)
            economic_data[metric] = data
        return economic_data

    # def get_news_sentiment(self, sector):
    #     # Example news API integration
    #     pass

if __name__ == "__main__":
    data_collector = DataCollector()
    data_collector.get_sector_data('2020-01-01', '2021-01-01')
    data_collector.get_economic_indicators('2020-01-01', '2021-01-01')
    # data_collector.get_news_sentiment('Technology')