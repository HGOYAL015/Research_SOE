import gensim
import numpy as np
import spacy
from spacy import displacy
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import matplotlib.pyplot as plt
import sklearn
# import keras
# file =input()
file=input()
file_handle=open(file,'r')
file_handle.readline()
print("issue_id~stam_let")
nlp = spacy.load('en_core_web_sm')

for line in file_handle:
    a,text=line.split("~",1)
    text=text[:-1]
    text=' '.join(text.split('\n'))
    text=' '.join(text.split())
    text=text+"\n"
    # print(text)

    doc = nlp(text.lower())
    # print(doc)
    # sent = nlp(u"Tom ran to the repair shop to fix his bicycle.")


    # for token in sent:
    #     print(token.text, token.pos_, token.tag_)


    # we add some words to the stop word list
    texts, article = [], []
    for w in doc:
        # if it's not a stop word or punctuation mark, add it to our article!
        if w.text != '\n' and not w.is_stop and not w.is_punct and not w.like_num and w.text != 'I':
            # we add the lematized version of the word
            article.append(w.lemma_)
        # if it's a new line, it means we're onto our next document
        if w.text == '\n':
            texts.append(article)
            article = []
    print(a,end="~")
    for i in texts:
        for j in i:
            print(j,end=" ")
    print()
