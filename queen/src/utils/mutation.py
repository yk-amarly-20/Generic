# mutate genes
import random

def mutate(genes, num_queen=8, num_genes=50):
    """
    mutate genes

    Parameters
    ----------
    genes: list<int>
        genes
    num_queen: int, default 8
        the numbers of queens
    num_genes: int, default 50
        the numbers of children

    Returns
    -------
    new_genes: list<int>
        new genes
    """

    for i in range(num_genes // 2):
        gene_idx = random.randint(0, len(genes) - 1)
        position = random.randint(0, num_queen - 1)
        value = random.randint(0, num_queen - 1)
        print(genes[gene_idx])
        print(genes[gene_idx][0][position])
        genes[gene_idx][0][position] = value

    return genes
