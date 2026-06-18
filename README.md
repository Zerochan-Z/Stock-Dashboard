## ✅ README.md – AAPL Stock SMA & Crossover Signal

---

# 📊 AAPL Stock SMA & Crossover Signal

A Python program that downloads Apple (AAPL) stock data, calculates a 5-day Simple Moving Average (SMA), detects crossover signals, and visualizes them with a price chart.

---

## 📋 Program Flow

| Step | Action |
|:----:|--------|
| 1 | Download AAPL stock data from Yahoo Finance |
| 2 | Clean and format data (dates as column, remove multi-index) |
| 3 | Plot Open and Close prices |
| 4 | Calculate 5-day Simple Moving Average (SMA) |
| 5 | Detect crossover signals (Close crosses above SMA) |
| 6 | Plot Close price with SMA overlay |
| 7 | Save chart as `stock_signals.jpg` |

---

## 🧠 Key Code Concepts

| Concept | How it's used |
|---------|----------------|
| `yfinance` | Download historical stock data |
| `df.columns.droplevel(1)` | Remove multi-index columns |
| `df.reset_index()` | Turn date index into column |
| `pd.to_numeric()` | Ensure Close is numeric |
| Manual SMA calculation | Loop over `Close` prices with window of 5 |
| Crossover detection | Compare `Close` vs `SMA` with `.shift(1)` |
| `matplotlib` | Plot price lines and save chart |
| `plt.savefig()` | Save chart as JPG file |

---

## 📊 SMA Calculation Logic

| Component | How it works |
|-----------|--------------|
| **Window** | 5-day Simple Moving Average |
| **Formula** | `SMA_5 = (Close[i-4] + Close[i-3] + Close[i-2] + Close[i-1] + Close[i]) / 5` |
| **Loop** | Starts from index 4 (needs 5 data points) |

---

## 🔀 Crossover Detection

| Condition | Meaning |
|-----------|---------|
| `prev_close < prev_sma` | Yesterday's Close was below SMA |
| `curr_close > curr_sma` | Today's Close is above SMA |
| **Both true** | **Buy Signal** – prints crossover date |

---

## 📤 Output Examples

### Console Output
```
Downloading data from 2025-01-01 to 2026-01-01...
Data downloaded.
Loading AAPL price chart...
2025-03-15
2025-06-22
2025-09-10
Stock_signals saved as jpg
Thanks for using this system
(❁´◡`❁)
Chill ~~~
```

### Chart Output
- Blue line: **Close Price**
- Orange line: **5-Day SMA**
- Legend, title, and axis labels included
- Saved as `stock_signals.jpg`

---

## ✅ Key Takeaways

| Concept | How it's used |
|---------|----------------|
| `yfinance` | Download real stock data |
| Manual SMA | Loop-based calculation (no `.rolling()`) |
| Crossover logic | `prev_close < prev_sma` and `curr_close > curr_sma` |
| `plt.savefig()` | Export chart as image |
| `plt.plot()` | Overlay multiple lines on same chart |

---

## 📁 Project Status

| Feature | Status |
|---------|--------|
| Download AAPL data | ✅ |
| Clean and format data | ✅ |
| Plot Open and Close | ✅ |
| Calculate 5-day SMA | ✅ |
| Detect crossover signals | ✅ |
| Print crossover dates | ✅ |
| Plot Close + SMA | ✅ |
| Save chart as JPG | ✅ |
| Error handling | ⚠️ Basic |

---

> *Last updated: May 2026*
```
