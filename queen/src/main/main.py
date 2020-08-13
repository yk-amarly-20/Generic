# main function
import argparse
import copy
import mlflow
import numpy as np
import random
import sys
sys.path.append('.')
from utils.BoardInit import BoardInit
from utils.cross_over import cross_over
from utils.mutation import mutate
from utils.selection import selection
from utils.show_board import show_board
from evaluation.evaluate import evaluate

def returnEval(gene):
    return gene[1]


def make_parse():
    """
    receive command line variable
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--nq', type=int, default=8, help='the numbers of queens')
    parser.add_argument('--ng', type=int, default=50, help='the numbers of genes')
    parser.add_argument('--seed', type=int, default=100, help="seed value")
    parser.add_argument('--mlflow_uri', default='./mlruns')
    parser.add_argument('--experiment_name', default='training')

    return parser


def main(args):
    """
    main function
    """
    np.random.seed(seed=args.seed)
    random.seed(args.seed)
    # initialize genes
    initializer = BoardInit(args.nq, args.ng)
    genes = initializer.set_init_gene()

    loop = 0
    while True:
        loop += 1
        idx = 0

        # mutate
        genes = mutate(genes, args.nq, args.ng)

        # caluclate fitness))
        for i, gene in enumerate(genes):
            genes[i][1] = evaluate(gene[0], args.nq)

        # selection
        tmp_genes = []
        for i in range(args.ng // 2):
            tmp = selection(genes)

            if tmp == []:
                continue
            else:
                for gene in tmp:
                    tmp_genes.append(gene)
        if tmp_genes == []:
            tmp_genes = copy.deepcopy(genes)

        # cross over
        new_genes = []
        while(len(new_genes) < len(genes)):
            a, b = np.random.choice(range(len(tmp_genes)), 2)
            gene_1, gene_2 = tmp_genes[a], tmp_genes[b]
            crossed = cross_over(gene_1, gene_2, args.nq)
            new_genes.append(min(crossed, key=returnEval))

        min_fitness = min(new_genes, key=returnEval)
        print(loop, 'minimum fitness is ', min_fitness)

        if min_fitness[1] == 0:
            print("loop finished!")
            print(str(loop), 'fitness = ', str(min_fitness[1]))
            print(min_fitness[0])
            break

        genes = copy.deepcopy(new_genes)

    mlflow.set_tracking_uri(args.mlflow_uri)
    mlflow.set_experiment(args.experiment_name)
    tracking = mlflow.tracking.MlflowClient()
    experiment = tracking.get_experiment_by_name(args.experiment_name)

    with mlflow.start_run(experiment_id=experiment.experiment_id, nested=True):
        mlflow.log_param('the numbers of queens', args.nq)
        mlflow.log_param('the numbers of genes', args.ng)
        mlflow.log_param('seed', args.seed)
        mlflow.log_metric('loop', loop)

if __name__=='__main__':
    args = make_parse().parse_args()
    main(args)


