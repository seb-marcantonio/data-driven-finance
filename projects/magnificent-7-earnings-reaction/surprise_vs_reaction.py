import json, os, statistics as st
BASE="/sessions/beautiful-eloquent-ritchie/mnt/outputs"
# reaction date + clean EPS surprise % (operating/ex one-time where flagged); None = exclude from magnitude fit
ROWS = {
 "AAPL":[("2025-08-01",9.03),("2025-10-31",4.52),("2026-01-30",6.74),("2026-05-01",3.08)],
 "MSFT":[("2025-07-31",8.31),("2025-10-30",12.84),("2026-01-29",6.15),("2026-04-30",5.17)],
 "NVDA":[("2025-08-28",3.96),("2025-11-20",4.00),("2026-02-26",5.19),("2026-05-21",6.25)],
 "AMZN":[("2025-08-01",28.24),("2025-10-31",24.20),("2026-02-06",-1.02),("2026-04-30",-5.5)], # Apr = clean operating miss (ex-Anthropic gain)
 "GOOGL":[("2025-07-24",7.44),("2025-10-30",25.33),("2026-02-05",9.73),("2026-04-30",None)], # Apr GAAP distorted by $37B equity gain -> exclude magnitude
 "META":[("2025-07-31",20.61),("2025-10-30",7.9),("2026-01-29",8.16),("2026-04-30",9.9)], # Oct & Apr = clean operating (ex one-time tax items)
 "TSLA":[("2025-07-24",0.70),("2025-10-23",-7.41),("2026-01-29",9.94),("2026-04-23",15.85)],
}
FLAG={("META","2025-10-30"),("META","2026-04-30"),("AMZN","2026-04-30"),("GOOGL","2026-04-30")}
react={}
for tk in ROWS:
    d=json.load(open(os.path.join(BASE,tk.lower()+".json"))); react[tk]={r["t"]:r["ch"] for r in d}

def pear(x,y):
    mx,my=st.mean(x),st.mean(y)
    n=sum((a-mx)*(b-my) for a,b in zip(x,y)); den=(sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))**.5
    return n/den

pairs=[]   # (tk,date,surprise,reaction,flagged)
for tk,lst in ROWS.items():
    for dt,sp in lst:
        pairs.append((tk,dt,sp,react[tk][dt],(tk,dt) in FLAG))

print("Surprise % vs stock reaction % (clean/operating EPS):\n")
print(f"{'stock':6}{'date':12}{'surprise':>10}{'reaction':>10}  note")
for tk,dt,sp,rc,fl in pairs:
    print(f"{tk:6}{dt:12}{('n/a' if sp is None else f'{sp:+.1f}%'):>10}{rc:>9.2f}%  {'one-time item, operating used' if fl else ''}")

# magnitude correlation (drop None)
mag=[(sp,rc) for tk,dt,sp,rc,fl in pairs if sp is not None]
clean=[(sp,rc) for tk,dt,sp,rc,fl in pairs if sp is not None and not fl]
print(f"\nCorrelation(surprise, reaction), all {len(mag)} with a clean number: {pear([a for a,_ in mag],[b for _,b in mag]):+.2f}")
print(f"Correlation, excluding the 4 one-time-item quarters ({len(clean)}): {pear([a for a,_ in clean],[b for _,b in clean]):+.2f}")

beats=[(tk,dt,sp,rc) for tk,dt,sp,rc,fl in pairs if sp is not None and sp>0]
misses=[(tk,dt,sp,rc) for tk,dt,sp,rc,fl in pairs if sp is not None and sp<0]
print(f"\nBeat rate: {len(beats)}/{len(mag)} reports beat EPS estimates ({100*len(beats)/len(mag):.0f}%)")
print(f"  of those beats, only {sum(rc>0 for _,_,_,rc in beats)}/{len(beats)} saw the stock RISE")
print(f"  {sum(rc<0 for _,_,_,rc in beats)}/{len(beats)} beat and FELL")
print(f"Misses: {len(misses)} (", ", ".join(f'{tk} {rc:+.1f}%' for tk,dt,sp,rc in misses), ")")
sign_agree=sum((sp>0)==(rc>0) for tk,dt,sp,rc,fl in pairs if sp is not None)
print(f"Sign agreement (beat->up / miss->down): {sign_agree}/{len(mag)} = {100*sign_agree/len(mag):.0f}%  (coin flip = 50%)")

print("\nClean poster children (stocks with no one-time-item noise):")
for tk in ["NVDA","MSFT","TSLA"]:
    print(f"  {tk}: surprises "+", ".join(f'{sp:+.0f}%' for _,sp in ROWS[tk])+"  ->  reactions "+", ".join(f'{react[tk][dt]:+.1f}%' for dt,_ in ROWS[tk]))
