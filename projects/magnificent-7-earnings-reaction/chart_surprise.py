import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, os

OUT="/sessions/beautiful-eloquent-ritchie/mnt/Trump Q1 trades"
# (EPS surprise %, next-day reaction %) per stock; clean/operating surprise. GOOGL Apr excluded (one-time $37B gain, no clean number)
DATA={
 "Meta":     [(20.61,11.25),(7.9,-11.33),(8.16,10.40),(9.9,-8.55)],
 "Microsoft":[(8.31,3.95),(12.84,-2.92),(6.15,-9.99),(5.17,-3.93)],
 "Amazon":   [(28.24,-8.27),(24.20,9.58),(-1.02,-5.55),(-5.5,0.77)],
 "Alphabet": [(7.44,1.02),(25.33,2.52),(9.73,-0.54)],
 "Tesla":    [(0.70,-8.20),(-7.41,2.28),(9.94,-3.45),(15.85,-3.56)],
 "Nvidia":   [(3.96,-0.79),(4.00,-3.15),(5.19,-5.46),(6.25,-1.77)],
 "Apple":    [(9.03,-2.50),(4.52,-0.38),(6.74,0.46),(3.08,3.24)],
}
COL={"Meta":"#1F6FEB","Microsoft":"#00A3A3","Amazon":"#E8623A","Alphabet":"#7A5AF8",
     "Tesla":"#E4406F","Nvidia":"#2FA84F","Apple":"#8A929C"}
INK="#0F1B2D"; GRID="#E6EAEF"
plt.rcParams.update({"font.family":"DejaVu Sans","text.color":INK,"axes.edgecolor":"#9AA3AE",
                     "axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK})
xs=[x for v in DATA.values() for x,_ in v]; ys=[y for v in DATA.values() for _,y in v]

fig,ax=plt.subplots(figsize=(11.6,7.0),dpi=140)
fig.subplots_adjust(top=0.80,bottom=0.115,left=0.075,right=0.975)
# quadrant guides
ax.axvline(0,color="#B8BFC9",lw=1.2); ax.axhline(0,color="#B8BFC9",lw=1.2)
ax.axhspan(-14,0,xmin=0.225,color="#E8623A",alpha=0.05)   # beat-but-fell region (x>=0, y<0)
# trend line
m,b=np.polyfit(xs,ys,1); r=np.corrcoef(xs,ys)[0,1]
xr=np.array([-9,31]); ax.plot(xr,m*xr+b,ls=(0,(6,4)),color="#5A6470",lw=1.6)
ax.text(18.5,m*18.5+b+0.7,f"barely any link  (r = {r:.1f})",ha="left",va="bottom",fontsize=10,color="#5A6470",fontstyle="italic")
# points
for name,pts in DATA.items():
    ax.scatter([p[0] for p in pts],[p[1] for p in pts],s=95,color=COL[name],edgecolor="white",lw=1.1,label=name,zorder=3)
# quadrant labels
ax.text(29,-12.6,"beat, but the stock FELL",ha="right",va="bottom",fontsize=11,color="#B23A1B",fontweight="bold")
ax.text(-8.3,12.4,"missed, but the stock ROSE",ha="left",va="top",fontsize=11,color="#5A6470",fontweight="bold")
ax.set_xlabel("Earnings surprise: how much EPS beat (right) or missed (left) estimates, %",fontsize=11.5)
ax.set_ylabel("Stock's next-day move (%)",fontsize=11.5)
ax.set_xlim(-9,31); ax.set_ylim(-14,14)
ax.set_axisbelow(True); ax.grid(True,color=GRID); ax.set_facecolor("white")
for s in ["top","right"]: ax.spines[s].set_visible(False)
ax.legend(frameon=False,fontsize=10,loc="lower left",ncol=2,handletextpad=0.2,columnspacing=1.0)
fig.text(0.075,0.95,"Beating estimates barely moved the stock",fontsize=18.5,fontweight="bold",ha="left",va="top")
fig.text(0.075,0.887,"Magnificent 7, last four quarters. Each dot is one report: how much it beat/missed EPS vs how the stock moved next day.",
         fontsize=11.3,color="#5A6470",ha="left",va="top")
fig.text(0.075,0.028,"Data: Yahoo Finance daily moves; consensus vs reported EPS (CoinCodex / company filings). Operating EPS used where one-time items distort the headline.",
         fontsize=8.4,color="#8A929C",ha="left",va="bottom")
fig.savefig(f"{OUT}/chart3_surprise_vs_reaction.png",facecolor="white"); plt.close(fig)
print("done; points:",len(xs),"corr:",round(r,3),"slope:",round(m,3))
