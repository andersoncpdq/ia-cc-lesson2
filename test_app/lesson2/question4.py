from src.generic_functions import count_string_occurrences
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-str_lst', '--str_lst',
                    default=['banana', 'pie', 'washington', 'pie', 'pie'],
                    help='string list')
    ap.add_argument('-str_key', '--str_key',
                    default='pie',
                    help='string analysis')

    args = vars(ap.parse_args())
    str_lst = args['str_lst']
    str_key = args['str_key']
    result = count_string_occurrences(str_lst, str_key)

    print(result)


if __name__ == '__main__':
    main()
