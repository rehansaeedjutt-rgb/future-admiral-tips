import os

lessons = {
    "01-introduction-to-markets.md": """# 📖 Chapter 01: Introduction to Financial Markets

## What Are Financial Markets?

Financial markets are venues where buyers and sellers come together to trade financial assets, including currencies, stocks, commodities, and cryptocurrencies.

## The Four Major Markets

### 1. Forex (Foreign Exchange)
The largest market in the world with over $7 trillion in daily volume. Operates 24 hours a day, 5 days a week.

### 2. Stock Market
Where shares of publicly traded companies are exchanged. Major exchanges include NYSE, NASDAQ, and LSE.

### 3. Cryptocurrency Market
A 24/7 market known for high volatility and significant opportunity.

### 4. Commodity Market
Where raw materials like gold, oil, and agricultural products are traded.

## Key Market Participants

- **Retail Traders** — Individuals like you
- **Institutional Traders** — Banks and hedge funds
- **Market Makers** — Provide liquidity
- **Central Banks** — Set monetary policy

## Key Takeaway

Understanding the structure of financial markets is the first step to becoming a successful trader.

---
*Next: What is Technical Analysis?*""",

    "02-technical-analysis.md": """# 📖 Chapter 02: What is Technical Analysis?

## Definition

Technical Analysis (TA) is the study of historical price data and chart patterns to forecast future price movements.

## Core Principles

1. **Price Discounts Everything** — All known information is already reflected in the price.
2. **Prices Move in Trends** — Markets tend to move in directional patterns.
3. **History Tends to Repeat** — Patterns recur because human psychology is constant.

## Key Tools

- **Candlestick Charts** — Visualize price action over time
- **Support & Resistance** — Key price zones
- **Trend Lines** — Identify direction
- **Indicators** — RSI, MACD, Moving Averages
- **Chart Patterns** — Head & Shoulders, Triangles, Flags

## When to Use Technical Analysis

- Identifying entry and exit points
- Confirming trend direction
- Setting stop losses and take profits

## Key Takeaway

Technical analysis is the language of the chart. Learn to read it fluently.

---
*Next: What is Fundamental Analysis?*""",

    "03-fundamental-analysis.md": """# 📖 Chapter 03: What is Fundamental Analysis?

## Definition

Fundamental Analysis (FA) evaluates an asset's intrinsic value by examining economic, financial, and geopolitical factors.

## Key Drivers

### 1. Interest Rates
Higher rates strengthen a currency. Lower rates weaken it.

### 2. Inflation (CPI)
Rising inflation typically leads to rate hikes, strengthening the currency.

### 3. Employment Data (NFP)
Strong employment supports currency strength.

### 4. GDP Growth
A growing economy attracts capital and strengthens its currency.

### 5. Geopolitical Events
Wars, elections, and trade disputes create volatility.

## Economic Calendar

Every serious trader checks the economic calendar daily. High-impact events cause rapid price movements.

## Technical vs. Fundamental

- **Technical** — Answers *when* to enter
- **Fundamental** — Answers *why* the market moves

## Key Takeaway

The best traders combine both disciplines. Fundamentals set the bias; technicals time the entry.

---
*Next: Understanding Candlestick Charts*""",

    "04-candlestick-charts.md": """# 📖 Chapter 04: Understanding Candlestick Charts

## What is a Candlestick?

A candlestick represents price action over a specific time period. It shows four data points: Open, High, Low, and Close (OHLC).

## Anatomy

- **Body** — Range between open and close
- **Wick (Shadow)** — Highest and lowest points

## Bullish vs. Bearish

- **Bullish (Green)** — Close is above open
- **Bearish (Red)** — Close is below open

## Essential Patterns

### Single-Candle Patterns
- **Doji** — Indecision
- **Hammer** — Bullish reversal
- **Shooting Star** — Bearish reversal

### Two-Candle Patterns
- **Bullish Engulfing** — Strong bullish signal
- **Bearish Engulfing** — Strong bearish signal

### Three-Candle Patterns
- **Morning Star** — Bullish reversal
- **Evening Star** — Bearish reversal

## Key Takeaway

Candlestick patterns are only reliable at key levels. Context is everything.

---
*Next: Support and Resistance*""",

    "05-support-resistance.md": """# 📖 Chapter 05: Support and Resistance

## Definition

Support and Resistance are price levels where the market historically reverses or pauses.

- **Support** — A floor where buying pressure exceeds selling
- **Resistance** — A ceiling where selling pressure exceeds buying

## Why They Work

They represent areas where institutional orders cluster. Traders remember these levels and act on them repeatedly.

## Drawing Them Correctly

1. Use higher timeframes (Daily, 4H)
2. Mark zones, not exact lines
3. Look for multiple touches
4. Consider volume at each level

## Role Reversal

When support breaks, it often becomes resistance. And vice versa. This is one of the most powerful concepts in trading.

## Key Takeaway

Trade reactions at these zones — not breakouts blindly. Wait for confirmation.

---
*Next: Trend Lines and Channels*""",

    "06-trend-lines.md": """# 📖 Chapter 06: Trend Lines and Channels

## What is a Trend Line?

A trend line is a diagonal line connecting two or more price points. It defines the direction and strength of a trend.

- **Uptrend** — Connects higher lows
- **Downtrend** — Connects lower highs

## Channels

A channel consists of two parallel trend lines:
- **Upper line** — Resistance
- **Lower line** — Support

Price oscillates between these lines until a breakout occurs.

## How to Draw Properly

1. Minimum two touches required
2. The more touches, the stronger the line
3. Never force a line — let it form naturally
4. Adjust as the market evolves

## Trading Trend Lines

- **Bounce trades** — Enter on the third touch
- **Breakout trades** — Enter when the line breaks with volume

## Key Takeaway

Trend lines define the rhythm of the market. Trade with them, not against them.

---
*Next: Moving Averages*""",

    "07-moving-averages.md": """# 📖 Chapter 07: Moving Averages (SMA & EMA)

## Definition

A Moving Average smooths price data to identify trend direction over a given period.

## Types

### SMA (Simple Moving Average)
Equal weight to all prices in the period.

### EMA (Exponential Moving Average)
More weight to recent prices. Reacts faster to price changes.

## Common Periods

- **20 EMA** — Short-term trend
- **50 EMA** — Medium-term trend
- **200 EMA** — Long-term trend (the most respected)

## Trading Signals

### Golden Cross
When the 50 EMA crosses above the 200 EMA — bullish signal.

### Death Cross
When the 50 EMA crosses below the 200 EMA — bearish signal.

## Dynamic Support & Resistance

Moving averages act as moving support in an uptrend and moving resistance in a downtrend.

## Key Takeaway

The 200 EMA is the single most important trend filter. Above it, bullish. Below it, bearish.

---
*Next: RSI and MACD*""",

    "08-rsi-macd.md": """# 📖 Chapter 08: RSI and MACD Indicators

## RSI (Relative Strength Index)

Measures momentum on a scale of 0 to 100.

- **Above 70** — Overbought (potential reversal)
- **Below 30** — Oversold (potential bounce)

### RSI Divergence
When price makes a new high but RSI does not, a reversal is likely. This is one of the most powerful signals in trading.

## MACD (Moving Average Convergence Divergence)

Consists of three components:
- **MACD Line** — 12 EMA minus 26 EMA
- **Signal Line** — 9 EMA of MACD line
- **Histogram** — Difference between the two

### Trading Signals
- **Bullish** — MACD line crosses above signal line
- **Bearish** — MACD line crosses below signal line

## Best Practice

Use RSI and MACD together. Confirmation from both increases reliability.

## Key Takeaway

Indicators are tools, not answers. Combine them with price action for the best results.

---
*Next: Chart Patterns*""",

    "09-chart-patterns.md": """# 📖 Chapter 09: Chart Patterns

## Reversal Patterns

### Head & Shoulders
Three peaks, with the middle highest. Signals a bearish reversal.

### Double Top / Double Bottom
Two equal highs or lows. Signals trend reversal.

## Continuation Patterns

### Ascending Triangle
Higher lows, flat resistance. Bullish continuation.

### Descending Triangle
Lower highs, flat support. Bearish continuation.

### Bull Flag
Sharp move up, then consolidation. Bullish continuation.

### Bear Flag
Sharp move down, then consolidation. Bearish continuation.

## How to Trade Patterns

1. Wait for the pattern to fully form
2. Enter on the breakout
3. Place stop loss at the opposite side of the pattern
4. Target the pattern's height as your profit

## Key Takeaway

Patterns are high-probability setups — but only when confirmed by volume and context.

---
*Next: Risk Management*""",

    "10-risk-management.md": """# 📖 Chapter 10: Risk Management Fundamentals

## The Golden Rule

Never risk more than 1–2% of your account on a single trade.

## Why It Matters

Even 10 consecutive losses at 1% risk only reduces your account by ~10%. At 10% risk, ten losses wipe out 65% of your capital.

## Stop Losses

Every trade must have a stop loss. No exceptions.

- Place it at a level where your trade idea is invalidated
- Never move it against your position

## Risk-to-Reward Ratio

Aim for a minimum of 1:2. Risk $100 to make $200.

With a 40% win rate and 1:2 R:R, you are profitable.

## Position Sizing Formula

Position Size = (Account Balance × Risk %) ÷ Stop Loss Distance

## Key Takeaway

Professionals focus on risk first, profits second. Survival is the game.

---
*Next: Position Sizing and Leverage*""",

    "11-position-sizing.md": """# 📖 Chapter 11: Position Sizing and Leverage

## What is Position Sizing?

Position sizing determines how much capital to allocate to a single trade. It is the single most important risk control.

## The Formula

Position Size = (Account Balance × Risk %) ÷ (Entry − Stop Loss)

## Example

- Account: $10,000
- Risk: 1% = $100
- Entry: 1.1000
- Stop: 1.0950 (50 pips)
- Position size = $100 ÷ 50 pips = $2 per pip

## What is Leverage?

Leverage allows you to control larger positions with less capital.

- 1:10 leverage = $1 controls $10
- 1:100 leverage = $1 controls $100

## The Danger

High leverage amplifies both profits and losses. Most retail traders blow up because of over-leveraging, not bad analysis.

## Key Takeaway

Use the lowest leverage that allows you to take your calculated position size.

---
*Next: Trading Psychology*""",

    "12-psychology.md": """# 📖 Chapter 12: Trading Psychology 101

## Why Psychology Matters

80% of trading success is mental. The strategy is only 20%.

## The Four Deadly Emotions

### 1. Fear
Causes you to exit winners too early or miss valid setups.

### 2. Greed
Causes you to hold losers too long and oversize positions.

### 3. Hope
Causes you to hold losing trades in the hope they will recover.

### 4. Regret
Causes revenge trading after a loss.

## Building Discipline

1. Follow a written trading plan
2. Journal every trade
3. Review performance weekly
4. Take breaks after losses
5. Never trade emotionally

## The Mindset of a Professional

- Losses are a business expense
- Consistency beats intensity
- The process matters more than any single trade

## Key Takeaway

Master your emotions, and the market becomes clear.

---
*Next: Order Types Explained*""",

    "13-order-types.md": """# 📖 Chapter 13: Order Types Explained

## Market Order
Executes immediately at the current market price. Fast but may slip during volatility.

## Limit Order
Executes only at your specified price or better. Ensures price but may not fill.

## Stop Order
Becomes a market order once a specific price is reached. Used for entries and stop losses.

## Stop-Loss Order
Automatically closes a losing position at a predetermined level. Essential for risk management.

## Take-Profit Order
Automatically closes a winning position at a target price.

## OCO (One-Cancels-the-Other)
Two orders linked together — when one executes, the other is cancelled. Used for combining stop-loss and take-profit.

## Trailing Stop
A stop-loss that moves with the price as the trade progresses, locking in profits.

## Key Takeaway

Knowing when to use each order type is critical for efficient execution.

---
*Next: Reading the Economic Calendar*""",

    "14-economic-calendar.md": """# 📖 Chapter 14: Reading the Economic Calendar

## What is an Economic Calendar?

A schedule of upcoming economic events that impact financial markets.

## Impact Levels

- 🔴 **High** — Causes major volatility (FOMC, NFP, CPI)
- 🟠 **Medium** — Moderate volatility (Retail Sales, PMI)
- 🟡 **Low** — Minimal impact

## Key Events to Watch

### FOMC Statement
Federal Reserve's interest rate decision. Most impactful event for USD.

### NFP (Non-Farm Payrolls)
US employment data. Released first Friday of each month.

### CPI (Consumer Price Index)
Inflation data. Directly influences rate decisions.

### ECB & BOE Decisions
Central bank policy for EUR and GBP.

## How to Trade Around News

1. Check the calendar daily
2. Know the exact release time
3. Reduce or close positions before high-impact events
4. Wait for the initial volatility to settle before entering

## Key Takeaway

News is not noise — it is the catalyst for the biggest moves.

---
*Next: Building Your Trading Plan*""",

    "15-trading-plan.md": """# 📖 Chapter 15: Building Your Trading Plan

## Why You Need a Plan

A trader without a plan is a gambler. Your plan is your business strategy.

## What Your Plan Should Include

### 1. Market Selection
Which markets do you trade? Forex, Crypto, Indices?

### 2. Timeframe
What timeframe do you trade? Scalping, Day Trading, Swing Trading?

### 3. Strategy Rules
- Entry criteria (exact conditions)
- Exit criteria (stop loss and take profit)
- Position sizing rules

### 4. Risk Parameters
- Maximum risk per trade (1–2%)
- Maximum daily loss
- Maximum weekly loss

### 5. Trading Schedule
- When do you trade?
- When do you not trade?

### 6. Review Process
- Daily journaling
- Weekly review
- Monthly performance analysis

## Testing Your Plan

Before risking real money, backtest your strategy on at least 100 historical trades. Record the win rate, average win, and average loss.

## Key Takeaway

A written plan is your anchor in a chaotic market. Without it, emotions will control you.

---
*End of Course. Congratulations!*"""
}

# Create education folder
os.makedirs("education", exist_ok=True)

# Create all files
for filename, content in lessons.items():
    filepath = os.path.join("education", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Created: {filepath}")

print(f"\n🎉 Total {len(lessons)} lessons created successfully!")