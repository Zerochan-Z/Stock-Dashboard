# Stock-Dashboard
Week 3 Python Learning

---

### Line 1: `returns = data.pct_change().dropna()`

| Part | What it does |
|------|--------------|
| `data` | DataFrame with closing prices for AAPL and TSLA |
| `.pct_change()` | Calculates daily percentage change for each column |
| `.dropna()` | Removes the first row (which is `NaN` because no previous day to compare) |
| `returns` | New DataFrame containing daily returns (in decimal form) |

---

### Line 2: `correlation = returns['AAPL'].corr(returns['TSLA'])`

| Part | What it does |
|------|--------------|
| `returns['AAPL']` | Series of AAPL daily returns |
| `returns['TSLA']` | Series of TSLA daily returns |
| `.corr()` | Calculates correlation coefficient between the two series |
| `correlation` | Stores the result (number between -1 and +1) |

---

### What Correlation Tells You

| Correlation | Meaning | Trading implication |
|-------------|---------|---------------------|
| `+1.0` | Move perfectly together | Diversification doesn't help |
| `+0.7` | Strong positive relationship | Often move same direction |
| `0` | No relationship | One moves, other random |
| `-0.5` | Weak negative relationship | Slightly opposite moves |
| `-1.0` | Perfect inverse | One up = other down |

---

### One Sentence Summary

**`.pct_change()` turns prices into daily returns, `.dropna()` removes the first empty row, and `.corr()` calculates how closely two stocks move together (from -1 opposite to +1 same direction).**
