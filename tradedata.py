import alpaca_trade_api as tradeapi
import pandas as pd

api = tradeapi.REST()
ticker = 'FB'
bars = api.get_barset(ticker,'day',limit = 1000)[ticker]

def bar_to_list(bar):
    templist = []
    for column in ['c','h','l','o','t','v']:
        templist.append( bar.__getattr__(column))
    return templist

def bars_to_list(bars):
    barslist = []
    for bar in bars:
        temp = bar_to_list(bar)
        barslist.append(temp)
    return barslist
        

data = bars_to_list(bars)

df = pd.DataFrame(data, columns = ['c','h','l','o','t','v'])

pp = []
for i in range(99,df.shape[0]):
    test = df.loc[i-99:i,'c'].mean()
    pp.append(test)
    df.loc[df.index[i],'SMA'] = test

df.plot(x = 't', y = ['c','SMA'])


