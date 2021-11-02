from src.generic_functions import region_interest
import numpy as np
import argparse


def main():
    matrix = np.array([[1, 2, 3, 4, 5],
                       [6, 7, 8, 9, 10],
                       [11, 12, 13, 14, 15],
                       [16, 17, 18, 19, 20],
                       [21, 22, 23, 24, 25]])

    ap = argparse.ArgumentParser()
    ap.add_argument('-mtx', '--mtx',
                    default=matrix,
                    help='input matrix')
    ap.add_argument('-rc', '--rc',
                    default=(1, 1),
                    help='roi center')
    ap.add_argument('-rs', '--rs',
                    default=(3, 3),
                    help='roi shape')

    args = vars(ap.parse_args())

    mtx = args['mtx']
    rc = args['rc']
    rs = args['rs']
    result = region_interest(mtx, rc, rs)

    print('Original matrix:\n{}'.format(mtx))
    print('ROI matrix:\n{}'.format(result))


if __name__ == '__main__':
    main()
