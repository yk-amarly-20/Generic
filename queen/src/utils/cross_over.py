# cross over
import sys
sys.path.append('..')
from evaluation.evaluate import evaluate
import random

def cross_over(gene_1, gene_2, num_queen=8):
    """
    1-point cross over.

    Parameters
    ----------
    gene_1: list<int>
        gene
    gene_2: list<int>
        gene
    num_queen: int, default 8
        the numbers of queens

    Returns
    -------
    new_genes: list<int>
        new genes
    """

    new_gene_1 = [[], 0]
    new_gene_2 = [[], 0]
    new_genes = []
    alter_point = 0     # cross_over point

    if random.randint(0, 1) == 0:
        alter_point = 1
    else:
        alter_point = num_queen // 2

    if random.randint(0, 1) == 0:
        new_queens_1 = gene_1[0][:alter_point]
        new_queens_1 += gene_2[0][alter_point:]
        new_queens_2 = gene_2[0][:alter_point]
        new_queens_2 += list(gene_1[0][alter_point:])
        new_gene_1[0] = new_queens_1
        new_gene_2[0] = new_queens_2
        new_gene_1[1] = evaluate(new_gene_1[0])
        new_gene_2[1] = evaluate(new_gene_2[0])
        new_genes.append(new_gene_1)
        new_genes.append(new_gene_2)

    else:
        new_queens_1 = gene_1[0][alter_point:]
        new_queens_1 += gene_2[0][:alter_point]
        new_queens_2 = gene_2[0][alter_point:]
        new_queens_2 += list(gene_1[0][:alter_point])
        new_gene_1[0] = new_queens_1
        new_gene_2[0] = new_queens_2
        new_gene_1[1] = evaluate(new_gene_1[0])
        new_gene_2[1] = evaluate(new_gene_2[0])
        new_genes.append(new_gene_1)
        new_genes.append(new_gene_2)

    return new_genes
