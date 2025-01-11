from fpylll import *
from lattice_utils import *
from tqdm import tqdm

class Lattice_Optimizer:

    
    def optimize(n):
        '''
        Randomly generate a generator matrix for an n-dimensional lattice.
        Optimize the NSM of the lattice.

        :param n: the dimension of the lattice
        :return: the optimized generator matrix
        '''

        # TODO: put paramerters into a config file
        mu0 = 0.005
        v = 200
        T = 1000000
        T_r = 100

        B = ORTH(RED(GRAN(n, n)))
        V = np.prod(B.diagonal())
        B = B / V**(1/n)
        for t in tqdm(range(T)):
            last_B = B.copy()
            mu = mu0*v**(-t/T-1)
            z = URAN(n)
            y = z - CLP(B, z@B)
            e = np.dot(y, B)
            for i in range(n):
                for j in range(i):
                    B[i][j] = B[i][j] -mu*y[i]*e[j]

                B[i][i] = B[i][i] - mu*(y[i]*e[i] - np.linalg.norm(e)**2/(n*B[i][i]))
                # sanity check
                if B[i][i] < 0:
                    print("Sanity check failed. Early stopping.")
                    B = last_B
                    break
            if t % T_r == T_r-1:
                B = ORTH(RED(B))
                V = np.prod(B.diagonal())
                B = B / V**(1/n)

        return B
    def descent(B,n,mu0=0.005,v=200,T=1000000,T_r=100):
        '''
        Randomly generate a generator matrix for an n-dimensional lattice.
        Optimize the NSM of the lattice.

        :param n: the dimension of the lattice
        :return: the optimized generator matrix
        '''

        # TODO: put paramerters into a config file
        #mu0 = 0.005
        #v = 200
        #T = 1000000
        #T_r = 100

        B = ORTH(RED(B))
        V = np.prod(B.diagonal())
        B = B / V**(1/n)
        for t in tqdm(range(T)):
            last_B = B.copy()
            mu = mu0*v**(-t/T-1)
            z = URAN(n)
            y = z - CLP(B, z@B)
            e = np.dot(y, B)
            for i in range(n):
                for j in range(i):
                    B[i][j] = B[i][j] -mu*y[i]*e[j]

                B[i][i] = B[i][i] - mu*(y[i]*e[i] - np.linalg.norm(e)**2/(n*B[i][i]))
                # sanity check
                if B[i][i] < 0:
                    print("Sanity check failed. Early stopping.")
                    B = last_B
                    break
            if t % T_r == T_r-1:
                B = ORTH(RED(B))
                V = np.prod(B.diagonal())
                B = B / V**(1/n)

        return B


