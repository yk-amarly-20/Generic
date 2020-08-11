# create board
import numpy as np

class BoardInit():
    """
    initialize chess board
    """

    def __init__(self, num_queen=8, num_children=50):
        """
        constructor

        Parameters
        ----------
        num_queen: int, default 8
            the numbers of queens
        num_children: int, default 50
            the numbers of children

        Notes
        -----
        num_queen == num_squares
        """

        self.num_queen = num_queen
        self.board = np.zeors((self.num_queen, self.num_queen), dtype=int)

    def set_init_gene(self):
        """
        initializing gene.
        """

        genes = []

        for i in range(num_children):
            gene = []
            queens = []

            for j in range(self.num_queen):



