import matplotlib
from matplotlib import ticker
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline



def read_and_add_method(file_path, method_name):
    df = pd.read_csv(file_path)
    if method_name == 'ChaoticOSA':
        method_name = 'COSA'
    if method_name == 'WDNMN':
        method_name = 'WDNS'
    df['method'] = method_name  # 添加新列记录算法名
    return df

def parallel_plot(df,cols,rank_attr,cmap='Spectral',spread=False,curved=0.1,curvedextend=0.05):
    '''Produce a parallel coordinates plot from pandas dataframe with line colour with respect to a column.
    Required Arguments:
        df: dataframe
        cols: columns to use for axes
        rank_attr: attribute to use for ranking
    Options:
        cmap: Colour palette to use for ranking of lines
        spread: Spread to use to separate lines at categorical values
        curved: Spline interpolation along lines
        curvedextend: Fraction extension in y axis, adjust to contain curvature
    Returns:
        x coordinates for axes, y coordinates of all lines'''
    colmap = matplotlib.cm.get_cmap(cmap)
    cols = cols + [rank_attr]

    fig, axes = plt.subplots(1, len(cols)-1, sharey=False, figsize=(3*len(cols)+3,5))#绘制三个子图
    valmat = np.ndarray(shape=(len(cols),len(df)))#定义需要绘制曲线的数组有df行，cols列
    x = np.arange(0,len(cols),1)#貌似没什么用,有3列那么x=[0,1,2]
    ax_info = {}
    for i,col in enumerate(cols):#归一化数据
        vals = df[col]
        if (vals.dtype == float) & (len(np.unique(vals)) > 20):
            minval = np.min(vals)
            maxval = np.max(vals)
            rangeval = maxval - minval#区间长度
            vals = np.true_divide(vals - minval, maxval-minval)#归一化处理vals-minval/maxval-minval除法运算
            nticks = 5
            tick_labels = [round(minval + i*(rangeval/nticks),4) for i in range(nticks+1)]
            ticks = [0 + i*(1.0/nticks) for i in range(nticks+1)]
            valmat[i] = vals
            ax_info[col] = [tick_labels,ticks]
        else:
            vals = vals.astype('category')#假如是目录型
            cats = vals.cat.categories
            c_vals = vals.cat.codes
            minval = 0
            maxval = len(cats)-1
            if maxval == 0:
                c_vals = 0.5
            else:
                c_vals = np.true_divide(c_vals - minval, maxval-minval)
            tick_labels = cats
            ticks = np.unique(c_vals)
            ax_info[col] = [tick_labels,ticks]
            if spread is not None:
                offset = np.arange(-1,1,2./(len(c_vals)))*2e-2
                np.random.shuffle(offset)
                c_vals = c_vals + offset
            valmat[i] = c_vals
            
    extendfrac = curvedextend if curved else 0.05  
    for i,ax in enumerate(axes):
        for idx in range(valmat.shape[-1]):
            if curved:
                x_new = np.linspace(0, len(x), len(x)*20)
                a_BSpline = make_interp_spline(x, valmat[:,idx],k=3,bc_type='clamped')
                y_new = a_BSpline(x_new)
                ax.plot(x_new,y_new,color=colmap(valmat[-1,idx]),alpha=0.5)
            else:
                ax.plot(x,valmat[:,idx],color=colmap(valmat[-1,idx]),alpha=0.5)
        ax.set_ylim(0-extendfrac,1+extendfrac)
        ax.set_xlim(i,i+1)
    
    for dim, (ax,col) in enumerate(zip(axes,cols)):
        ax.xaxis.set_major_locator(ticker.FixedLocator([dim]))
        ax.yaxis.set_major_locator(ticker.FixedLocator(ax_info[col][1]))
        ax_info[col][0] = [int(label) for label in ax_info[col][0]]#y标签下取整
        # ax.set_yticklabels(ax_info[col][0])

        ax.set_xticklabels([cols[dim]])
    
    
    plt.subplots_adjust(wspace=0)
    norm = matplotlib.colors.Normalize(0,1)#*axes[-1].get_ylim())
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    # print(ax_info[rank_attr][0])
    # exit()
    cbar = plt.colorbar(sm,pad=0,ticks=ax_info[rank_attr][1],extend='both',extendrect=True,extendfrac=extendfrac)
    #if curved:
        #cbar.ax.set_ylim(0-curvedextend,1+curvedextend)
    cbar.ax.set_yticklabels(ax_info[rank_attr][0])
    # cbar.ax.set_xlabel(rank_attr)
    # ax.set_position([0, 0, 1, 0.9])  # Adjust the position of the axes
    plt.show()
            
    return x,valmat

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
        nsm = np.load(os.path.join(path, nsm_fn))
        Bs.append(B)
        NSMs.append(nsm)

# sort Bs by NSMs
Bs = [B for _, B in sorted(zip(NSMs, Bs))]
NSMs = sorted(NSMs)


# Select the first ten, middle ten, and last ten elements
Bs = Bs[:10] + Bs[len(Bs)//2-5:len(Bs)//2+5] + Bs[-10:]
NSMs = NSMs[:10] + NSMs[len(NSMs)//2-5:len(NSMs)//2+5] + NSMs[-10:]

# # select the first 2 Bs and NSMs
# Bs = Bs[-2:]
# NSMs = NSMs[-2:]

# select the first and the last
# Bs = Bs[:1] + Bs[-1:]
# NSMs = NSMs[:1] + NSMs[-1:]

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



parallel_plot(df, [f"dim{i+1}" for i in range(df.shape[1]-1)], 'nsm', cmap='Spectral', spread=False, curved=0.1, curvedextend=0.05)

