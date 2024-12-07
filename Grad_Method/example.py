import numpy as np
# n , t = 4, 0
# B = np.eye(n)
# B_0 = np.eye(n)
# z = np.array([0.6, 0.6, 0.0, 0.0])
# z_0 = z.copy()
# u = np.array([1,1,0,0])
# e = (z-u).dot(B)
# print(e)

# def g(B, e):
#     assert B.shape[0] == B.shape[1] and len(B.shape) == 2
#     n = B.shape[0]
#     return (1/n) * np.prod(np.diag(B))**(-2/n) * np.linalg.norm(e)**2

# print(g(B, e))

# def B_grad(B, e, z, u):
#     assert B.shape[0] == B.shape[1] and len(B.shape) == 2
#     n = B.shape[0]
#     V = np.prod(np.diag(B))
#     y = z-u
#     def f(i, j):
#         if i < j:
#             return 0
#         elif i == j:
#             return (2/n) * V**(-2/n) * (y[i]*e[j]-np.linalg.norm(e)**2/n*B[i,i])
#         else:
#             return 2/n * V**(-2/n) * y[i]*e[j]
#     return np.array([[f(i, j) for j in range(n)] for i in range(n)])

# dB = B_grad(B, e, z, u)
# print(dB)
# print(B - 0.01* dB)

from utils import URAN, GRAN
from matplotlib import pyplot as plt
N_Matrix = [GRAN(2,2) for i in range(1000)]
# draw the distribution of each element in the matrix and the theorectical distribution



