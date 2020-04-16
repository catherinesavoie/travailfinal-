# coding utf-8 

import csv
from collections import Counter

import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 

# ouverture du fichier csv qui contient les données 

devoir = "ledevoir.csv"

f1= open(devoir)
manipulations = csv.reader(f1)
next(manipulations)

vocabulaire = []
bigrams = []

# traitement des 3 lignes du doc ledevoir.csv, soit titre, lien, texte 

for mani in manipulations: 

    tokens = word_tokenize(mani[3])
    print(mots)

# élimination des mots vides 

tokens = [mot for mot in word_tokenize(mani[3]) if mot not in string.punctuation] 
print(tokens)

# compter les fréquences d'utilisation d'un mot 

mots = [fr.stem(mot)for mot in word_tokenize(mani[3]) if mot not in string.punctuation]
print(mots)

for mot in mots: 
vocabulaire.append(mot)

# déterminer les 20 mots les plus utilisés par le journal 

freq = Counter(vocabulaire)
print(freq.most_common(20))
print(len(vocabulaire))

# on regroupe les mots avec la fonction Bigramme 

    for a, b in enumerate(mots[:-1]): 
        bigrams.append("{} {}".format(mots[a], mots[a+1]))
    print(bigrams)

 freq = Counter(bigrams)   
 print(freq.most_common(20))
 print(len(bigrams))










