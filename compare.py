print "fichier compare.py"
import sqlite3
from bdd import *
#licences_orig_fichier = recupListeLicencesFichier().row[0]
#nom_orig_fichier = recupListeLicencesFichier().row[1]
licences_orig_fichier, nom_orig_fichier = recupListeLicencesFichier()
licences_distrib_fichier, nom_distrib_fichier = recupListeLicencesFichier()
print "licences orig"
print licences_orig_fichier
print "*******"
print "Nom"
print nom_orig_fichier

#licences_distrib_fichier = recupListeLicencesFichier().row[0]
#nom_distrib_fichier = recupListeLicencesFichier().row[1]

i = 0
k = 1
l = k
print "Longueur licences origine"
print len(licences_orig_fichier)
print "longueur licences distrib"
print len(licences_distrib_fichier)
while i < len(licences_orig_fichier):
	j=0
	while j < len(licences_distrib_fichier):
		if nom_orig_fichier[i] != nom_distrib_fichier[j]:
			if j == 0:
				k=l
			if isCompatible(licences_orig_fichier[i],licences_distrib_fichier[j]) or licences_orig_fichier[i] == licences_distrib_fichier[j]:
				print("Les deux licences sont compatibles: "+licences_orig_fichier[i]+" ; "+licences_distrib_fichier[j])
				etat = "compatibles"

				ajoutEtatComp(k, licences_orig_fichier[i], nom_orig_fichier[i], licences_distrib_fichier[j], nom_distrib_fichier[j], etat)
				fermetureBase()

			else:
				print("Les licences ne sont pas compatibles: "+licences_orig_fichier[i]+" ; "+licences_distrib_fichier[j])
				etat = "non_compatibles"

	                        ajoutEtatComp(k, licences_orig_fichier[i], nom_orig_fichier[i], licences_distrib_fichier[j], nom_distrib_fichier[j], etat)
				fermetureBase()

   		j=j+1
		k=k+1
	i=i+1
	l=k


