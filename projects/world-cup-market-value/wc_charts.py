#!/usr/bin/env python3
"""Two separate World Cup value charts: players and teams (2014, 2018, 2022)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK="#0F172A"; SUB="#64748B"; GRID="#E2E8F0"
BEFORE="#94A3B8"; AFTER="#059669"; LINE="#CBD5E1"; PILLBG="#ECFDF5"
plt.rcParams["font.family"]="DejaVu Sans"

def draw(ax, entries, xlim, gridvals, namex_off, valoff, pillx):
    XMIN, XMAX = xlim
    positions, y = [], 0.0
    for e in entries:
        if e[0] == "__h__":
            y -= 0.7; positions.append((y, e)); y -= 1.0
        else:
            positions.append((y, e)); y -= 1.0
    ys = [p[0] for p in positions]
    ax.set_xlim(XMIN, XMAX); ax.set_ylim(min(ys) - 0.9, max(ys) + 0.8)
    for gx in gridvals:
        ax.plot([gx, gx], [min(ys) - 0.6, max(ys) + 0.4], color=GRID, lw=1, zorder=0)
        ax.text(gx, min(ys) - 0.85, "€0" if gx == 0 else f"€{gx:,}m",
                ha="center", va="top", fontsize=9, color=SUB)
    for yy, e in positions:
        if e[0] == "__h__":
            ax.text(XMIN + namex_off, yy, e[1], ha="left", va="center",
                    fontsize=13, fontweight="bold", color=INK)
            ax.plot([XMIN + namex_off, gridvals[-1]], [yy - 0.52, yy - 0.52],
                    color=GRID, lw=1.2, zorder=0)
            continue
        name, meta, b, a, approx, pct = e
        pre = "~" if approx else ""
        ax.plot([b, a], [yy, yy], color=LINE, lw=3, solid_capstyle="round", zorder=1)
        ax.scatter([b], [yy], s=140, color=BEFORE, zorder=3, edgecolors="white", linewidths=1.4)
        ax.scatter([a], [yy], s=185, color=AFTER, zorder=3, edgecolors="white", linewidths=1.4)
        ax.text(XMIN + namex_off, yy + 0.17, name, ha="left", va="center",
                fontsize=12.5, fontweight="bold", color=INK)
        ax.text(XMIN + namex_off, yy - 0.21, meta, ha="left", va="center", fontsize=9.5, color=SUB)
        ax.text(b - valoff, yy, f"{pre}€{b:,}m", ha="right", va="center", fontsize=10, color=SUB)
        ax.text(a + valoff, yy, f"{pre}€{a:,}m", ha="left", va="center",
                fontsize=10.5, fontweight="bold", color=AFTER)
        ax.text(pillx, yy, f"+{pct}", ha="right", va="center", fontsize=11.5,
                fontweight="bold", color=AFTER,
                bbox=dict(boxstyle="round,pad=0.32", fc=PILLBG, ec=AFTER, lw=1.1))
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])

def legend(ax):
    ax.scatter([], [], s=140, color=BEFORE, edgecolors="white", linewidths=1.4, label="Before World Cup")
    ax.scatter([], [], s=185, color=AFTER, edgecolors="white", linewidths=1.4, label="After World Cup")
    ax.legend(loc="lower right", bbox_to_anchor=(0.996, 1.005), ncol=2, frameon=False,
              fontsize=10.5, handletextpad=0.4, columnspacing=1.3)

# ---------------- Players ----------------
players = [
    ("Azzedine Ounahi", "Morocco · 2022", 3.5, 15, False, "329%"),
    ("Keylor Navas", "Costa Rica · 2014", 4, 10, False, "150%"),
    ("James Rodríguez", "Colombia · 2014", 35, 60, False, "71%"),
    ("Enzo Fernández", "Argentina · 2022", 35, 55, False, "57%"),
    ("Harry Maguire", "England · 2018", 25, 35, False, "40%"),
    ("Cody Gakpo", "Netherlands · 2022", 45, 60, False, "33%"),
    ("Joško Gvardiol", "Croatia · 2022", 60, 75, False, "25%"),
]
figP, axP = plt.subplots(figsize=(11, 8.6), dpi=190)
figP.subplots_adjust(left=0.005, right=0.995, top=0.80, bottom=0.10)
draw(axP, players, (-37, 104), [0, 20, 40, 60, 80], 2, 2, 96)
legend(axP)
figP.text(0.005, 0.955, "How much does a great World Cup add to a player's value?",
          fontsize=20, fontweight="bold", color=INK)
figP.text(0.005, 0.905, "Transfermarkt market value, before the tournament vs after",
          fontsize=12.5, color=SUB)
figP.text(0.005, 0.028,
          "Source: Transfermarkt market value history (EUR). Before = last valuation before the tournament; after = first valuation after.",
          fontsize=9, color=SUB)
figP.savefig("wc_players.png", dpi=190, facecolor="white")
print("saved wc_players.png")

# ---------------- Teams ----------------
teams = [
    ("__h__", "2014 World Cup  ·  Brazil"),
    ("Germany", "Winner", 538, 570, False, "5.9%"),
    ("Argentina", "Runner-up", 392, 410, False, "4.6%"),
    ("Netherlands", "3rd place", 208, 215, False, "3.4%"),
    ("Brazil", "4th place", 468, 472, False, "1%"),
    ("__h__", "2018 World Cup  ·  Russia"),
    ("Croatia", "Runner-up", 364, 413, False, "13.5%"),
    ("France", "Winner", 1080, 1200, False, "11.1%"),
    ("England", "4th place", 874, 915, False, "4.7%"),
    ("Belgium", "3rd place", 754, 789, False, "4.6%"),
    ("__h__", "2022 World Cup  ·  Qatar"),
    ("Morocco", "4th place", 251, 291, False, "15.9%"),
    ("Argentina", "Winner", 633, 710, False, "12.2%"),
    ("Croatia", "3rd place", 377, 400, False, "6.1%"),
    ("France", "Runner-up", 1000, 1060, True, "6.0%"),
]
figT, axT = plt.subplots(figsize=(12.5, 15), dpi=180)
figT.subplots_adjust(left=0.004, right=0.996, top=0.905, bottom=0.05)
draw(axT, teams, (-560, 1710), [0, 300, 600, 900, 1200], 18, 22, 1645)
legend(axT)
figT.text(0.004, 0.963, "How much does a great World Cup add to a whole squad?",
          fontsize=20, fontweight="bold", color=INK)
figT.text(0.004, 0.935, "Total squad value of the final four, before the tournament vs after",
          fontsize=12.5, color=SUB)
figT.text(0.004, 0.030,
          "Source: Transfermarkt market values (EUR), total squad value before vs after. "
          "2014 totals reconstructed by summing player values at the 22 Jul 2014 revaluation.",
          fontsize=9, color=SUB)
figT.text(0.004, 0.017,
          "France 2022 rounded to 3 significant figures.",
          fontsize=9, color=SUB)
figT.savefig("wc_teams.png", dpi=180, facecolor="white")
print("saved wc_teams.png")
