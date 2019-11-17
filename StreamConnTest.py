import alpaca_trade_api as tradeapi

api = tradeapi.REST()
aapl = api.polygon.historic_agg('day', 'AAPL', limit=1000).df