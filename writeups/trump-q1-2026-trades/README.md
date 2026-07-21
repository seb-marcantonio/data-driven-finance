# Analyzing All 3,642 of Trump's Q1 2026 Stock Trades

A full parse of Donald Trump's Q1 2026 periodic transaction report (OGE Form 278-T) covering 3,642 trades across 1,008 unique tickers and $447M in transaction volume. The analysis matches sales to earlier buys FIFO, marks still-held positions to market, and benchmarks against the S&P 500, finding combined estimated Q1 gains of $13.5M (about $3.8M ahead of the index) with 37% of capital in Technology. The framing also surfaces statement-trade timing (159 public statements landing within +/-14 days of a related trade) while staying descriptive and non-accusatory.

## The LinkedIn post

I analyzed all 3,642 of Donald Trump's Q1 2026 stock trades from his filing (OGE 278-T).

Scale:
- 3,642 trades, 1,008 unique tickers, 90 days
- $447M in transaction volume (midpoint between $207M and $686M)
- $121M to $390M in purchases, $86M to $296M in sales
- 37% of capital in Technology

Performance (Q1):
- Combined estimated gains of $13.5M
- Better than the S&P 500 by $3.8M, roughly 39% better
- 64% of still-held positions are in the green (373 of 580)
- Top 5 still-held winners: SNDK 355%, INTC 181%, MRVL 162%, AMD 157%, IRDM 152%

Timing:
- 159 of his public statements landed within ±14 days of a trade in that company
- 13 on the same day as the trade
- Bought TXN Jan 12, signed chip tariff EO 2 days later
- Bought NEE Mar 17, approved gas expansion 3 days later

Methodology: OGE Form 278-T, Yahoo Finance closes, P&L matches each Q1 sale FIFO to its earlier Q1 buy, still-held positions marked to the May 26 close, S&P benchmark uses the same dollars and same hold windows. Pre-existing position sales (~$66M) are excluded since the filing doesn't disclose cost basis.

Is this what you were expecting? Curious to hear what others think.

Source: OGE Form 278-T, filed May 8, 2026 - https://lnkd.in/gknvGE55

## Notes
- Data source: OGE Form 278-T (Trump's Q1 2026 periodic transaction report); Yahoo Finance (yfinance) daily closes for prices and S&P 500 benchmark; web searches for public statements/executive orders matched by date to trades.
- Original chat produced: two charts (a Trump vs S&P 500 performance chart used first as the scroll-stopper, and a sector allocation pie chart), plus an audited Excel workbook / CSVs where every figure was independently recomputed from source. Files are not included here.
