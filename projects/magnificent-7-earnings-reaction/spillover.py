import json, os, itertools, statistics as st
from collections import Counter
BASE="/sessions/beautiful-eloquent-ritchie/mnt/outputs"
TK=["META","MSFT","AMZN","GOOGL","TSLA","NVDA","AAPL"]
EARN = {  # reaction (next-session) dates
 "META":["2025-07-31","2025-10-30","2026-01-29","2026-04-30"],
 "MSFT":["2025-07-31","2025-10-30","2026-01-29","2026-04-30"],
 "AMZN":["2025-08-01","2025-10-31","2026-02-06","2026-04-30"],
 "GOOGL":["2025-07-24","2025-10-30","2026-02-05","2026-04-30"],
 "TSLA":["2025-07-24","2025-10-23","2026-01-29","2026-04-23"],
 "NVDA":["2025-08-28","2025-11-20","2026-02-26","2026-05-21"],
 "AAPL":["2025-08-01","2025-10-31","2026-01-30","2026-05-01"]}

data={}
for tk in TK:
    for r in json.load(open(os.path.join(BASE,tk.lower()+".json"))):
        data.setdefault(r["t"],{})[tk]=r["ch"]
full=[dt for dt in sorted(data) if len(data[dt])==7]

def pear(x,y):
    mx,my=st.mean(x),st.mean(y)
    num=sum((a-mx)*(b-my) for a,b in zip(x,y))
    den=(sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))**.5
    return num/den
series={tk:[data[dt][tk] for dt in full] for tk in TK}
corrs=[pear(series[a],series[b]) for a,b in itertools.combinations(TK,2)]
print(f"1) BASELINE co-movement: average pairwise correlation of daily returns = {st.mean(corrs):.2f}")
print(f"   range {min(corrs):.2f} to {max(corrs):.2f} over {len(full)} days\n")

base_abs=st.mean(abs(data[dt][tk]) for dt in full for tk in TK)
print(f"2) baseline average absolute daily move (any stock, any day) = {base_abs:.2f}%\n")

# who reports on each date (clustering)
rep_on={}
for tk,ds in EARN.items():
    for dt in ds: rep_on.setdefault(dt,[]).append(tk)
print("3) CLUSTERING - reporters reacting on the same day:")
for dt in sorted(rep_on):
    if len(rep_on[dt])>1: print(f"   {dt}: {', '.join(rep_on[dt])}")
print(f"   distinct earnings-reaction days: {len(rep_on)} (for 28 reports)\n")

# spillover: on a reporter's day, how did NON-reporting peers move?
peerabs=[]; samedir=[]; signed=[]
for tk in TK:
    for dt in EARN[tk]:
        rc=data[dt][tk]
        for p in TK:
            if p==tk or p in rep_on[dt]: continue   # exclude self and co-reporters
            pc=data[dt][p]
            peerabs.append(abs(pc)); samedir.append((pc>=0)==(rc>=0)); signed.append((1 if rc>=0 else -1)*pc)
print("4) SPILLOVER to NON-reporting peers on a member's earnings day:")
print(f"   their avg absolute move = {st.mean(peerabs):.2f}%  (vs {base_abs:.2f}% baseline)")
print(f"   moved SAME direction as the reporter: {100*st.mean(samedir):.0f}% of the time")
print(f"   avg move in the reporter's direction = {st.mean(signed):+.2f}%\n")

# cleanest case: Nvidia reports alone (later than the rest)
print("5) CLEAN CASE - Nvidia reports by itself; how did the other 6 move that day?")
for dt in EARN["NVDA"]:
    rc=data[dt]["NVDA"]; peers=[p for p in TK if p!="NVDA"]
    pv=[data[dt][p] for p in peers]
    print(f"   {dt}: NVDA {rc:+.2f}%  |  others avg {st.mean(pv):+.2f}% (abs {st.mean(abs(v) for v in pv):.2f}%), "
          f"{sum((v>=0)==(rc>=0) for v in pv)}/6 same direction")
