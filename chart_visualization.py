import plotly.graph_objects as go
from plotly.subplots import make_subplots

class ChartVisualizer:
    @staticmethod
    def create_price_chart(data):
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                           vertical_spacing=0.05,
                           subplot_titles=('Price History', 'Volume'))
        
        # Price Candles
        fig.add_trace(go.Candlestick(
            x=data['timestamp'],
            open=data['open'],
            high=data['high'],
            low=data['low'],
            close=data['close']
        ), row=1, col=1)
        
        # Volume Bars
        fig.add_trace(go.Bar(
            x=data['timestamp'],
            y=data['volume'],
            marker_color='rgba(0,128,0,0.5)'
        ), row=2, col=1)
        
        fig.update_layout(
            height=600,
            showlegend=False,
            xaxis_rangeslider_visible=False
        )
        return fig
