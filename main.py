import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


df_m = pd.read_csv(
    "tennis_MatchChartingProject/charting-m-points-from-2017.csv", encoding="ISO-8859-1")
df_w = pd.read_csv(
    "tennis_MatchChartingProject/charting-w-points-from-2017.csv", encoding="ISO-8859-1")

for (df, label) in [(df_m, "M"), (df_w, "F")]:

