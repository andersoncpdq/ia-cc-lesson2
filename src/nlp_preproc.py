from typing import List, Dict
import PyPDF2
import os
import re
import stanza
import json
import nltk

stanza.download('pt')
nltk.download('stopwords')

stop_words = nltk.corpus.stopwords.words('portuguese')


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
        # removing stop words
        filtered_words = [word for word in text[i].split() if word not in stop_words]
        # removing chars alphanumeric or underscore
        filtered_words = [re.sub(r'[^\w]', '', word) for word in filtered_words]

        # removing break lines
        # filtered_words = [re.sub('\n', '', word) for word in filtered_words]
        # removing accents
        # filtered_words = [unidecode.unidecode(z) for z in filtered_words]
        # removing numeric values
        # filtered_words = [word for word in filtered_words if not word.isnumeric()]

        filtered_text.append(' '.join(filtered_words))

    return filtered_text


def tokenize_and_lemma(filtered_list: List) -> Dict:
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
        for sentence in doc.sentences:
            for word in sentence.words:
                if len(word.lemma) > 1:
                    tokenized_terms[s] |= {word.id: word.lemma}  # update operation

    with open("token_file.json", "w", encoding='utf-8') as file:
        json.dump(tokenized_terms, file, ensure_ascii=False)

    return tokenized_terms


