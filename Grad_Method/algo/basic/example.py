from fpylll import *
import numpy as np
from Lattice_Optimizer import Lattice_Optimizer
from lattice_utils import *
import matplotlib.pyplot as plt

# visualize_lattice(Lattice_Optimizer.optimize(2))
# converged 2 dimensional lattice.
# visualize_lattice(np.array([[ 0.98375456  ,0.        ], 
#  [-0.42347557 , 1.01651371]]))

# estimate NSM
# B = np.array([[1,0], [1/2, np.sqrt(3)/2]])
# B = np.array([[ 0.87679027 , 0.        ], [-0.13371271 , 1.14052361]])
# B = np.array([[.109868411347E+01, .000000000000E+00, .000000000000E+00],
#                 [-.455089860701E+00, .999999999939E+00, .000000000000E+00],
#                 [-.188504392394E+00, -.585786437865E+00, .910179720963E+00]])
# mean, var = estimate_NSM(B)
# print(mean, '+-', np.sqrt(var))

# test whether e is uniformly distributed
# B = np.array([[1,0], [1/2, np.sqrt(3)/2]])
# points = []
# for i in range(100000):
#     z = URAN(2)
#     u = CLP(B, np.dot(z, B))
#     e = np.dot(z-u, B)
#     points.append(e)

# points = np.array(points)
# plt.scatter(points[:, 0], points[:, 1], s=1, c='blue')
# plt.axhline(0, color='black', lw=0.5)
# plt.axvline(0, color='black', lw=0.5)
# plt.xlim(-2,2)
# plt.ylim(-2,2)

# points = []
# for i in range(-10, 11):
#     for j in range(-10, 11):
#         coord = np.array([i, j])
#         points.append(np.dot(coord, B))

# points = np.array(points)

# plt.scatter(points[:, 0], points[:, 1], s=1, c='red')

# plt.show()

# best_Bs = []

# for i in range(10):
#     B = Lattice_Optimizer.optimize(2)
#     nsm, _ = estimate_NSM(B)
#     best_Bs.append((B, nsm))


# best_Bs = sorted(best_Bs, key=lambda x: x[1])
# for B, nsm in best_Bs:
#     print(B)
#     print(nsm)
#     print('*'*20)

# best_Bs = np.array(best_Bs)
# save_path = 'best_lattices.npy'
# np.save(save_path, best_Bs)

# # a try for dimension 8
# B = Lattice_Optimizer.optimize(8)
# nsm, _ = estimate_NSM(B)
# print(B)
# print(nsm)

# test new CLP algorithm
B = np.array([[1,0,0, 0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
# B = np.array([[1,1/2], [0, np.sqrt(3)/2]])
r = np.array([0,0,0,1])
u = CLP(B, r)
print(u)





