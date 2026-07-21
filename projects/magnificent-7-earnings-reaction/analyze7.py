import json, os
BASE = os.path.dirname(os.path.abspath(__file__))
WIN_START, WIN_END = "2025-07-01", "2026-06-26"   # common window across all 7

# all report after close -> reaction = next trading session
EARN = {
 "AAPL": ["2025-08-01","2025-10-31","2026-01-30","2026-05-01"],
 "MSFT": ["2025-07-31","2025-10-30","2026-01-29","2026-04-30"],
 "NVDA": ["2025-08-28","2025-11-20","2026-02-26","2026-05-21"],
 "AMZN": ["2025-08-01","2025-10-31","2026-02-06","2026-04-30"],
 "GOOGL":["2025-07-24","2025-10-30","2026-02-05","2026-04-30"],
 "META": ["2025-07-31","2025-10-30","2026-01-29","2026-04-30"],
 "TSLA": ["2025-07-24","2025-10-23","2026-01-29","2026-04-23"],
}
ORDER = ["META","TSLA","AMZN","GOOGL","MSFT","AAPL","NVDA"]  # provisional; will sort by share later

def load(tk):
    d = json.load(open(os.path.join(BASE, tk.lower()+".json")))
    d.sort(key=lambda r: r["t"]); return d

def comp(rows):
    p=1.0
    for r in rows: p*=(1+r["ch"]/100)
    return (p-1)*100

rows_summary=[]
for tk in EARN:
    d = load(tk); bd={r["t"]:r for r in d}
    bad=0
    for i in range(1,len(d)):
        imp=(d[i]["c"]/d[i-1]["c"]-1)*100
        if abs(imp-d[i]["ch"])>0.06: bad+=1
    win=[r for r in d if WIN_START<=r["t"]<=WIN_END]
    er=[bd[x] for x in EARN[tk]]
    miss=[x for x in EARN[tk] if x not in bd]
    norm=[r for r in win if r["t"] not in EARN[tk]]
    tot=sum(abs(r["ch"]) for r in win); em=sum(abs(r["ch"]) for r in er)
    share=em/tot*100
    var=sum(r["ch"]**2 for r in er)/sum(r["ch"]**2 for r in win)*100
    ae=em/4; an=sum(abs(r["ch"]) for r in norm)/len(norm)
    net=comp(win); ecomp=comp(er); rest=comp(norm)
    fair=4/len(win)*100
    rows_summary.append(dict(tk=tk,n=len(win),bad=bad,miss=miss,share=share,var=var,ae=ae,an=an,
                             ratio=ae/an,net=net,ecomp=ecomp,fair=fair,
                             ermoves=[(r["t"],r["ch"]) for r in er]))

rows_summary.sort(key=lambda s:-s["share"])
for s in rows_summary:
    print(f"{s['tk']:6} n={s['n']} chk_mismatch={s['bad']} miss={s['miss']}")
    print("   earnings: "+", ".join(f"{t} {c:+.2f}%" for t,c in s['ermoves']))
    print(f"   share={s['share']:.1f}% (fair {s['fair']:.2f}%, {s['share']/s['fair']:.1f}x)  var={s['var']:.1f}%  avgErn={s['ae']:.2f}% avgNorm={s['an']:.2f}% ratio={s['ratio']:.1f}x  net={s['net']:+.1f}% ernComp={s['ecomp']:+.1f}%\n")

print("="*86)
print(f"{'TK':6}{'AbsShare%':>10}{'VarShare%':>10}{'AvgErn':>8}{'AvgNorm':>9}{'Ratio':>7}{'Net%':>8}{'ErnComp%':>10}")
for s in rows_summary:
    print(f"{s['tk']:6}{s['share']:>10.1f}{s['var']:>10.1f}{s['ae']:>8.2f}{s['an']:>9.2f}{s['ratio']:>6.1f}x{s['net']:>8.1f}{s['ecomp']:>10.1f}")
print(f"\nAvg abs share {sum(s['share'] for s in rows_summary)/7:.1f}%   Avg var share {sum(s['var'] for s in rows_summary)/7:.1f}%")
print(f"window days = {rows_summary[0]['n']}, 4 days = {4/rows_summary[0]['n']*100:.2f}% of the year")
