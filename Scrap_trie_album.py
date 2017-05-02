from lxml import html
import requests
import os
import subprocess

# Extraction des noms d'albums de l'auteur
# recuperation de la page du groupe

nom_groupe = input("Entrer le nom du groupe: ")
lien_page_groupe = input("Entrer le lien de la page wikipedia du groupe: ")
emplacement = os.getcwd()
print(emplacement)
os.chdir(emplacement)
page = requests.get(lien_page_groupe)

#on se place  a l'emplacement voulu pour telecharger les musiques
# recherche des noms d'album
tree = html.fromstring(page.content)
nom_albums = tree.xpath('//table/tr/td/div/div/cite//text()')
print(nom_albums)
for album in nom_albums:
    nom_dossier = album.replace(' ', '_')
    os.makedirs(nom_dossier)
    os.chdir(nom_dossier)
    liste_musique = tree.xpath("//table/tr/td//div[contains(.,\"{}\")]//i//text()".format(album))
    for musique in liste_musique:
        subprocess.call("youtube-dl --extract-audio -o '{}.%(ext)s' 'ytsearch:{} {}'".format(musique.replace(' ','_'),nom_groupe, musique), shell=True)
    os.chdir(emplacement)

    #test = '//table/tr/td//div[contains(.,\'{}\')]//i//text()'.format(album)

