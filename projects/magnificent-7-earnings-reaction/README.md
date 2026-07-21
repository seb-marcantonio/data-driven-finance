# Magnificent 7: beating estimates barely moved the stock

Tests the common assumption that topping EPS estimates sends a stock up. Across the last four quarters, the Magnificent 7 beat consensus EPS on 24 of 27 reports, yet the stock fell after 16 of those beats. The size of the surprise barely predicted the next-day move (correlation about 0.2). What moves these names is guidance and how results land against already-high expectations. A result that is priced in does nothing.

## Files
- `surprise_vs_reaction.py` — main analysis (EPS surprise vs next-day reaction)
- `chart4_beats_updown.py` and `chart4_beats_updown.png` — the beats-vs-direction chart
- other `*.py` — supporting analysis, charting, and verification scripts
- `data/` — per-ticker price and earnings JSON (`_raw_*` are the unprocessed pulls)
- `post.md` — the LinkedIn post

## Run
```bash
pip install matplotlib
python surprise_vs_reaction.py
```
Note: some scripts contain hardcoded absolute paths from the original working session. Adjust the `BASE` path near the top of a script before rerunning.

## Data
Consensus vs reported EPS (CoinCodex and company filings); next-day price reaction (Yahoo Finance, split and dividend adjusted), last four quarters. Operating EPS is used where one-time tax or investment items distorted headline numbers, and Alphabet's April report is excluded from the magnitude fit because a one-time $37B gain made its headline EPS meaningless.
