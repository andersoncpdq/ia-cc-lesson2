import numpy as np
from collections import Counter


def euclidean_distance(p1, p2):
    return np.linalg.norm(p1 - p2)


def closest_coordinate(p1, lp):
    pt = []
    min_dist = float('inf')
    for p in lp:
        aux_dist = euclidean_distance(p, p1)
        if aux_dist < min_dist:
            min_dist = aux_dist
            pt = p
    return pt


def sort_string_list(str_lst, desc=False):
    if desc:
        str_lst = sorted(str_lst, key=len, reverse=True)
    else:
        str_lst = sorted(str_lst, key=len)
    return str_lst


def count_string_occurrences(str_lst, str_key):
    return str_lst.count(str_key)


def occurrences_for_each_element(str_lst):
    return Counter(str_lst)


def proximity_analysis(str_lst, str_key, bias):
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
    return list(dict.fromkeys(lst))


def region_interest(mtx, c_roi, s_roi):
    x, y = c_roi
    h, w = s_roi

    x1 = x - (w // 2)
    y1 = y - (h // 2)
    x2 = 1 + x + (w // 2)
    y2 = 1 + y + (h // 2)

    return mtx[x1:x2, y1:y2]


def roi_list(mtx, c_lst, s_lst):
    return [region_interest(mtx, c_lst[i], s_lst[i]) for i in range(len(c_lst))]
