from src.generic_functions import roi_list
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
    ap.add_argument('-rc_lst', '--rc_lst',
                    default=[(1, 1), (2, 2), (3, 3)],
                    help='roi center list')
    ap.add_argument('-rs_lst', '--rs_lst',
                    default=[(3, 3), (5, 3), (5, 5)],
                    help='roi shape list')

    args = vars(ap.parse_args())

    mtx = args['mtx']
    c_lst = args['rc_lst']
    s_lst = args['rs_lst']
    result = roi_list(mtx, c_lst, s_lst)

    print('\nMatrix:\n', mtx)
    print('\nLista de ROIs:')
    for i in range(len(result)):
        print('center = {}, shape = {}'.format(mtx[c_lst[i][0]][c_lst[i][1]], s_lst[i]))
        print('\n{}\n'.format(result[i]))


if __name__ == '__main__':
    main()
