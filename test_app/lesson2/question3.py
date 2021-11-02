from src.generic_functions import sort_string_list
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-str_lst', '--str_lst',
                    default=['banana', 'pie', 'Washington', 'book'],
                    help='string list')
    ap.add_argument('-desc', '--desc',
                    default=True,
                    help='boolean desc')

    args = vars(ap.parse_args())
    str_lst = args['str_lst']
    is_desc = args['desc']
    result = sort_string_list(str_lst, is_desc)

    print(result)


if __name__ == '__main__':
    main()
