import json, os
BASE="/sessions/beautiful-eloquent-ritchie/mnt/outputs"
WIN_START, WIN_END = "2025-07-01", "2026-06-26"
# reaction date = next session after each after-close report
EARN = {
 "META":["2025-07-31","2025-10-30","2026-01-29","2026-04-30"],
 "MSFT":["2025-07-31","2025-10-30","2026-01-29","2026-04-30"],
 "AMZN":["2025-08-01","2025-10-31","2026-02-06","2026-04-30"],
 "GOOGL":["2025-07-24","2025-10-30","2026-02-05","2026-04-30"],
 "TSLA":["2025-07-24","2025-10-23","2026-01-29","2026-04-23"],
 "NVDA":["2025-08-28","2025-11-20","2026-02-26","2026-05-21"],
 "AAPL":["2025-08-01","2025-10-31","2026-01-30","2026-05-01"]}
# post text values: name -> (avgErn, avgNorm, mult, absShare[chart], varShare)
CLAIM={"META":("Meta",10.4,1.4,7.5,10.9,34),"MSFT":("Microsoft",5.2,1.1,4.6,7.0,19),
 "AMZN":("Amazon",6.0,1.4,4.4,6.7,20),"GOOGL":("Alphabet",3.5,1.3,2.7,4.2,12),
 "TSLA":("Tesla",4.4,2.2,2.0,3.2,5),"NVDA":("Nvidia",2.8,1.7,1.6,2.6,4),"AAPL":("Apple",1.6,1.1,1.6,2.5,3)}
def load(t):
    d=json.load(open(os.path.join(BASE,t.lower()+".json"))); d.sort(key=lambda r:r["t"]); return d,{r["t"]:r for r in d}
def comp(rs):
    p=1.0
    for r in rs: p*=(1+r["ch"]/100)
    return (p-1)*100
fails=0
def ck(cond,label):
    global fails
    print(("  OK  " if cond else " FAIL ")+label)
    if not cond: fails+=1
res={}
for tk in EARN:
    d,bd=load(tk); w=[r for r in d if WIN_START<=r["t"]<=WIN_END]
    miss=[x for x in EARN[tk] if x not in bd]; er=[bd[x] for x in EARN[tk] if x in bd]
    nm=[r for r in w if r["t"] not in EARN[tk]]
    ae=sum(abs(r["ch"]) for r in er)/4; an=sum(abs(r["ch"]) for r in nm)/len(nm)
    ab=sum(abs(r["ch"]) for r in er)/sum(abs(r["ch"]) for r in w)*100
    var=sum(r["ch"]**2 for r in er)/sum(r["ch"]**2 for r in w)*100
    res[tk]=dict(n=len(w),miss=miss,ae=ae,an=an,ab=ab,var=var,net=comp(w),rest=comp(nm),er=er)

print("=== WINDOW & DATES ===")
ck(all(res[t]["n"]==249 for t in res), "all 7 datasets span exactly 249 trading days (post: 'out of 249')")
ck(all(res[t]["miss"]==[] for t in res), "all 28 earnings reaction dates exist as real trading days")
ck(249-4==245, "other days = 245 (post: 'the other 245 days')")

print("\n=== PER-STOCK: earnings dates, moves, and the bullet/variance numbers ===")
for tk in ["META","MSFT","AMZN","GOOGL","TSLA","NVDA","AAPL"]:
    nm,ae_c,an_c,mu_c,ab_c,var_c=CLAIM[tk]; r=res[tk]
    print(f"\n{nm}: "+", ".join(f"{x['t']}={x['ch']:+.2f}%" for x in r['er']))
    ck(abs(r['ae']-ae_c)<0.06, f"  avg earnings move {r['ae']:.2f}% -> post {ae_c}%")
    ck(abs(r['an']-an_c)<0.06, f"  avg normal move {r['an']:.2f}% -> post {an_c}%")
    ck(abs(r['ae']/r['an']-mu_c)<0.06, f"  multiple {r['ae']/r['an']:.2f}x -> post {mu_c}x")
    ck(round(r['var'])==var_c, f"  share of risk (variance) {r['var']:.1f}% -> post ~{var_c}%")
    ck(abs(r['ab']-ab_c)<0.06, f"  share of movement {r['ab']:.1f}% -> chart {ab_c}%")

print("\n=== HEADLINE & NARRATIVE CLAIMS ===")
ck(max(res,key=lambda t:res[t]['var'])=="META", "Meta = the most volatile of the seven (highest risk share)")
ck(round(res['META']['var'])==34, f"Meta ~ a third of its year of risk ({res['META']['var']:.1f}%)")
ck(res['AAPL']['var']<4 and res['NVDA']['var']<4, f"Apple ({res['AAPL']['var']:.1f}%) & Nvidia ({res['NVDA']['var']:.1f}%) under 4%")
ck(abs(res['NVDA']['net']-22)<0.6, f"Nvidia rose ~22% on the year (net {res['NVDA']['net']:+.1f}%)")
ck(all(x['ch']<0 for x in res['NVDA']['er']), "Nvidia: all four earnings reactions negative")
ck(abs(res['MSFT']['net']+24)<0.6, f"Microsoft fell ~24% (net {res['MSFT']['net']:+.1f}%)")
ck(abs(res['MSFT']['rest']+13)<0.6, f"Microsoft ex-earnings ~-13% (halves the drop) ({res['MSFT']['rest']:+.1f}%)")
ck(10**2==100, "risk: one 10% day = a hundred 1% days (10 squared vs 1 squared)")

print("\n"+("="*46)+"\nRESULT: "+("ALL CHECKS PASS" if fails==0 else f"{fails} CHECK(S) FAILED")+"\n"+("="*46))
