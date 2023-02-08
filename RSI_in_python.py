import matplotlib
import matplotlib.pyplot as plt
import yfinance as yf

symbol = yf.Ticker('SEK=X')
prices = symbol.history(interval="1wk",period="max")
del prices["Dividends"],prices["Stock Splits"],prices["Open"],prices["High"],prices["Low"],prices["Volume"]

delta = prices["Close"].diff()

delta_up = delta.copy()
delta_down = delta.copy()

delta_up[delta_up<0] = 0
delta_down[delta_down>0] = 0
avg_up = delta_up.rolling(14).mean()
avg_down = delta_down.rolling(14).mean().abs()
rsi = 100 * avg_up / (avg_up + avg_down)
rsi.head(20)

plt.rcParams['figure.figsize'] = (8, 6)
price_plot = plt.subplot2grid((10,1), (0,0), rowspan = 4, colspan = 1)
price_plot.plot(prices['Close'])
price_plot.set_title('Price')

rsi_plot = plt.subplot2grid((10,1), (5,0), rowspan = 4, colspan = 1)
rsi_plot.plot(rsi, color='red')
rsi_plot.set_title('Relative Strength Index')
rsi_plot.axhline(30, color='purple')
rsi_plot.axhline(70, color='purple')

plt.show()