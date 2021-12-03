import numpy as np


def euclidean_distance(p1, p2):
    """
    Calculate the distance between two points

    :param p1: point 1 coordinates;
    :param p2: point 2 coordinates;
    :return: euclidian distance between p1 and p2
    """
    return np.linalg.norm(p1 - p2)


def closest_coordinate(p1, lp):
    """
    Calculate te closest coordinate of a list compared to another point

    :param p1: specific point;
    :param lp: points list;
    :return: list's closest coordinate comparing to p1
    """
    pt = []
    min_dist = float('inf')
    for p in lp:
        aux_dist = euclidean_distance(p, p1)
        if aux_dist < min_dist:
            min_dist = aux_dist
            pt = p
    return pt


def sort_string_list(str_lst, desc=False):
    """
    Sort a string's list with the len of the words in parameter

    :param str_lst: strings list;
    :param desc: booleano para indicar ordem decrescente;
    :return: sorted list.
    """
    if desc:
        str_lst = sorted(str_lst, key=len, reverse=True)
    else:
        str_lst = sorted(str_lst, key=len)
    return str_lst


def count_string_occurrences(str_lst, str_key):
    """
    Counts the quantity of ocurrencies of a specific word in a string list

    :param str_lst: string list;
    :param str_key: key string;
    :return: Quantity of ocurrencies
    """
    return str_lst.count(str_key)


def occurrences_for_each_element(lst):
    """
    Counts how many times each element in a list of dicts

    :param lst: list;
    :return: list of dicts
    """
    cnt = []
    for dct in lst:
        aux = {}
        for k in dct:
            word = dct[k]
            if word not in aux.keys():
                aux[word] = 1
            else:
                aux[word] += 1
        cnt.append(aux)
    return cnt


def proximity_analysis(str_lst, str_key, bias):
    """
    Realizes a proximity analysis in a string's list, comparing them with a passed string

    :param str_lst: string list;
    :param str_key: analysis string;
    :param bias: limiar distance;
    :return: A list with the closest strings based on bias
    """
    str_idx = [i for i, s in enumerate(str_lst) if s == str_key]
    bias_idx = []
    for i in range(1, bias + 1):
        for j in str_idx:
            if (j - i >= 0) and (j - i not in bias_idx):
                bias_idx.append(j - i)
            if (j + i <= len(str_lst) - 1) and (j + i not in bias_idx):
                bias_idx.append(j + i)
    bias_idx.sort()
    return [str_lst[k] for k in bias_idx]


def no_repetition(lst):
    """
    Remove repeated elements in a list

    :param lst: passed list;
    :return: list without repeating elements.
    """
    return list(dict.fromkeys(lst))


def region_interest(mtx, c_roi, s_roi):
    """
    Extracts a ROI from a 2D matrix.

    :param mtx: 2D matrix;
    :param c_roi: ROI's central coordinate(x,y);
    :param s_roi: ROI's shape (h, w);
    :return: ROI matrix
    """
    x, y = c_roi
    h, w = s_roi

    x1 = x - (w // 2)
    y1 = y - (h // 2)
    x2 = 1 + x + (w // 2)
    y2 = 1 + y + (h // 2)

    return mtx[x1:x2, y1:y2]


def roi_list(mtx, c_lst, s_lst):
    """
    Extracts multiple ROI's from a 2D matrix

    :param mtx: 2D matrix;
    :param c_lst: ROI's center list(x,y);
    :param s_lst: Roi's shapes list (h, w);
    :return: Roi's list
    """
    return [region_interest(mtx, c_lst[i], s_lst[i]) for i in range(len(c_lst))]


def thresholding(mtx, bias):
    """
    Performs the thresholding of a numerical matrix. For each equal value or
    above the threshold in the input matrix, a value of 1 is assigned, otherwise,
    it is assigned a value of 0, in the same position as the return matrix.

    :param mtx: matrix;
    :param bias: limiar;
    :return: binary matrix with the same proportions of the original matrix
    """
    return np.vectorize(lambda x: 1 if x >= bias else 0)(mtx)
