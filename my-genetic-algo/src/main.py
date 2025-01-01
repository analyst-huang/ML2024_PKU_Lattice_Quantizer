from gene import Gene
from gene_utils import *

def main():
    n = 2
    gene = Gene(n)
    best_matrix = gene.run()
    print("best matrix", best_matrix)
    print("NSM", estimate_NSM(best_matrix))
    visualize_lattice(best_matrix)

if __name__ == "__main__":
    # main()
    B_2 = np.array([[4,0], [2, 2*np.sqrt(3)]])
    print("NSM", estimate_NSM(B_2))
