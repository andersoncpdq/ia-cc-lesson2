from src.generic_functions import no_repetition
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-lst', '--lst',
                    # default=['a', 'b', 'b', 'c', 'd', 'c', 'e', 'f', 'a'],
                    default=[1, 1, 2, 3, 4, 2, 5, 3, 6],
                    help='input list')

    args = vars(ap.parse_args())
    input_lst = args['lst']
    result = no_repetition(input_lst)

    print(result)


if __name__ == '__main__':
    main()
