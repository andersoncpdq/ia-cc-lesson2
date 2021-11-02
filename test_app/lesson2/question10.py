from src.generic_functions import thresholding
import numpy as np
import argparse


def main():
    mtx = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25]])

    ap = argparse.ArgumentParser()
    ap.add_argument('-mtx', '--mtx',
                    default=mtx,
                    help='input matrix')
    ap.add_argument('-bias', '--bias',
                    default=10,
                    help='threshold')

    args = vars(ap.parse_args())

    mtx = args['mtx']
    bias = args['bias']
    result = thresholding(mtx, bias)

    print('Original matrix:\n{}'.format(mtx))
    print('\nLimiarização com bias = {}:\n{}'.format(bias, result))


if __name__ == '__main__':
    main()
