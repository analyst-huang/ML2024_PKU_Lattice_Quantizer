import numpy as np  
from fpylll import *
from gene_utils import *
from tqdm import tqdm
#import sys
#sys.path.append('../../Grad_Method/algo/basic')
from Lattice_Optimizer import Lattice_Optimizer

class Gene:
    def __init__(self, n):
        self.n = n
        self.population_size = 40
        self.generations = 60
        self.mutation_rate = 0.2
        self.matrices = self.initialize_population()

    def initialize_population(self):
        return [ORTH(RED(GRAN(self.n))) for _ in range(self.population_size)]
        

    def fitness(self, nsm):
        return np.exp(-nsm)

    def mutate(self, matrix):
        # decide wheter to mutate
        if np.random.rand() > self.mutation_rate:
            return matrix
        
        mutated_matrix = Lattice_Optimizer.descent(matrix,n=self.n,mu0=0.005,T=1000)
        return normalize(mutated_matrix)

    def reproduce(self, parent1, parent2):
        split_point = np.random.randint(1, self.n)
        child = np.concatenate((parent1[:split_point], parent2[split_point:]))
        # randomly disturb rows of the child matrix
        child = self.mutate(child)
        np.random.shuffle(child)
        return ORTH(RED(child))

    def run(self):
        for generation in tqdm(range(self.generations)):
            nsm_values = [estimate_NSM(matrix, T=1000) for matrix in self.matrices]
            fitness_values = [self.fitness(nsm) for nsm in nsm_values]

            # Selection and reproduction logic
            new_matrices = []
            for _ in range(self.population_size // 2):
                parents = np.random.choice(range(len(self.matrices)), size=2, p=fitness_values/np.sum(fitness_values))

                child = self.reproduce(self.matrices[parents[0]], self.matrices[parents[1]])
                new_matrices.append(child)

            self.matrices = new_matrices

        best_matrix = self.matrices[np.argmax(fitness_values)]
        best_matrix=ORTH(RED(Lattice_Optimizer.descent(best_matrix,n=self.n,T=100000)))
        best_matrix=ORTH(RED(best_matrix))
        return best_matrix