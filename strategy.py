import pandas as pd


class SectorRotationStrategy:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.current_positions = {}
        
    def generate_signals(self, sector_data, economic_data):
        # Combine the factors
        signals = pd.DataFrame()
        
        # Factor 1: Economic Model Predictions
        economic_predictions = self.analyzer.model.predict(economic_data)
        signals['economic_score'] = economic_predictions
        
        # Factor 2: Technical Analysis
        momentum = self.analyzer.calculate_sector_momentum(sector_data)
        relative_strength = self.analyzer.calculate_relative_strength(sector_data)
        signals['technical_score'] = (momentum + relative_strength) / 2
        
        # # Factor 3: Sentiment
        # signals['sentiment_score'] = sentiment_data
        
        # Combine scores with weights
        signals['total_score'] = (
            0.5 * signals['economic_score'] +
            0.5 * signals['technical_score']
        )
        
        return signals
    
    def execute_rotation(self, signals, top_n=3):
        # Select top N sectors based on combined signals
        top_sectors = signals.nlargest(top_n, 'total_score')
        return top_sectors.index.tolist()