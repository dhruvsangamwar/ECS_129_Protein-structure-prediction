import pandas as pd
import pdbCleanup
import numpy as np

df = pd.read_csv("degrees.csv")
print(df)

df = df.to_numpy()
print(df)
