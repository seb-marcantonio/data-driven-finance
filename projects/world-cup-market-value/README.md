# World Cup market value: how much does a great World Cup add?

Analyzes how a strong World Cup re-rates a player's and a national team's Transfermarkt market value, comparing the value just before each tournament with the value just after. Covers individual breakout players and the squad totals of the final-four teams across 2014, 2018, and 2022. The framing is financial: the tournament as an "earnings event" that re-prices players, where the market rewards positive surprise more than the trophy itself.

## Key findings
- Individuals can re-rate steeply (Azzedine Ounahi +329% in 2022), while whole squads move far less, roughly 1 to 16 percent, because a squad is a diversified book and its expensive core is already priced in.
- The biggest squad gains go to teams that beat expectations (Morocco +15.9% in 2022), not the pre-priced favourites.

## Files
- `wc_charts.py` — generates both charts
- `wc_players.png`, `wc_teams.png` — the two charts (players and teams)
- `post.md` — the LinkedIn post
- `methodology.md` — full data sources, definitions, caveats, and the underlying data tables

## Run
```bash
pip install matplotlib
python wc_charts.py
```
Produces `wc_players.png` and `wc_teams.png`.

## Data
Transfermarkt market values: player value histories, and archived tournament squad pages via the Internet Archive. The 2014 team totals are reconstructed by summing individual player values (validated against the archived pre-tournament page). See `methodology.md` for exact sources and caveats. Market values are Transfermarkt estimates, not transaction prices.
