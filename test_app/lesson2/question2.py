from src.generic_functions import closest_coordinate
import numpy as np
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-p1', '--p1',
                    default=np.array([1.5, 2.2]),
                    help='point')
    ap.add_argument('-lp', '--lp',
                    default=np.array([[1.0, 1.5], [2.5, 3.0], [3.5, 4.0]]),
                    help='list of points')

    args = vars(ap.parse_args())
    p1 = args['p1']
    lp = args['lp']
    result = closest_coordinate(p1, lp)

    print('Coordenada mais prox: ', result)


if __name__ == '__main__':
    main()
