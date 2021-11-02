from src.generic_functions import proximity_analysis
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-str_lst', '--str_lst',
                    default=['abacate', 'pera', 'uva', 'banana', 'maçã', 'repolho', 'uva', 'feijão', 'arroz'],
                    help='string list')
    ap.add_argument('-str_key', '--str_key',
                    default='uva',
                    help='string key')
    ap.add_argument('-bias', '--bias',
                    default=2,
                    help='limiar')

    args = vars(ap.parse_args())
    str_lst = args['str_lst']
    str_key = args['str_key']
    bias = args['bias']
    result = proximity_analysis(str_lst, str_key, bias)

    print(result)


if __name__ == '__main__':
    main()
