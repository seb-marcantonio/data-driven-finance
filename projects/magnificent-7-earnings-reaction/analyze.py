import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
WIN_START = "2025-06-27"   # trailing 12 months ...
WIN_END   = "2026-06-26"   # ... ending on last close
ANCHOR    = "2025-06-26"   # prior close for net-return calc

# Earnings-reaction days (the trading day the market reacts to the report).
# NVDA/TSLA/NFLX/META report after close -> reaction = next session.
# KO reports before open -> reaction = same session.
EARN = {
 "NVDA": ["2025-08-28","2025-11-20","2026-02-26","2026-05-21"],
 "TSLA": ["2025-07-24","2025-10-23","2026-01-29","2026-04-23"],
 "NFLX": ["2025-07-18","2025-10-22","2026-01-21","2026-04-17"],
 "META": ["2025-07-31","2025-10-30","2026-01-29","2026-04-30"],
 "KO":   ["2025-07-22","2025-10-21","2026-02-10","2026-04-28"],
}

def load(tk):
    with open(os.path.join(BASE, tk.lower()+".json")) as f:
        rows = json.load(f)
    rows.sort(key=lambda r: r["t"])  # oldest -> newest
    return rows

print(f"Window: {WIN_START} -> {WIN_END}  (anchor close {ANCHOR})\n")
summary = []
for tk in ["NVDA","TSLA","NFLX","META","KO"]:
    rows = load(tk)
    bydate = {r["t"]: r for r in rows}

    # --- consistency check: recompute ch from consecutive closes ---
    bad = 0
    for i in range(1, len(rows)):
        implied = (rows[i]["c"]/rows[i-1]["c"] - 1)*100
        if abs(implied - rows[i]["ch"]) > 0.06:
            bad += 1
            if bad <= 5:
                print(f"  [{tk}] CH MISMATCH {rows[i]['t']}: stated {rows[i]['ch']} vs implied {implied:.2f}")

    win = [r for r in rows if WIN_START <= r["t"] <= WIN_END]
    n = len(win)
    earn_days = EARN[tk]
    earn_rows = [bydate[d] for d in earn_days]

    total_move = sum(abs(r["ch"]) for r in win)
    earn_move  = sum(abs(r["ch"]) for r in earn_rows)
    share = earn_move/total_move*100
    # variance / "risk" framing: share of sum of squared daily returns
    var_share = sum(r["ch"]**2 for r in earn_rows)/sum(r["ch"]**2 for r in win)*100
    fair = 4/n*100
    fairmult = share/fair

    avg_earn   = earn_move/len(earn_rows)
    norm_rows  = [r for r in win if r["t"] not in earn_days]
    avg_norm   = sum(abs(r["ch"]) for r in norm_rows)/len(norm_rows)

    # net 12-month price return over window
    c_end = bydate[WIN_END]["c"]; c_anchor = bydate[ANCHOR]["c"]
    net = (c_end/c_anchor - 1)*100
    # compounded contribution of the 4 earnings days
    e_comp = 1.0
    for r in earn_rows: e_comp *= (1+r["ch"]/100)
    e_comp = (e_comp-1)*100
    # year excluding the 4 earnings days
    rest = 1.0
    for r in norm_rows: rest *= (1+r["ch"]/100)
    rest = (rest-1)*100

    print(f"{tk}: rows={n}  consistency_mismatches={bad}")
    print(f"   earnings reaction moves: " + ", ".join(f"{r['t']} {r['ch']:+.2f}%" for r in earn_rows))
    print(f"   total |move| sum = {total_move:.1f}   earnings |move| sum = {earn_move:.1f}")
    print(f"   SHARE of yearly movement on 4 earnings days = {share:.1f}%  ({fairmult:.1f}x the 1.6% fair share)")
    print(f"   VARIANCE share (sum of squared moves) = {var_share:.1f}%")
    print(f"   avg earnings-day |move| = {avg_earn:.2f}%   avg normal-day |move| = {avg_norm:.2f}%   ratio = {avg_earn/avg_norm:.1f}x")
    print(f"   net 12m price return = {net:+.1f}%   |   4 earnings days compounded = {e_comp:+.1f}%   |   other {len(norm_rows)} days = {rest:+.1f}%\n")
    summary.append((tk,n,share,var_share,avg_earn,avg_norm,avg_earn/avg_norm,net,e_comp))

print("="*78)
print(f"{'TK':5}{'AbsShare%':>10}{'VarShare%':>10}{'AvgErn':>8}{'AvgNorm':>9}{'Ratio':>7}{'Net%':>8}{'ErnComp%':>10}")
for tk,n,share,vshare,ae,an,ratio,net,ec in summary:
    print(f"{tk:5}{share:>10.1f}{vshare:>10.1f}{ae:>8.2f}{an:>9.2f}{ratio:>6.1f}x{net:>8.1f}{ec:>10.1f}")
shares=[s[2] for s in summary]; vshares=[s[3] for s in summary]
print(f"\nAvg ABS share across 5 names: {sum(shares)/len(shares):.1f}%   Avg VARIANCE share: {sum(vshares)/len(vshares):.1f}%")
print(f"4 days as % of {summary[0][1]} trading days: {4/summary[0][1]*100:.2f}%")
