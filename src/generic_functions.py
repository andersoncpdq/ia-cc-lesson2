import numpy as np
from collections import Counter


def euclidean_distance(p1, p2):
    """
    Calcula a distancia euclidiana entre dois pontos.

    :param p1: coordenada do ponto 1;
    :param p2: coordenada do ponto 2;
    :return: distancia euclidiana entre os pontos (p1 e p2).
    """
    return np.linalg.norm(p1 - p2)


def closest_coordinate(p1, lp):
    """
    Calcula qual a coordenada mais proxima de uma lista de
    pontos a um ponto especifico.

    :param p1: ponto especifico;
    :param lp: lista de pontos;
    :return: coordenada mais proxima na lista (lp) ao ponto (p1).
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
    Ordena uma lista de strings considerando o tamanho de cada string.

    :param str_lst: lista de strings;
    :param desc: booleano para indicar ordem decrescente;
    :return: a lista ordenada.
    """
    if desc:
        str_lst = sorted(str_lst, key=len, reverse=True)
    else:
        str_lst = sorted(str_lst, key=len)
    return str_lst


def count_string_occurrences(str_lst, str_key):
    """
    Contabiliza a quantidade de ocorrencias de uma string-alvo em uma
    lista de strings.

    :param str_lst: lista de strings;
    :param str_key: string-alvo;
    :return: numero de ocorrencias de str_key em str_lst.
    """
    return str_lst.count(str_key)


def occurrences_for_each_element(str_lst):
    """
    Contabiliza a quantidade de cada elemento na lista de strings.

    :param str_lst: lista de strings;
    :return: dictionary mapeando a contagem de cada elemento na lista.
    """
    return Counter(str_lst)


def proximity_analysis(str_lst, str_key, bias):
    """
    Realiza uma analise de proximidade de strings em uma lista de strings,
    com base na string a ser analisada e o limiar de distancia de analise.

    :param str_lst: lista de strings;
    :param str_key: string de analise;
    :param bias: limiar de distancia de analise;
    :return: uma lista com as strings mais proximas da string de analise
             (str_key) baseado no limiar de distancia (bias).
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
    Remove os elementos repetidos de uma lista de qualquer tipo de dados.

    :param lst: lista de entrada;
    :return: lista sem elementos repetidos.
    """
    return list(dict.fromkeys(lst))


def region_interest(mtx, c_roi, s_roi):
    """
    Extrai uma regiao de interesse (ROI) de uma matriz 2D.

    :param mtx: matriz 2D de entrada;
    :param c_roi: coordenada central da ROI (x, y);
    :param s_roi: shape da ROI (h, w);
    :return: recorte da matriz original (matriz ROI).
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
    Extrai multiplas ROIs de uma matriz 2D.

    :param mtx: matriz 2D de entrada;
    :param c_lst: lista dos centros das ROIs (x, y);
    :param s_lst: lista de shapes das ROIs (h, w);
    :return: lista de ROIs extraidas da matriz 2D de entrada.
    """
    return [region_interest(mtx, c_lst[i], s_lst[i]) for i in range(len(c_lst))]


def thresholding(mtx, bias):
    """
    Realiza a limiarizacao de uma matriz numerica. Para cada valor igual ou
    superior ao limiar na matriz de entrada, é atribuído valor 1, caso contrario,
    é atribuido valor 0, na mesma posição da matriz de retorno.

    :param mtx: matriz de entrada;
    :param bias: limiar;
    :return: matriz binaria com as mesmas proporcoes da matriz de entrada.
    """
    return np.vectorize(lambda x: 1 if x >= bias else 0)(mtx)
