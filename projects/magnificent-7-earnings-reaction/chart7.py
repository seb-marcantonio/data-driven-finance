import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np, os

OUT = "/sessions/beautiful-eloquent-ritchie/mnt/Trump Q1 trades"

# Magnificent 7, trailing 12 months (2025-07-01 -> 2026-06-26, 249 trading days), sorted by share of movement
labels   = ["Meta","Microsoft","Amazon","Alphabet","Tesla","Nvidia","Apple"]
avg_earn = [10.38, 5.20, 6.04, 3.51, 4.37, 2.79, 1.65]
avg_norm = [ 1.38, 1.13, 1.37, 1.30, 2.16, 1.71, 1.05]
abs_share= [10.9,  7.0,  6.7,  4.2,  3.2,  2.6,  2.5]
var_share= [33.6, 19.3, 20.3, 12.1,  5.1,  3.5,  3.1]

INK="#0F1B2D"; GRID="#E6EAEF"; EARN="#1F6FEB"; NORM="#C2C9D2"; RISK="#0B2C66"; ACCENT="#E8623A"
plt.rcParams.update({"font.family":"DejaVu Sans","text.color":INK,"axes.edgecolor":"#9AA3AE",
                     "axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK})
x = np.arange(len(labels)); w=0.4

def header(fig, title, subtitle, source):
    fig.text(0.062, 0.95, title, fontsize=18.5, fontweight="bold", ha="left", va="top")
    fig.text(0.062, 0.887, subtitle, fontsize=11.3, color="#5A6470", ha="left", va="top")
    fig.text(0.062, 0.035, source, fontsize=8.6, color="#8A929C", ha="left", va="bottom")

# ---------- Chart 1 ----------
fig, ax = plt.subplots(figsize=(12.2,6.8), dpi=140)
fig.subplots_adjust(top=0.80, bottom=0.135, left=0.08, right=0.975)
ax.bar(x-w/2, avg_earn, w, label="Earnings-reaction day", color=EARN)
ax.bar(x+w/2, avg_norm, w, label="Average normal day", color=NORM)
for i,(e,n) in enumerate(zip(avg_earn,avg_norm)):
    ax.text(x[i]-w/2, e+0.15, f"{e:.1f}", ha="center", va="bottom", fontsize=10, fontweight="bold", color=EARN)
    ax.text(x[i]+w/2, n+0.15, f"{n:.1f}", ha="center", va="bottom", fontsize=10, color="#6B7480")
    ax.text(x[i], max(e,n)+0.95, f"{e/n:.1f}x", ha="center", va="bottom", fontsize=11, fontweight="bold", color=ACCENT)
ax.set_ylabel("Average absolute one-day move (%)", fontsize=11.5)
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=11.5)
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0)); ax.set_ylim(0,13.2)
ax.set_axisbelow(True); ax.yaxis.grid(True,color=GRID); ax.set_facecolor("white")
for s in ["top","right"]: ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=11, loc="upper right")
header(fig, "An earnings day is not a normal day",
       "The Magnificent 7. Average size of a one-day move, trailing 12 months. Orange = how many times bigger an earnings day is.",
       "Data: Yahoo Finance daily closes (split/dividend-adjusted). Earnings reaction = the next session (all seven report after the close).")
fig.savefig(f"{OUT}/chart1_earnings_vs_normal.png", facecolor="white"); plt.close(fig)

# ---------- Chart 2 ----------
fig, ax = plt.subplots(figsize=(12.2,6.8), dpi=140)
fig.subplots_adjust(top=0.80, bottom=0.135, left=0.08, right=0.975)
ax.bar(x-w/2, abs_share, w, label="Share of total movement (sum of daily moves)", color=EARN)
ax.bar(x+w/2, var_share, w, label="Share of risk (variance: big days weigh more)", color=RISK)
for i,(a,v) in enumerate(zip(abs_share,var_share)):
    ax.text(x[i]-w/2, a+0.4, f"{a:.1f}%", ha="center", va="bottom", fontsize=9.8, fontweight="bold", color=EARN)
    ax.text(x[i]+w/2, v+0.4, f"{v:.0f}%", ha="center", va="bottom", fontsize=9.8, fontweight="bold", color=RISK)
ax.axhline(1.6, color=ACCENT, ls=(0,(5,4)), lw=1.8, label="1.6% = if the 4 earnings days were just normal days")
ax.set_ylabel("Share of the year in 4 earnings days (%)", fontsize=11.5)
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=11.5)
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0)); ax.set_ylim(0,38)
ax.set_axisbelow(True); ax.yaxis.grid(True,color=GRID); ax.set_facecolor("white")
for s in ["top","right"]: ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=10.3, loc="upper right")
header(fig, "Four days out of 249 carried a chunk of the whole year",
       "The Magnificent 7, trailing 12 months. How much of the year's price action landed on the 4 earnings days (1.6% of trading days).",
       "Data: Yahoo Finance daily closes (split/dividend-adjusted), 2025-07-01 to 2026-06-26. Alphabet's Sept antitrust jump is excluded (not earnings).")
fig.savefig(f"{OUT}/chart2_share_of_year.png", facecolor="white"); plt.close(fig)
print("done")
