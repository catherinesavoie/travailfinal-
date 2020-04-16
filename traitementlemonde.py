# coding utf-8 

import csv
from collections import Counter

import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 

# ouverture du fichier csv qui contient les données 

devoir = "lemonde.csv"

f1= open(lemonde)
manipulations = csv.reader(f1)
next(manipulations)

vocabulaire = []
bigrams = []

# traitement des lignes des trois sujets de l'entête du document csv (titre, url et texte) 

for mani in manipulations: 

    tokens = word_tokenize(mani[3])
    print(mots)

# retirer tous les mots vides et avec une pontuation hors normes 

tokens = [mot for mot in word_tokenize(mani[3]) if mot not in string.punctuation] 
print(tokens)

# la fréquence de chaque mot inscris dans les trois colonnes du fichier  lemonde.csv 

mots = [fr.stem(mot)for mot in word_tokenize(mani[3]) if mot not in string.punctuation]
print(mots)

for mot in mots: 
vocabulaire.append(mot)

# déterminer les 20 mots les plus utilisés par le journal 

freq = Counter(vocabulaire)
print(freq.most_common(20))
print(len(vocabulaire))

# on regroupe les mots avec la fonction Bigramme 

    for x, y in enumerate(mots[:-1]): 
        bigrams.append("{} {}".format(mots[a], mots[x+1]))
    print(bigrams)

 freq = Counter(bigrams)   
 print(freq.most_common(20))
 print(len(bigrams))
