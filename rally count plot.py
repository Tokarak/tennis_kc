import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_m = pd.read_csv(
    "tennis_MatchChartingProject/charting-m-points-from-2017.csv", encoding="ISO-8859-1")
df = df_m[["rallyCount", "PtWinner"]]
# df=df_m[df_m["isForced"]==0][["rallyCount", "PtWinner"]]
rallyct = df.groupby("rallyCount").count().astype(int, errors="ignore")
t = rallyct.values[:, 0]
plt.plot(t)
plt.show()
X = []
for (i, v) in enumerate(zip(t, t[1:])):
    X.append(v[1] / v[0])
X = np.array(X)
plt.plot(X[4:30])
plt.show()
