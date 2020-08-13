# create board
import numpy as np
import sys
sys.path.append('..')
from evaluation.evaluate import evaluate

class BoardInit():
    """
    initialize chess board
    """

    def __init__(self, num_queen=8, num_genes=50):
        """
        constructor

        Parameters
        ----------
        num_queen: int, default 8
            the numbers of queens
        num_genes: int, default 50
            the numbers of children

        Notes
        -----
        num_queen == num_squares
        """

        self.num_queen = num_queen
        self.num_genes = num_genes
        self.board = np.zeros((self.num_queen, self.num_queen), dtype=int)

    def set_init_gene(self):
        """
        initializing gene.
        """

        genes = []

        for i in range(self.num_genes):
            gene = []
            queens = []

            for j in range(self.num_queen):
                queen = int(np.random.rand()*self.num_queen)
                queens.append(queen)
            gene.append(queens)
            gene.append(evaluate(queens))
            genes.append(gene)

        return genes


