from src.generic_functions import occurrences_for_each_element
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-str_lst', '--str_lst',
                    default=['banana', 'pie', 'washington', 'pie', 'banana', 'pie'],
                    help='string list')

    args = vars(ap.parse_args())
    str_lst = args['str_lst']
    result = occurrences_for_each_element(str_lst)

    print(result)


if __name__ == '__main__':
    main()
