import pandas as pd

class PortfolioManager:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=[
            'symbol', 'amount', 'entry_price', 'current_price', 
            'value', 'profit_loss'
        ])
        
    def update_portfolio(self, token_data):
        """Update portfolio with latest prices"""
        for index, row in self.portfolio.iterrows():
            symbol = row['symbol']
            if symbol in token_data:
                current_price = token_data[symbol]['price']
                self.portfolio.at[index, 'current_price'] = current_price
                self.portfolio.at[index, 'value'] = row['amount'] * current_price
                self.portfolio.at[index, 'profit_loss'] = (
                    (current_price - row['entry_price']) / row['entry_price']
                )
    
    def add_position(self, symbol, amount, entry_price):
        """Add new position to portfolio"""
        new_row = {
            'symbol': symbol,
            'amount': amount,
            'entry_price': entry_price,
            'current_price': entry_price,
            'value': amount * entry_price,
            'profit_loss': 0.0
        }
        self.portfolio = self.portfolio.append(new_row, ignore_index=True)
