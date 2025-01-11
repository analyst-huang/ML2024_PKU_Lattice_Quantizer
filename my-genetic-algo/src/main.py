from gene import Gene
from gene_utils import *

def main():
    '''
    n = 2
    gene = Gene(n)
    best_matrix = gene.run()
    print("best matrix", best_matrix)
    print("NSM", estimate_NSM(best_matrix))
    visualize_lattice(best_matrix)
    '''
    
    n = 4# 矩阵维度
    best_nsm = float('inf')  # 初始化为正无穷
    best_matrix = None

    # 运行 100 次
    for i in range(10):
        gene = Gene(n)
        matrix = gene.run()
        nsm = estimate_NSM(matrix)

        print(f"Run {i + 1}: NSM = {nsm:.9f}")

        # 如果当前矩阵的 NSM 小于之前的最小值，则更新
        if nsm < best_nsm:
            best_nsm = nsm
            best_matrix = matrix

    # 输出最优结果
    print("\nBest Matrix:")
    print(best_matrix)
    print(f"Minimum NSM: {best_nsm:.9f}")

    # 可视化最优矩阵
    visualize_lattice(best_matrix)
    

if __name__ == "__main__":
    # main()
    B_2 = np.array([[4,0], [2, 2*np.sqrt(3)]])
    print("NSM", estimate_NSM(B_2))
    main()