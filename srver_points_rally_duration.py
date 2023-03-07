import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df_m = pd.read_csv(
    "tennis_MatchChartingProject/charting-m-points-from-2017.csv")
df_w = pd.read_csv(
    "tennis_MatchChartingProject/charting-w-points-from-2017.csv")

for (df, label) in [(df_m, "M"), (df_w, "F")]:
    # Check who wins the point
    df["svrWinsPoint"] = df["PtWinner"] == df["Svr"]
    # Restrict the data just to 1st service points, how long the rally was, and who won the point
    df_res = df[["1stIn", "rallyCount", "svrWinsPoint"]]
    df_res = df_res[df_res["1stIn"] == 1][["rallyCount", "svrWinsPoint"]]

    # make the data integers
    df_res = df_res.astype(int)

    # group by rally count
    df_rally_count = df_res.groupby("rallyCount").count()
    # you'll spot the server always wins 1 shot rallies, returner 2 shot rallies etc (this is what we were discussing re: data collection being important)
    t = df_rally_count.values[:, 0]
    X = []

    # look at the relative fraction of points won in (k+1) shots vs k and (k+2) shots.
    # I am weighting k and (k+2) 50% each. You'll notice this doesn't fully remove the oscillating effect, so you might want to look at other windowing methods for the 5th, 6th, 7th shots
    # I am combining them using a Beta distribution. (https://en.wikipedia.org/wiki/Beta_distribution)
    # I then use this distribution to determine confidence intervals for the frequencies of various shots (ppf is giving the percentiles, 5%, 50% and 95%)
    for (i, v) in enumerate(zip(t, t[1:], t[2:])):
        quantiles = stats.beta.ppf([0.05, 0.5, 0.95], v[1]+1, (v[0]+v[2])/2+1)
        if i % 2 == 0:
            quantiles = 1-quantiles[::-1]
        X.append(quantiles)
    X = np.array(X)
    plt.errorbar(np.arange(1, 16),
                 X[:15, 1], yerr=X[:15, 0]-X[:15, 1], fmt=".--", label=label)
    plt.hlines(.5, 0, 14)
plt.title("%age of pts won by the server by rally duration")
plt.xlabel("Rally Duration")
plt.xlim([1, 15])
plt.ylabel("Win %age")
plt.legend()
plt.show()
