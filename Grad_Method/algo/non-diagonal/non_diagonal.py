from Lattice_Optimizer import Lattice_Optimizer
from lattice_utils import *
from tqdm import tqdm
import numpy as np
import scipy
def op(n):
    for k in range(2,n-1):
        print("k=",k)
        t1=k
        t2=n-t1
        print("Optimizing B1")
        B1=Lattice_Optimizer.optimize(t1)
        print("Optimizing B2")
        B2=Lattice_Optimizer.optimize(t2)
        V1=np.linalg.det(B1)
        V2=np.linalg.det(B2)
        print("Estimating NSM of B1 and B2")
        G1=estimate_NSM(B1)
        G2=estimate_NSM(B2)
        B1=(B1/(V1**(1/t1)))/(G1**(1/2))
        B2=(B2/(V2**(1/t2)))/(G2**(1/2))
        B=scipy.linalg.block_diag(B1,B2)
        H=GRAN(t2, t1)
        for i in range(t1,n):
            for j in range(t2,n):
                B[i][j]=H[i-t1][j-t2]
    
        mu0 = 0.005
        v = 200
        T = 1000000
        T_r = 100

    
        for t in tqdm(range(T)):
            last_B = B.copy()
            mu = mu0*v**(-t/T-1)
            z = URAN(n)
            y = z - CLP(B, z@B)
            e = np.dot(y, B)
            for i in range(t1,n):
                for j in range(0,t1):
                    B[i][j] = B[i][j] -mu*y[i]*e[j]
        B=ORTH(RED(B))
        print(B)
        print(estimate_NSM(B))
        print("Optimization Done")
    return B

op(4)
op(4)
op(4)