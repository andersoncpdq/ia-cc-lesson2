import json


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


# Document Frequency (Df)
def get_document_frequency(txt_occurrences_terms):
    """
    Calculate document frequent (DF) for each term

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


# Inverse Document Frequency (IDF)
# TF-IDF
#
# CSV file
