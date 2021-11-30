import PyPDF2
from typing import List, Dict
import os
import stanza
import re
import unidecode
import json

stanza.download('pt')


stop_words = ['o', 'a', 'é', 'e', 'na', 'no', 'ou', 'do', 'da', 'de', 'na', 'à', 'ao', 'as', 'os', 'e,' 'por', 'em',
              'mais', 'como', 'embora', 'haja', 'ser', 'foram', 'tais', 'dos', 'das', 'esse']  # A list with stop words


def reading_pdfs(PATH: str) -> List:
    """
    This function reads all PDF's in the directory and saves their content in a list
    :param PATH: Path to PDF directory
    :return: List with the filtered texts
    """
    all_files = os.listdir(PATH)  # All files in current directory
    pdf_files = sorted([file for file in all_files if 'pdf' in file])  # All PDF files in current directory
    text = list()
    for x in pdf_files:
        file = open(PATH + '/' + f'{x}', 'rb')  # Opening PDF file as binary file
        print(x)
        pdf = PyPDF2.PdfFileReader(file)
        for c in range(pdf.numPages):  # Scanning all PDF's pages
            objHandler = pdf.getPage(c)  # An object who will handle the PDF page
            text.append(objHandler.extractText().lower())  # Adding texts in lowercase

    filtered_text = []
    for c in range(len(text)):
        filtered_words = [word for word in text[c].split() if word.lower() not in stop_words]  # Filtering stop words
        filtered_words = [re.sub(r'[^\w]', '', word) for word in filtered_words]  # removing characters that's not
        # alphanumeric or underscore

        filtered_words = [unidecode.unidecode(z) for z in filtered_words]  # removing accents

        new_phrase = ' '.join(filtered_words)
        filtered_text.append(new_phrase)

    print(filtered_text)

    del text  # Deleting unused variable
    del filtered_words  # Deleting unused variable

    return filtered_text


def lemma(word: str) -> str:
    """
    This function will lemmantize a word and return her with lemma
    :param word: word
    :return: lemmantized word
    """
    nlp = stanza.Pipeline(lang='pt', processors='tokenize,mwt,pos,lemma')
    doc = nlp(word)
    for sent in doc.sentences:
        for word in sent.words:
            return word.lemma


def tokenize(filtered_list: List) -> Dict:
    """
    This function takes a filtered list with the filtered texts and returns a dictionary with the tokenized
    words of the texts
    :param filtered_list:
    :return: tokenized dictionary
    """
    tokenized_terms = {
        i: dict() for i in range(len(filtered_list))
    }  # Nested dictionary for tokenized words

    nlp = stanza.Pipeline(lang='pt', processors='tokenize')

    for s in range(len(filtered_list)):  # Loop for all passed list's elements
        doc = nlp(filtered_list[s])

        for i, sentence in enumerate(doc.sentences):
            print('='*5 + f' Sentence {i + 1} tokens ' + '='*5)
            print(*[f'id: {token.id[0]}\ttext: {token.text}' for token in sentence.tokens], sep='\n')
            for token in sentence.tokens:
                # LEMANTIZAR AQUI!!!!
                lemma_word = lemma(token.text)
                tokenized_terms[s] |= {token.id[0]: lemma_word}  # update operation

    print('\n\n')
    print(tokenized_terms)
    with open("token_file.json", "w") as file:
        json.dump(tokenized_terms, file)

    return tokenized_terms


