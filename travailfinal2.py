# coding : utf-8 

from bs4 import BeautifulSoup
import csv 
import requests 

# définir identifer le lien principal à utiliser 


liens = []

for mois in range(1,13): 
    if mois < 10: 
        mois = "0" + str(mois) 
    for jour in range(1, 32): 
        if jour< 10: 
            jour = "0" + str(jour) 
        for page in range(1,11): 
            url = 'https://www.lemonde.fr/archives-du-monde/{}-{}-2018/{}/'.format(str(jour), str(mois), str(page))

            print(url)

            resultat = requests.get(url)

            if resultat.ok:
            
                soup = BeautifulSoup(resultat.text, 'html.parser')
                articles = soup.find_all('section', class_='teaser')

                for section in articles: 
                    a = section.find('a')
                    titre = section.find('h3').text.strip()
                    print(titre, url)
                    try:
                        site = requests.get(url)
                        page = BeautifulSoup(site.text, 'html.parser')
                        texte = page.find('article', class_='article__content').text.strip()
                        print(texte)
                        print('#'*20)
                        
                    except:
                        print('ça ne fonctionne pas')

                

            # print(liens)

            # création d'un fichier csv pour exporter les urls du quotion Le Monde
            
            fichier = 'lemonde.csv' 

            entêtes = ['Titre', 'Lien URL', 'Texte']

            tableau = open(fichier, 'w') 

            tableau.writerow(entêtes)
            tableau.writerows(titre, liens, texte)
            tableau.close()












        


        
            



    








