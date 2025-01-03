from sklearn.ensemble import RandomForestRegressor
from textblob import TextBlob
import numpy as np

class SectorRotationAnalyzer:
    def __init__(self, data_collector):
        self.data_collector = data_collector
        self.model = RandomForestRegressor()
        
    def calculate_sector_momentum(self, data, window=20):
        return data.pct_change(window)
    
    def calculate_relative_strength(self, data):
        returns = data.pct_change()
        return returns.div(returns.mean(axis=1), axis=0)
    
    def train_economic_model(self, sector_data, economic_data):
        # Train machine learning model using economic indicators
        X = economic_data
        y = sector_data
        self.model.fit(X, y)
        
    # def get_sector_sentiment(self, sector_news):
    #     sentiments = []
    #     for news in sector_news:
    #         blob = TextBlob(news)
    #         sentiments.append(blob.sentiment.polarity)
    #     return np.mean(sentiments)