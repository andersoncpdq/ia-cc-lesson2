import json
import math


def get_term_frequency(txt_occurrences_terms, qtd_terms_docs):
    """
    Calculate term frequency (TF) for each term

    :param txt_occurrences_terms:
    :param qtd_terms_docs:
    :return: list of Tfs
    """
    tfs = []
    for i in range(len(txt_occurrences_terms)):
        tfs.append(dict(map(lambda x: (x, txt_occurrences_terms[i][x] / qtd_terms_docs[i]), txt_occurrences_terms[i])))

    with open("tfs.json", "w", encoding='utf-8') as file:
        json.dump(tfs, file, ensure_ascii=False)

    return tfs


def get_document_frequency(txt_occurrences_terms):
    """
    Calculate document frequency (DF) for each term

    :param txt_occurrences_terms:
    :return: dictionary of frequencies
    """
    dfs = {}
    for doc in txt_occurrences_terms:
        for word in doc.keys():
            if word not in dfs.keys():
                dfs[word] = 1
            else:
                dfs[word] += 1

    with open("dfs.json", "w", encoding='utf-8') as file:
        json.dump(dfs, file, ensure_ascii=False)

    return dfs


def get_inverse_document_frequency(txt_occurrences_terms, dfs):
    """
    Calculate inverse document frequency (IDF) for each term

    :param txt_occurrences_terms:
    :param dfs:
    :return: dictionary of inverse frequencies
    """
    qtd_docs = len(txt_occurrences_terms)
    idfs = {word: math.log10(qtd_docs/(df + 1)) for word, df in dfs.items()}

    with open("idfs.json", "w", encoding='utf-8') as file:
        json.dump(idfs, file, ensure_ascii=False)

    return idfs


# TF-IDF
#
# CSV file
