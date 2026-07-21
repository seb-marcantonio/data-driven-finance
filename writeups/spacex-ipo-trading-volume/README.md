# SpaceX IPO: Turnover vs Float

This analysis looks past the headline 19% first-day pop on SpaceX's June 2026 Nasdaq debut (ticker SPCX) and measures turnover instead: the share of the tradable float that changed hands each day. Because insiders hold most of the company, only about 5% of shares (roughly 635M of ~13.1B) actually float, so day-one volume of ~522M shares equalled ~82% of the entire float, and cumulative volume passed 100% of the float by day two. The framing contrasts SpaceX's ultra-thin, rapidly churning float against NVIDIA (~96% free float, ~0.6% daily turnover), arguing that day one was priced on supply and demand rather than the business, and every figure was reconciled against the raw Databento volume data before publishing.

## The LinkedIn post

The number everyone is quoting from SpaceX's debut is the 19% first-day pop. The more revealing number is turnover: the share of tradable stock that changed hands.

Here is what most observers skipped. SpaceX's float is about 635 million shares (its IPO plus the over-allotment), but the company has roughly 13.1 billion shares outstanding (Elon Musk and insiders hold most of it). So the tradable float is only about 5% of the total. NVIDIA is the opposite: about 96% of its 24.3 billion shares trade freely.

On June 12, SpaceX opened well after the bell, once the Nasdaq IPO cross had cleared the order backlog, so it traded for only part of the session. Even in that shortened window:
- About 522 million shares traded, roughly 82% of SpaceX's entire float, in less than a full day.
- NVIDIA trades about 130 million shares on a typical day, about 0.6% of its float.
- So SpaceX's tradable float changed hands at roughly 140 times the rate of NVIDIA's.
- Day three turned over about 51% of the float, the session SPCX hit an all-time high near $226.

Volume tells you how many shares traded. Turnover tells you how that compares to the float. On day one, SpaceX's volume reached about 82% of its float, and by day two, it had traded more than the entire float.

Do you judge an IPO by its first-day price, or by how much of the float actually changes hands? With only about 5% of SpaceX tradable, was day one priced on the business (cash flow), or on supply and demand?

Methodology: turnover = a day's volume divided by free float. Daily volumes from Databento (consolidated US venues, June 12 to 16, 2026; NVIDIA shown as its average across those days). SpaceX's ~635M float (IPO plus over-allotment) and ~13.1B shares outstanding from the IPO terms and prospectus; NVIDIA's 96% float from GuruFocus, LLC.

## Notes
- Data source: Databento (consolidated US venue volumes, EQUS.SUMMARY, June 12-16, 2026); SpaceX float/shares from the IPO terms and S-1 prospectus; NVIDIA's 96% free float from GuruFocus. FactSet was cited in an early draft but dropped after it turned out not to have been used.
- Original chat produced: a waffle chart (SpaceX June 12 debut at 82.3% of float, June 16 record high at 50.7%, NVIDIA typical day at 0.6%) and Python verification scripts that re-derived every figure against the Databento pull, though those files are not included here.
- Tagging note (from the chat): tag @Databento and @GuruFocus natively in the LinkedIn composer so mentions resolve; the methodology links in the draft were placeholders (linkedin.com/feed#).
