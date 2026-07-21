import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT="/sessions/beautiful-eloquent-ritchie/mnt/outputs"
INK="#0F1B2D"; GRID="#E6EAEF"; MUTE="#5A6470"
RED="#D9463F"; GREEN="#2FA84F"
plt.rcParams.update({"font.family":"DejaVu Sans","text.color":INK,"axes.edgecolor":"#9AA3AE",
                     "axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK})

fig,ax=plt.subplots(figsize=(9.6,7.0),dpi=150)
fig.subplots_adjust(top=0.795,bottom=0.10,left=0.085,right=0.965)

x=[0,1]; vals=[16,8]; cols=[RED,GREEN]; tot=24
ax.bar(x,vals,width=0.60,color=cols,edgecolor="white",lw=1.0,zorder=3)

for xi,v in zip(x,vals):
    ax.text(xi,v+0.30,str(v),ha="center",va="bottom",fontsize=34,fontweight="bold",color=INK)
    ax.text(xi,v/2,f"{round(100*v/tot)}%",ha="center",va="center",fontsize=15,fontweight="bold",color="white")

ax.set_xticks(x); ax.set_xticklabels(["Stock fell","Stock rose"],fontsize=13.5)
ax.set_ylabel("Number of reports (of the 24 that beat)",fontsize=11.5)
ax.set_ylim(0,19); ax.set_xlim(-0.7,1.7)
ax.set_yticks([0,4,8,12,16])
ax.set_axisbelow(True); ax.grid(True,axis="y",color=GRID); ax.set_facecolor("white")
for s in ["top","right"]: ax.spines[s].set_visible(False)

fig.text(0.085,0.945,"They beat estimates 24 times. The stock fell on 16.",fontsize=19,fontweight="bold",ha="left",va="top")
fig.text(0.085,0.878,"Magnificent 7, last four quarters. The next-day move after each report that topped EPS estimates.",
         fontsize=11.5,color=MUTE,ha="left",va="top")
fig.text(0.085,0.022,"Data: Yahoo Finance next-day moves; consensus vs reported EPS (CoinCodex / company filings). Alphabet's April report excluded.",
         fontsize=8.6,color="#8A929C",ha="left",va="bottom")
fig.savefig(f"{OUT}/chart4_beats_updown.png",facecolor="white"); plt.close(fig)
print("saved chart4_beats_updown.png  fell=16 rose=8 of 24")
