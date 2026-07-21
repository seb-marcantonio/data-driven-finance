# What 2 Seconds of Information Advantage Was Worth on Wall Street

This analysis reconstructs the 2013 Thomson Reuters/University of Michigan Consumer Sentiment scandal using tick-level S&P 500 e-mini futures data. From 2007 to July 2013, high-speed traders paid extra to receive the sentiment index at 9:54:58 ET, two seconds ahead of the regular paid feed at 9:55:00. Measuring the tape, the early second saw a burst of trading (on April 12, 2013: 1,057 trades and 3,712 contracts versus 37 trades and 146 contracts two seconds later) and the price had already moved before the official feed went out. Across 11 release Fridays the two seconds before 9:55 averaged 1,881 contracts versus 209 on non-release Fridays, and the burst vanished after the feed was suspended under New York AG pressure. The framing question: was this price discovery, or just a paid head start?

## The LinkedIn post

What 2 seconds of information advantage was worth on Wall Street

From 2007 to July 2013, Thomson Reuters sold the University of Michigan Consumer Sentiment Index in tiers. One group of high-speed traders paid extra to receive it at 9:54:58 AM ET, two seconds before the regular paid feed at 9:55:00 (and roughly five minutes before the 10:00 public release).

I pulled tick-level S&P 500 e-mini futures (ES) data to measure what those two seconds were worth (Databento).

April 12, 2013, a sentiment release Friday:
- In the minute before the release: about 13 trades per second
- 9:54:58, the early-tier second: 1,057 trades, 3,712 contracts, price falling from 1584.00 to 1582.50
- 9:55:00, the regular paid feed: 37 trades, 146 contracts, and no new move

The 9:54:58 second traded about 25 times the volume of the 9:55:00 second, and the price had already moved before the official feed went out.

This was not a one-off. Across the 11 release Fridays before the suspension, the two seconds before 9:55:00 averaged 1,881 ES contracts and 0.55 index points of movement. On non-release Fridays, the same two seconds averaged 209 contracts and 0.08 points.

Thomson Reuters suspended the early feed in July 2013, under pressure from the New York Attorney General, and the early burst disappeared: on release days afterward, the 9:54:58 second fell from about 1,600 contracts to 30.

Was any of this price discovery, or just a paid head start?

Methodology: S&P 500 e-mini futures, front-month continuous by volume (ES.v.0), from CME Globex MDP 3.0 (GLBX.MDP3) via Databento, trades and ohlcv-1s schemas. A 9:50 to 10:01 ET window on every Friday in 2013. Release days are the twice-monthly Michigan Consumer Sentiment Fridays, identified by the volume signature around 9:55 and cross-checked against reporting. All times ET.

## Notes
- Data source: Databento, CME Globex MDP 3.0 (GLBX.MDP3), S&P 500 e-mini futures ES.v.0 (front-month continuous by volume), trades and ohlcv-1s schemas; release-day identification cross-checked against reporting.
- Original chat produced: Chart 2 (the release-day 9:54:58 volume collapsing from ~1,600 to ~30 contracts after the July 2013 suspension), paired with the post. Not included here.
- Tagging note (from the chat): tag @Databento natively in the LinkedIn composer; the methodology link in the draft was a placeholder (linkedin.com/feed#).
