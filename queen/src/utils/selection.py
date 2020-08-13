# selection
import numpy as np

def selection(genes):
    """
    select new generation

    Parameters
    ----------
    genes: list<int>
        gene set

    Returns
    -------
    new_genes: list<int>
        gene set
    """

    p = np.zeros(len(genes))
    new_genes = []

    for i, gene in enumerate(genes):
        if gene[1] == 0:
            value = 10000
        else:
            value = 1 / (gene[1] ** 2)
        p[i] = value

    p = p / sum(p)


    prob = np.random.rand(len(genes))
    for i in range(len(genes)):
        if p[i] > prob[i]:
            new_genes.append(genes[i])

    return new_genes
