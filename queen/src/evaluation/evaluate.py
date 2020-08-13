# calclate evaliation
import sys
sys.path.append('..')
from utils.show_board import show_board

def evaluate(gene, num_queen=8):
    """
    calclate evaluation

    Parameters
    ----------
    gene: list<int>
        gene
    num_queen: int, default 8
        the numbers of queens

    Returns
    -------
    value: int
    """

    value = 0
    board = show_board(gene, num_queen)
    for i, queen in enumerate(gene):
        x = queen
        y = i

        for j in range(num_queen):
            # check if queen exists in vertical line or not
            if (board[j][queen] == 1) and (j != y):
                value += 1

            # check if queen diagonal line or not
            vertical = i + j
            horizontal = queen + j

            if (vertical < num_queen) and (horizontal < num_queen) and \
             (board[vertical][horizontal] == 1):
                value += 1

            vertical = i - j
            horizontal = queen - j

            if (vertical > -1) and (horizontal > -1) and \
            (board[vertical][horizontal] == 1):
                value += 1

            vertical = i - j
            horizontal = queen + j

            if (vertical > -1) and (horizontal < num_queen) and \
            (board[vertical][horizontal] == 1):
                value += 1

            vertical = i + j
            horizontal = queen - j

            if (vertical < num_queen) and (horizontal > -1) and \
            (board[vertical][horizontal] == 1):
                value += 1
    return value
