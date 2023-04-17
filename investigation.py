import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    "tennis_MatchChartingProject/charting-m-points-from-2017.csv", encoding="ISO-8859-1", nrows=5000)
print(df.shape[0])

df_fs = df[df["1stIn"] == 1]
df_ss = df[df["2ndIn"] == 1]
print("Probability of first serve being in:", df_fs.shape[0]/df.shape[0])
print("Probability of second serve being in, given that the first serve is out:", df_ss.shape[0]/(df.shape[0]-df_fs.shape[0]))
# for dfn, label in [(df_fs, "df_fs"), (df_ss, "df_ss")]:
#    print("Probability of server winning in", label, "is", dfn[dfn["isSvrWinner"]==1].shape[0]/dfn.shape[0])
s
