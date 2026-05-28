import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ['AAPL','TSLA']
start_date= '2025-01-01'
end_date= '2026-01-01'
print('Downloading data from Yahoo Finance...\n')
data = yf.download(tickers, start_date, end_date)['Close'] # print only close only
returns=data.pct_change().dropna()

correlation= returns['AAPL'].corr(returns['TSLA'])
print(f'\nCorrelation between AAPL and TSLA: {correlation:.4f}')

print(f"\nLoading {tickers} chart...")
plt.figure(figsize=(12,5))
plt.plot(data.index, data['AAPL'],label ='AAPL Close Price',color='royalblue',linewidth=2)
plt.plot(data.index, data['TSLA'],label ='TSLA Close Price',color='green',linewidth=2)
plt.title('AAPL VS TSLA - Closing Prices)')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True,alpha=0.3)
plt.show()

plt.figure(figsize=(12,5))
plt.plot(returns.index, returns['AAPL'], label ='AAPL Daily Return', color ='royalblue',lw=1,alpha=0.7)
plt.plot(returns.index, returns['TSLA'],label= 'TSLA Daily Return', color ='green',lw=1,alpha=0.7)
plt.axhline(y=0, color='red',linestyle='--',lw=1,label ='0% Reference Line')
plt.title('AAPL VS TSLA - Daily Return)')
plt.xlabel('Date')
plt.ylabel('Daily Return (%)')
plt.legend()
plt.grid(True,alpha=0.3)
plt.show()