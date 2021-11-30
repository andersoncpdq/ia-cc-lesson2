from src.nlp_preproc import reading_pdfs, tokenize
from pathlib import Path
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-path", "--path", default=str(Path(__file__).parent.resolve()) + '/pdf_files', help="Path to pdfs directory")

    args = vars(ap.parse_args())
    path = args['path']
    list_filtered_texts = reading_pdfs(path)
    tokenized_words = tokenize(list_filtered_texts)
    print(tokenized_words)


if __name__ == "__main__":
    main()
