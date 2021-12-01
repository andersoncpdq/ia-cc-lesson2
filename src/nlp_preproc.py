import PyPDF2
from typing import List, Dict
import os
import stanza
import re
import unidecode
import json
from functools import lru_cache

stanza.download('pt')

stop_words = ['o', 'a', 'é', 'e', 'na', 'no', 'ou', 'do', 'da', 'de', 'na', 'à', 'ao', 'as', 'os', 'e,' 'por', 'em',
              'mas', 'como', 'pois', 'embora', 'tais', 'dos', 'das', 'esse', 'desse', 'que', 'um', 'uma']


def reading_pdfs(path: str) -> List:
    """
    This function reads all PDF's in the directory and saves their content in a list
    :param path: Path to PDF directory
    :return: List with the filtered texts
    """
    all_files = os.listdir(path)  # All files in current directory
    pdf_files = sorted([file for file in all_files if 'pdf' in file])  # All PDF files in current directory
    text = []

    for x in pdf_files:
        file = open(path + '/' + f'{x}', 'rb')  # Opening PDF file as binary file
        pdf = PyPDF2.PdfFileReader(file)
        for c in range(pdf.numPages):  # Scanning all PDF's pages
            text.append(pdf.getPage(c).extractText().lower())

    filtered_text = []
    for i in range(len(text)):
        filtered_words = [word for word in text[i].split() if word not in stop_words and len(word) > 1]
        # removing break lines
        filtered_words = [re.sub('\n', '', word) for word in filtered_words]
        # removing chars alphanumeric or underscore
        filtered_words = [re.sub(r'[^\w]', '', word) for word in filtered_words]
        # removing accents
        filtered_words = [unidecode.unidecode(z) for z in filtered_words]

        filtered_text.append(' '.join(filtered_words))

    return filtered_text


def tokenize_and_lemmatize(filtered_list: List) -> Dict:
    """
    This function takes a filtered list with the filtered texts and returns a dictionary with the tokenized
    words of the texts
    :param filtered_list:
    :return: tokenized dictionary
    """
    tokenized_terms = {
        i: dict() for i in range(len(filtered_list))
    }  # Nested dictionary for tokenized words

    nlp = stanza.Pipeline(lang='pt', processors='tokenize,mwt,pos,lemma')

    for s in range(len(filtered_list)):  # Loop for all passed list's elements
        doc = nlp(filtered_list[s])
        for i, sentence in enumerate(doc.sentences):
            for word in sentence.words:
                if word.lemma not in stop_words and len(word.lemma) > 1:
                    tokenized_terms[s] |= {word.id: word.lemma}  # update operation

    with open("token_file.json", "w") as file:
        json.dump(tokenized_terms, file)

    return tokenized_terms


