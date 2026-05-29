import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticket ='AAPL'
start_date = '2025-01-01'
end_date = '2026-01-01'

print(f'Downloading data from {start_date} to {end_date}...\n')
data = yf.download(ticket, start_date, end_date)
data.columns = data.columns.droplevel(1)
data.index.name = None
data.reset_index(inplace=True)
data.rename(columns={'index':'Date'}, inplace=True)

print('Data downloaded.\n')
print(f'Loading {ticket} price chart...\n')
plt.plot(data.index,data['Close'],color='royalblue',lw=2,label='Close')
plt.plot(data.index,data['Open'],color='orange',lw=2,label='Open')
plt.legend(loc='upper left')
plt.title('AAPL 1 Year Data')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend(loc='upper left')
plt.show()

data['SMA']= None

# SMA(day i) = (Close[i-4] + Close[i-3] + Close[i-2] + Close[i-1] + Close[i]) / 5
for i in range(4,len(data)):
    SMA_5 = (data.loc[i - 4, 'Close'] +
             data.loc[i - 3, 'Close'] +
             data.loc[i - 2, 'Close'] +
             data.loc[i - 1, 'Close'] +
             data.loc[i, 'Close']) / 5

    data.loc[i, 'SMA'] = SMA_5

'''
Using the SMA you calculated in Task 2, find days where:

Yesterday's Close < Yesterday's SMA

Today's Close > Today's SMA

Print out the dates where this happens.

Hint: Use .shift(1) to compare with previous day.

'''

for i in range(5,len(data)):
    prev_close = data.loc[i - 1, 'Close']
    prev_sma = data.loc[i - 1, 'SMA']
    curr_close = data.loc[i, 'Close']
    curr_sma = data.loc[i, 'SMA']

    if prev_close < prev_sma and curr_close > curr_sma:
        print(data.loc[i,'Date'].strftime('%Y-%m-%d'))

plt.plot(data.index,data['Close'],color='royalblue',lw=2,label='Close')
plt.plot(data.index,data['SMA'],color='orange',lw=2,label='SMA')
plt.legend(loc='upper left')
plt.title('AAPL with SMA')
plt.xlabel('Date')
plt.ylabel('Price (USD)')

plt.savefig('stock_signals.jpg')
print('Stock_signals saved as jpg')
plt.show()

print('\n\n\nThanks for using this system \n(❁´◡`❁)\nChill ~~~')