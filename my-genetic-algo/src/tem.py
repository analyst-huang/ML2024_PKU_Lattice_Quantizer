from gene import Gene
from gene_utils import *

B_2 = np.array([[0.22541393*2,0],[-0.05794181*2,2]])
               
print("NSM", estimate_NSM(B_2))
visualize_lattice(B_2)

B_1 = np.array([[4,0], [2, 2*np.sqrt(3)]])
print("NSM", estimate_NSM(B_1))
visualize_lattice(B_1)