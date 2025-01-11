import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.interpolate import griddata 


# load data_points.npy
data_points = np.load("data_points.npy")

def visualize_3d_data(data, title, xlabel, ylabel, zlabel):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Scatter plot of the data points
    # ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='r', marker='o', label='Data points')
    
    # Set labels and title
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_zlim(bottom=0.080, top=0.1)

    # select data points with NSM < 0.1
    data = data[data[:, 2] < 0.09]

    # select data points with NSM > 0.08
    data = data[data[:, 2] > 0.081]

    # select data point with angle > 0.1
    data = data[data[:, 0] > 0.05]
    
    
    # Fit datapoints to a 3D surface
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]
    
    # Create a grid for interpolation
    xi = np.linspace(x.min(), x.max(), 50)
    yi = np.linspace(y.min(), y.max(), 50)
    xi, yi = np.meshgrid(xi, yi)
    
    # Interpolate z values over the grid
    zi = griddata((x, y), z, (xi, yi), method='linear')
    
    # Plot the surface
    surf = ax.plot_surface(xi, yi, zi, cmap='viridis', alpha=0.7)
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)  # Add color bar for reference
    
    plt.legend()
    plt.show()

visualize_3d_data(data_points, title="NSM of 2D Lattices", xlabel="Angle", ylabel="Ratio", zlabel="NSM")