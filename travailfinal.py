# coding : utf-8 

import requests 
from bs4 import BeautifulSoup
import csv 


# créer une boucle en ajoutant le numéro qui correspond à l'url de chaque article publié en 2018 par le Devoir

fichier = "codesDevoir2018.csv"

f1 = open(fichier)

lignes = csv.reader(f1)

for data in lignes:
    print(data)

lignes = list(range(368493,545653))

urlDebut = "http://m.ledevoir.com/article-" 

    for data in lignes: 
        url = urlDebut + str(data)
        print(url)

        resultat = requests.get(url)

        if resultat.ok:
            
        soup = BeautifulSoup(resultat.text, 'html.parser')
        articles= soup.find_all('div', class_='single')

            for div in articles: 
            titre = div.find('h1')
            print(titre)

                try:
                    site = requests.get(titre)
                    page = BeautifulSoup(site.text, 'html.parser')
                    texte = page.find('div', class_='editorscrolling-tracker').text.strip()
                    print(texte)
                    
# création d'un fichier csv pour exporter les urls du quotion Le Devoir
            
        fichier = 'ledevoir.csv' 

        entêtes = ['Titre', 'Lien URL', 'Texte']

        tableau = open(fichier, 'w') 

        tableau.writerow(entêtes)
        tableau.writerows(titre, url, texte)
        tableau.close()
           























