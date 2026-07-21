# How Fast Markets Priced Trump's Liberation Day Tariffs

A tick-level look at how the S&P 500 reacted the moment Trump revealed his country-specific reciprocal tariff rates on April 2, 2025 ("Liberation Day"). Using Databento tick data on S&P 500 e-mini futures, the analysis shows the index fell 1.42% in 64 seconds once the chart appeared, with trade frequency surging from a 15/sec baseline to a 335/sec peak. The angle is an Efficient Market Hypothesis test: markets are fast but not instant, the drop did not accelerate until 36 seconds in, and the daily data shows the selloff continuing for four more trading days to a -11.5% bottom, raising the question of slow digestion versus new information (Canada and China retaliation) piling on.

## The LinkedIn post

The S&P 500 fell 11.5% in 5 trading days after Liberation Day (Trump's reciprocal tariff announcement). The first 1.42% of that happened in 64 seconds.

At 4:26:07 PM ET, Trump held up the chart with country-specific reciprocal tariff rates.
S&P 500 e-mini futures, tick by tick (Databento):
- 4:26:07 PM ET (chart appears): 5,750.75
- 4:26:30 PM ET (23 sec after chart): 5,742.50 (-8 since chart)
- 4:26:43 PM ET (cliff begins, 36 sec after chart): 5,728.00
- 4:27:11 PM ET (biggest 60-sec drop ended): 5,669.25 (-81 points, -1.42%)

Trade frequency surged from a 15/sec baseline to a peak of 335/sec during the cliff.

The tick data shows something the daily price data hides. Markets are fast, but they are not instant. Prices began drifting within seconds of the chart appearing, but the drop (where most of the move happened) didn't happen until 36 seconds in, and the full 1.42% drop took 64 seconds to complete. The Efficient Market Hypothesis says public information should be priced in instantly.

Looking at the daily data, the selloff continued for 4 more trading days, eventually bottoming at -11.5% by April 8. Was that the market slowly digesting the original information, new information piling on (Canada's auto-tariff retaliation on April 3, China's 34% retaliation on April 4), or both?

Would you classify any of this as an efficient market reaction?

Methodology: ES front-month continuous contract (ES.c.0) on CME Globex MDP 3.0 dataset (GLBX.MDP3) via Databento "ohlcv-1s" and "trades" schemas. Reveal timestamps verified against C-SPAN footage. Daily index closes from Yahoo Finance.

## Notes
- Data source: Databento (CME Globex MDP 3.0 / GLBX.MDP3, "ohlcv-1s" and "trades" schemas) for tick data; Yahoo Finance (yfinance) for daily index closes; reveal timestamps verified against C-SPAN footage.
- Original chat produced: multiple candidate charts (dual-panel EMH tick chart `chart_emh_dualpanel.png`, 90-second tick chart `chart_es_tick_90s.png`, 30-second ultra-zoom, 15-minute 1-second view, and a day-over-day country-ETF round-trip chart `chart3_round_trip.png` covering USA SPY, Japan EWJ, Germany/EU EWG, China FXI, Vietnam VNM). Final post intended to run with a photo of Trump holding the chart, the dual-panel tick chart, and the round-trip chart. These files are not included here.
