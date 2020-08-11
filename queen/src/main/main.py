# main function
import argparse
import mlflow
from ..utils.BoardInit import BoardInit
from ..utils.cross_over import cross_over
from ..utils.mutation import mutate
from ..utils.selection import selection
from ..utils.show_board import show_board
from ..evaluation.evaluate import evaluate

def returnEval(gene):
    return gene[1]


def make_parse():
    """
    receive command line variable
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--nq', type=int, default=8, help='the numbers of queens')
    parser.add_argument('--ng', type=int, default=50, help='the numbers of genes')

    return parser


def main(args):
    """
    main function
    """

    # initialize genes
    initializer = BoardInit(args.nq, args.ng)
    genes = initializer.set_init_gene()

    loop = 0
    while True:
        loop += 1
        idx = 0

        # mutate
        genes = mutate(genes, args.nq, args.ng)

        # caluclate fitness
        for i, genes in enumerate(genes):
            genes[i][1] = evaluate(gene[0], args.nq)

        # selection



