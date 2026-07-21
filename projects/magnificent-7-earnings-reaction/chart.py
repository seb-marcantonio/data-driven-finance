import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np, os

OUT = "/sessions/beautiful-eloquent-ritchie/mnt/Trump Q1 trades"
os.makedirs(OUT, exist_ok=True)

labels   = ["Meta","Netflix","Coca-Cola","Tesla","Nvidia"]
avg_earn = [10.38, 6.77, 2.50, 4.37, 2.79]
avg_norm = [ 1.38, 1.36, 0.78, 2.16, 1.71]
abs_share= [10.9,  7.5,  4.9,  3.2,  2.6]
var_share= [33.6, 19.7, 11.9,  5.1,  3.5]

INK="#0F1B2D"; GRID="#E6EAEF"; EARN="#1F6FEB"; NORM="#C2C9D2"; RISK="#0B2C66"; ACCENT="#E8623A"
plt.rcParams.update({"font.family":"DejaVu Sans","text.color":INK,"axes.edgecolor":"#9AA3AE",
                     "axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK})
x = np.arange(len(labels)); w=0.38

def header(fig, title, subtitle, source):
    fig.text(0.065, 0.95, title, fontsize=18.5, fontweight="bold", ha="left", va="top")
    fig.text(0.065, 0.885, subtitle, fontsize=11.5, color="#5A6470", ha="left", va="top")
    fig.text(0.065, 0.035, source, fontsize=8.7, color="#8A929C", ha="left", va="bottom")

# ---------- Chart 1 ----------
fig, ax = plt.subplots(figsize=(11.5,6.8), dpi=140)
fig.subplots_adjust(top=0.80, bottom=0.135, left=0.085, right=0.965)
ax.bar(x-w/2, avg_earn, w, label="Earnings-reaction day", color=EARN)
ax.bar(x+w/2, avg_norm, w, label="Average normal day", color=NORM)
for i,(e,n) in enumerate(zip(avg_earn,avg_norm)):
    ax.text(x[i]-w/2, e+0.15, f"{e:.1f}%", ha="center", va="bottom", fontsize=10.5, fontweight="bold", color=EARN)
    ax.text(x[i]+w/2, n+0.15, f"{n:.1f}%", ha="center", va="bottom", fontsize=10.5, color="#6B7480")
    ax.text(x[i], max(e,n)+1.0, f"{e/n:.1f}x", ha="center", va="bottom", fontsize=11.5, fontweight="bold", color=ACCENT)
ax.set_ylabel("Average absolute one-day move (%)", fontsize=11.5)
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=12.5)
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0)); ax.set_ylim(0,13.4)
ax.set_axisbelow(True); ax.yaxis.grid(True,color=GRID); ax.set_facecolor("white")
for s in ["top","right"]: ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=11, loc="upper right")
header(fig, "An earnings day is not a normal day",
       "Average size of a one-day price move, trailing 12 months. Orange = how many times bigger an earnings day is.",
       "Data: stockanalysis.com daily closes (dividend-adjusted). Earnings reaction = the session the market trades the report (next day if reported after close).")
fig.savefig(f"{OUT}/chart1_earnings_vs_normal.png", facecolor="white"); plt.close(fig)

# ---------- Chart 2 ----------
fig, ax = plt.subplots(figsize=(11.5,6.8), dpi=140)
fig.subplots_adjust(top=0.80, bottom=0.135, left=0.085, right=0.965)
ax.bar(x-w/2, abs_share, w, label="Share of total movement (sum of daily moves)", color=EARN)
ax.bar(x+w/2, var_share, w, label="Share of risk (variance: violent days weigh more)", color=RISK)
for i,(a,v) in enumerate(zip(abs_share,var_share)):
    ax.text(x[i]-w/2, a+0.4, f"{a:.1f}%", ha="center", va="bottom", fontsize=10.5, fontweight="bold", color=EARN)
    ax.text(x[i]+w/2, v+0.4, f"{v:.0f}%", ha="center", va="bottom", fontsize=10.5, fontweight="bold", color=RISK)
ax.axhline(1.6, color=ACCENT, ls=(0,(5,4)), lw=1.8, label="1.6% = the 4 days' fair share (4 of 251 days)")
ax.set_ylabel("Share of the year in 4 earnings days (%)", fontsize=11.5)
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=12.5)
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0)); ax.set_ylim(0,38)
ax.set_axisbelow(True); ax.yaxis.grid(True,color=GRID); ax.set_facecolor("white")
for s in ["top","right"]: ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=10.5, loc="upper right")
header(fig, "Four days out of 251 carried a chunk of the whole year",
       "How much of the past year's price action landed on the 4 earnings-reaction days (1.6% of trading days).",
       "Data: stockanalysis.com daily closes (dividend-adjusted), 2025-06-27 to 2026-06-26. Illustrative 5-stock sample, not a market-wide claim.")
fig.savefig(f"{OUT}/chart2_share_of_year.png", facecolor="white"); plt.close(fig)
print("done", os.listdir(OUT)[:3])
