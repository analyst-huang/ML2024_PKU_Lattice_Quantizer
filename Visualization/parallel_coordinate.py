import numpy as np
import pandas as pd
import plotly.express as px

def visualize_lattice(Bs, NSMs):
    # Bs is a list of B matrices
    # Bs = [B1, B2, B3, ...]
    df = pd.DataFrame()
    # get the max and min of NSMs
    min_nsm = min(NSMs)
    max_nsm = max(NSMs)

    for  B,nsm in zip(Bs,NSMs):
        # B is a matrix of shape (n, n)
        # each row of B is a vector of length n
        # we need to convert B to a DataFrame, with each row being a vector and class label as the last column with value i
        df_temp = pd.DataFrame(B)
        df_temp["nsm"] = nsm
        df_temp.columns = [f"dim{i+1}" for i in range(df_temp.shape[1]-1)] + ["nsm"]
        df = pd.concat([df, df_temp], axis=0)
    fig = px.parallel_coordinates(
        df,
        color="nsm",
        dimensions=[f"dim{i+1}" for i in range(df.shape[1]-1)]+["nsm"],
        color_continuous_scale=px.colors.diverging.Tealrose,
        color_continuous_midpoint=(min_nsm + max_nsm) / 2,  # Scale color to nsm value
    )
    fig.show()
    

n = input("get data for ? dimensions: ")

path = "../assets/" + n + "_dim_lattices"

# get all the files in the directory
import os
files = os.listdir(path)

# there are 2 types of files in the directory
# 1. files with the basis of the lattice, B_{data}_{index}.npy
# 2. files with the nsm of the lattice, nsm_{data}_{index}.npy

Bs = []
NSMs = []

for fn in files:
    if fn.startswith("B"):
        tmp = fn.split("_")
        nsm_fn = "nsm_" + "_".join(tmp[1:])
        B = np.load(os.path.join(path, fn))
        # scale the elements of B to be in the range [0, 1]
        B = (B - B.min()) / (B.max() - B.min())
        nsm = np.load(os.path.join(path, nsm_fn))
        Bs.append(B)
        NSMs.append(nsm)

# sort Bs by NSMs
Bs = [B for _, B in sorted(zip(NSMs, Bs))]
NSMs = sorted(NSMs)

Bs = Bs[:1]
NSMs = NSMs[:1]
visualize_lattice(Bs, NSMs)



