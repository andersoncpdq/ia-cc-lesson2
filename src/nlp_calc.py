from src.generic_functions import token_list_no_repetition, proximity_analysis, n_terms_max_tf_idf
import numpy as np
import csv


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

    return dfs


def get_inverse_document_frequency(txt_occurrences_terms, dfs):
    """
    Calculate inverse document frequency (IDF) for each term

    :param txt_occurrences_terms:
    :param dfs:
    :return: dictionary of inverse frequencies
    """
    qtd_docs = len(txt_occurrences_terms)
    idfs = {word: np.log10(qtd_docs/(df + 1)) for word, df in dfs.items()}

    return idfs


def get_tf_idf(tfs, idfs):
    """
    Calculate TF-IDF for each term

    :param tfs:
    :param idfs:
    :return: list of dictionary TF-IDF
    """
    tf_idf = []
    for i in range(len(tfs)):
        aux = {}
        for word, vl in tfs[i].items():
            score = vl * idfs[word]
            aux[word] = score
        tf_idf.append(aux)

    return tf_idf


def get_list_of_proximity(tokens, tfs, tf_idfs, n_terms, bias):
    lst_words_max_tf_idf = n_terms_max_tf_idf(tokens, n_terms, tf_idfs)

    dict_str_prox = {}
    for word in lst_words_max_tf_idf:
        for doc in range(len(tokens)):
            lst_tk_doc = [w for w in tokens[doc].values()]
            if word in lst_tk_doc:
                dict_str_prox[word] = [(w, tfs[doc][w]) for w in proximity_analysis(lst_tk_doc, word, bias)]

    return dict_str_prox


def set_csv_proximity(dict_proximity):
    with open('tokens_max_tf_idf.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["TOKENS MAX TF-IDF", "LIST OF PROXIMITY AND TF"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for word, lst in dict_proximity.items():
            writer.writerow({
                "TOKENS MAX TF-IDF": word,
                "LIST OF PROXIMITY AND TF": str(lst)
            })


def set_csv_results(tokens, tfs, dfs, idfs, tf_idfs):
    all_tokens = token_list_no_repetition(tokens)

    with open('results.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["DOC", "TOKEN", "TF", "DF", "IDF", "TF-IDF"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for word in all_tokens:
            for doc in range(len(tokens)):
                if word in tokens[doc].values():
                    writer.writerow({
                        "DOC": str(doc),
                        "TOKEN": word,
                        "TF": str(tfs[doc][word]),
                        "DF": str(dfs[word]),
                        "IDF": str(idfs[word]),
                        "TF-IDF": str(tf_idfs[doc][word])
                    })
