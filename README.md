# Stock-Dashboard
Week 3 Python Learning

---

### `returns = data.pct_change().dropna()`

| Part | What it does |
|------|--------------|
| `data` | DataFrame with closing prices for AAPL and TSLA |
| `.pct_change()` | Calculates daily percentage change for each column |
| `.dropna()` | Removes the first row (which is `NaN` because no previous day to compare) |
| `returns` | New DataFrame containing daily returns (in decimal form) |

---

### `correlation = returns['AAPL'].corr(returns['TSLA'])`

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

## Visual Example

After `reset_index()`, your DataFrame looks like this:

| (index) | Date       | Close  | Open   |
|---------|------------|--------|--------|
| 0       | 2025-01-02 | 185.90 | 185.50 |
| 1       | 2025-01-03 | 184.20 | 184.00 |
| 2       | 2025-01-04 | 183.50 | 183.00 |

| Access method | Code | Returns |
|---------------|------|---------|
| `.loc` by label | `data.loc[0, 'Close']` | `185.90` |
| `.loc` by label | `data.loc[1, 'Date']` | `2025-01-03` |
| `.iloc` by position | `data.iloc[0, 1]` | `185.90` (row 0, column 1) |
| `.iloc` by position | `data.iloc[1, 0]` | `2025-01-03` (row 1, column 0) |

---

## Why Both Exist?

| Use `.loc` when... | Use `.iloc` when... |
|--------------------|---------------------|
| Your index has meaningful labels (dates, names, IDs) | You don't care about labels, just row position |
| You know the row name (e.g., `'2025-01-02'`) | You know the row number (0,1,2...) |
| You want clear, readable code | You need speed (`.iloc` is slightly faster) |

---

## One Sentence Summary

**`.loc` accesses by row **label** (name), `.iloc` accesses by **position** (0,1,2...) – in your code, both would work the same because your labels are 0,1,2...**

### One Sentence Summary

**`.pct_change()` turns prices into daily returns, `.dropna()` removes the first empty row, and `.corr()` calculates how closely two stocks move together (from -1 opposite to +1 same direction).**
