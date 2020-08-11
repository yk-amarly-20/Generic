# show board from gene list
import numpy as np

def show_board(gene, num_queen=8):
    """
    show board from gene list.
    A board is represented as zeros-ndarray.
    There is "1" where queen stands.

    Parameters
    ----------
    gene: list<int>
        gene list

    num_queen: int, default 8
        the numbers of queens

    Returns
    -------
    board: ndarray<int>
        board
    """

    board = np.zeros((num_queen, num_queen), dtype=int)
    for i, queen in enumerate(gene):
        board[i][queen] = 1

    return board
