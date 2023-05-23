import pandas as pd
# import numpy as np
# from distutils.util import strtobool
# from numpy import dtype


# NOTE: the dataset has bad data; auto conversion of dtypes does not work.
# df_dtype = {'match_id': str, 'Pt': np.int64, 'Set1': np.int64,
#                  'Set2': np.int64, 'Gm1': np.int64, 'Gm2': np.int64,
#                  'Pts': str, 'Gm#': str, 'TbSet': bool,
#                  'TB?': bool, 'TBpt': np.int64, 'Svr': np.int64,
#                  'Ret': np.int64, 'Serving': str, '1st': str,
#                  '2nd': str, 'Notes': str, '1stSV': bool,
#                  '2ndSV': bool, '1stIn': bool, '2ndIn': bool,
#                  'isAce': bool, 'isUnret': bool, 'isRallyWinner': bool,
#                  'isForced': bool, 'isUnforced': bool, 'isDouble': bool,
#                  'PtWinner': np.int64, 'isSvrWinner': bool, 'rallyCount': np.int64}
# df_converters = {'TbSet': strtobool, 'TB?': strtobool,}


def get_df(*args, **kwargs):
    # placeholder:
    df_frames = []
    for g in ["m", "w"]:
        for y in ["from-2017", "to-2016"]:
            df = pd.read_csv("tennis_MatchChartingProject/charting-{}-points-{}.csv".format(g, y),
                             encoding="ISO-8859-1",
                             *args, **kwargs)
            df_frames.append(df)
    df = pd.concat(df_frames)
    df = df.where(pd.notnull(df), None)

    return df

# %%

# %%
