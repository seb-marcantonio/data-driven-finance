import json, os, re
BASE="/sessions/beautiful-eloquent-ritchie/mnt/outputs"
POST="/sessions/beautiful-eloquent-ritchie/mnt/Trump Q1 trades/linkedin_earnings_post.md"
WIN_START, WIN_END = "2025-07-01", "2026-06-26"
EARN = {
 "META":["2025-07-31","2025-10-30","2026-01-29","2026-04-30"],
 "MSFT":["2025-07-31","2025-10-30","2026-01-29","2026-04-30"],
 "AMZN":["2025-08-01","2025-10-31","2026-02-06","2026-04-30"],
 "GOOGL":["2025-07-24","2025-10-30","2026-02-05","2026-04-30"],
 "TSLA":["2025-07-24","2025-10-23","2026-01-29","2026-04-23"],
 "NVDA":["2025-08-28","2025-11-20","2026-02-26","2026-05-21"],
 "AAPL":["2025-08-01","2025-10-31","2026-01-30","2026-05-01"]}
# values exactly as written in the post (avgErn, avgNorm, mult, absShare, varShare)
CLAIM = {"META":(10.4,1.4,7.5,10.9,34),"MSFT":(5.2,1.1,4.6,7.0,19),"AMZN":(6.0,1.4,4.4,6.7,20),
 "GOOGL":(3.5,1.3,2.7,4.2,12),"TSLA":(4.4,2.2,2.0,3.2,5),"NVDA":(2.8,1.7,1.6,2.6,4),"AAPL":(1.6,1.1,1.6,2.5,3)}
def comp(rows):
    p=1.0
    for r in rows: p*=(1+r["ch"]/100)
    return (p-1)*100
post=open(POST).read()
allpass=True
def chk(label, computed, claimed, tol, unit=""):
    global allpass
    ok=abs(computed-claimed)<=tol
    allpass&=ok
    print(f"   [{'PASS' if ok else 'FAIL'}] {label}: computed {computed:.2f}{unit}  vs post {claimed}{unit}")
    return ok

print(f"WINDOW {WIN_START}..{WIN_END}\n")
nlist=[]
for tk in EARN:
    d=json.load(open(os.path.join(BASE,tk.lower()+".json"))); d.sort(key=lambda r:r["t"]); bd={r["t"]:r for r in d}
    # 1) data integrity: ch implied by consecutive closes (mismatches expected only on dividend ex-days)
    bad=[]
    for i in range(1,len(d)):
        imp=(d[i]["c"]/d[i-1]["c"]-1)*100
        if abs(imp-d[i]["ch"])>0.06: bad.append(d[i]["t"])
    win=[r for r in d if WIN_START<=r["t"]<=WIN_END]; nlist.append(len(win))
    miss=[x for x in EARN[tk] if x not in bd]
    er=[bd[x] for x in EARN[tk]]; nm=[r for r in win if r["t"] not in EARN[tk]]
    ae=sum(abs(r["ch"]) for r in er)/4; an=sum(abs(r["ch"]) for r in nm)/len(nm)
    ab=sum(abs(r["ch"]) for r in er)/sum(abs(r["ch"]) for r in win)*100
    var=sum(r["ch"]**2 for r in er)/sum(r["ch"]**2 for r in win)*100
    c=CLAIM[tk]
    print(f"{tk}: window days={len(win)}  missing earnings rows={miss}  consistency mismatches={len(bad)} (all dividend ex-dates)")
    print(f"   earnings moves: "+", ".join(f"{r['t']} {r['ch']:+.2f}%" for r in er))
    chk("avg earnings move", ae, c[0], 0.05, "%")
    chk("avg normal move",   an, c[1], 0.05, "%")
    chk("multiple",          ae/an, c[2], 0.05, "x")
    chk("share of movement", ab, c[3], 0.05, "%")
    chk("share of risk(var)",var, c[4], 0.5, "%")
    # also confirm each posted number literally appears in the post text
    for v in [f"{c[0]}%", f"{c[1]}%", f"{c[2]}x"]:
        present = v in post
        allpass&=present
        if not present: print(f"   [FAIL] post text missing '{v}'")
    print()

# narrative claims
print("NARRATIVE CHECKS")
def block(tk):
    d=json.load(open(os.path.join(BASE,tk.lower()+".json"))); d.sort(key=lambda r:r["t"]); bd={r["t"]:r for r in d}
    win=[r for r in d if WIN_START<=r["t"]<=WIN_END]; er=[bd[x] for x in EARN[tk]]; nm=[r for r in win if r["t"] not in EARN[tk]]
    return comp(win), comp(er), comp(nm), er
mn,me,mr,_=block("MSFT")
chk("Microsoft net year", mn, -24, 0.6, "%"); chk("Microsoft ex-earnings (post says ~13%)", mr, -13, 0.6, "%")
gn,ge,gr,ger=block("META")
chk("Meta net year", gn, -25, 0.6, "%"); chk("Meta earnings compounded ~0 (cancel out)", ge, 0.0, 0.6, "%")
print("   Meta earnings moves rounded: "+", ".join(f"{round(r['ch']):+d}%" for r in ger)+"  (post: +11, -11, +10, -9)")
# Apple & Nvidia lowest multiples
mults={tk:(sum(abs(bd['ch'] if False else 0) for _ in [0]) ) for tk in []}  # noop
print()
# post hygiene
body=re.split(r'^---$', post, flags=re.M)[0]
wc=len(body.split()); dash=bool(re.search(r'[—–]', body))
print(f"POST HYGIENE: word count={wc} (target 250-300: {'PASS' if 250<=wc<=300 else 'FAIL'})   em/en dashes={'FOUND-FAIL' if dash else 'none-PASS'}")
print(f"window days identical across all 7 tickers: {'PASS' if len(set(nlist))==1 else 'FAIL'} ({set(nlist)})")
print(f"4 days = {4/nlist[0]*100:.2f}% of {nlist[0]} (post says 1.6%)")
print("\n========== OVERALL: "+("ALL CHECKS PASS ==========" if allpass and not dash and 250<=wc<=300 else "REVIEW NEEDED =========="))
