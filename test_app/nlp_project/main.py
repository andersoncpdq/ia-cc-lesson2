from src.generic_functions import occurrences_for_each_element
from src.nlp_preproc import reading_pdfs, tokenize_and_lemma
from src.nlp_calc import get_term_frequency, get_document_frequency
from pathlib import Path
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-path",
                    "--path",
                    default=str(Path(__file__).parent.resolve()) + '/pdf_files',
                    help="Path pdfs dir")

    args = vars(ap.parse_args())
    path = args['path']

    list_filtered_texts = reading_pdfs(path)
    tokenized_words = tokenize_and_lemma(list_filtered_texts)

    qtd_terms_docs = list(map(len, tokenized_words))
    txt_occurrences_terms = occurrences_for_each_element(tokenized_words)

    tfs = get_term_frequency(txt_occurrences_terms, qtd_terms_docs)
    dfs = get_document_frequency(txt_occurrences_terms)

    print(qtd_terms_docs)
    print(txt_occurrences_terms)
    print(tfs)
    print(dfs)


if __name__ == "__main__":
    main()
