# the file is used to visualize the 2d lattices' NSM value

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from lattice_utils import *
from itertools import product
import concurrent.futures
from tqdm import tqdm

def _parallel_estimate(args):
    angle, ratio = args
    B = np.array([[1, 0], [ratio*np.cos(angle), ratio*np.sin(angle)]])
    B = ORTH(RED(B))
    mean, var = estimate_NSM(B)
    return [angle, ratio, mean]

def generate_2d_lattice(max_angle, max_ratio):
    assert max_angle > 0 and max_ratio > 1
    assert max_angle <= np.pi/2
    # generate a grid of points in [0, max_angle] x [1, max_ratio]
    angles = np.linspace(0.0001, max_angle, 10)
    ratios = np.linspace(1, max_ratio, 10)
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        total_tasks = len(angles) * len(ratios)
        results = list(tqdm(executor.map(_parallel_estimate, product(angles, ratios)), total=total_tasks))

    data_points = [r for r in results if r is not None]
    return np.array(data_points)

def visualize_3d_data(data, title, xlabel, ylabel, zlabel):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='r', marker='o')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_zlim(bottom=0.080, top=0.1)
    plt.show()

def visualize_higher_dimension_lattice(data):
    pass

# fisrt get data points
# data = generate_2d_lattice(np.pi/2, 10)
data = np.load("data.npy")

# save the data points
np.save("data.npy", data)

# then visualize the data points
visualize_3d_data(data, title="NSM of 2D Lattices", xlabel="Angle", ylabel="Ratio", zlabel="NSM")