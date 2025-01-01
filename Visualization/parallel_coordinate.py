import numpy as np
import pandas as pd
import plotly.express as px

# # Generate random data with 15 features and 50 samples
# data1 = np.random.rand(5)
# data2 = np.random.rand(5)
# data3 = np.random.rand(5)

# df = pd.DataFrame([data1, data2, data3],
#                   columns=[f"dim{i+1}" for i in range(5)])
# df["label"] = ["data1", "data2", "data3"]
# df["label_numeric"] = [0, 1, 2]

# fig = px.parallel_coordinates(
#     df,
#     color="label_numeric",
#     dimensions=[f"dim{i+1}" for i in range(5)],
#     color_continuous_scale=px.colors.diverging.Tealrose,
#     color_continuous_midpoint=2,
# )
# fig.show()

def visualize_lattice(Bs, NSMs):
    # Bs is a list of B matrices
    # Bs = [B1, B2, B3, ...]
    df = pd.DataFrame()
    for i, B,nsm in enumerate(zip(Bs,NSMs)):
        # B is a matrix of shape (n, n)
        # each row of B is a vector of length n
        # we need to convert B to a DataFrame, with each row being a vector and class label as the last column with value i
        df_temp = pd.DataFrame(B)
        df_temp["nsm"] = nsm
        df_temp.columns = [f"dim{i+1}" for i in range(df_temp.shape[1]-1)] + ["nsm"]
        df = pd.concat([df, df_temp], axis=0)
    fig = px.parallel_coordinates(
        df,
        color="label",
        dimensions=[f"dim{i+1}" for i in range(df.shape[1]-1)]+["nsm"],
        color_continuous_scale=px.colors.diverging.Tealrose,
        color_continuous_midpoint=len(Bs)//2,
    )
    fig.show()
    
B1 = [[1,2,3], [4,5,6], [7,8,9]]
B2 = [[9,8,7], [6,5,4], [3,2,1]]
visualize_lattice([B1, B2])

