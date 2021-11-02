from src.generic_functions import euclidean_distance
import numpy as np
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-p1', '--p1', default=np.array([1, 1]), help='first point')
    ap.add_argument('-p2', '--p2', default=np.array([3, 1]), help='second point')

    args = vars(ap.parse_args())
    p1 = args['p1']
    p2 = args['p2']
    result = euclidean_distance(p1, p2)

    print('Distancia Euclidiana: ', result)


if __name__ == '__main__':
    main()
