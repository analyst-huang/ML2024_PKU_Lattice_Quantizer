import numpy as np
# from Grad_Method.algo.basic.lattice_utils import estimate_NSM

n = input("get data for ? dimensions: ")

path = "assets/" + n + "_dim_lattices"

# get all the files in the directory
import os
files = os.listdir(path)

# there are 2 types of files in the directory
# 1. files with the basis of the lattice, B_{data}_{index}.npy
# 2. files with the nsm of the lattice, nsm_{data}_{index}.npy

best_B = None
best_nsm = np.inf
for fn in files:
    if fn.startswith("B"):
        tmp = fn.split("_")
        nsm_fn = "nsm_" + "_".join(tmp[1:])
        B = np.load(os.path.join(path, fn))
        nsm = np.load(os.path.join(path, nsm_fn))
        if nsm < best_nsm:
            best_B = B
            best_nsm = nsm

print("Best basis matrix:")
print(best_B)
print("reestimated nsm:")

print("Best nsm:")
print(best_nsm)

    
