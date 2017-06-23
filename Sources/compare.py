print "fichier compare.py"
import sqlite3
from bdd import *

def comparaison():
	licences_orig_fichier, nom_orig_fichier = recupListeLicencesFichier()
	licences_distrib_fichier, nom_distrib_fichier = recupListeLicencesFichier()

	resultatComp=[]

#	print "licences orig"
#	print licences_orig_fichier
#	print "*******"
#	print "Nom"
#	print nom_orig_fichier

	i = 0
	k = 1
	l = k

#	print "Longueur licences origine"
#	print len(licences_orig_fichier)
#	print "longueur licences distrib"
#	print len(licences_distrib_fichier)
	if len(licences_orig_fichier) < 100:
		print "Merci de patienter, l'operation de comparaison prendra quelques secondes"
	if len(licences_orig_fichier) >= 100 and len(licences_orig_fichier) < 1000:
		print "Merci de patiente, l'operation de comparaison peut prendre quelques minutes"
	if len(licences_orig_fichier) >= 1000:
		print "Merci de patienter, suivant la puissance de votre ordinateur, l'operation peut prendre quelques minutes voire quelques heures"
	while i < len(licences_orig_fichier):
		j=0
		while j < len(licences_distrib_fichier):
			if nom_orig_fichier[i] != nom_distrib_fichier[j]:
				if j == 0:
					k=l
				if isCompatible(licences_orig_fichier[i],licences_distrib_fichier[j]) or licences_orig_fichier[i] == licences_distrib_fichier[j]:
					#print("Les deux licences sont compatibles: "+licences_orig_fichier[i]+" ; "+licences_distrib_fichier[j])
					etat = "compatibles"

					resultatComp.insert(k, licences_orig_fichier[i])
					resultatComp.insert(k+1, nom_orig_fichier[i])
					resultatComp.insert(k+2, licences_distrib_fichier[j])
					resultatComp.insert(k+3, nom_orig_fichier[j])
					resultatComp.insert(k+4, etat)

					#ajoutEtatComp(k, licences_orig_fichier[i], nom_orig_fichier[i], licences_distrib_fichier[j], nom_distrib_fichier[j], etat)
					#fermetureBase()

				else:
					#print("Les licences ne sont pas compatibles: "+licences_orig_fichier[i]+" ; "+licences_distrib_fichier[j])
					etat = "non_compatibles"

					resultatComp.insert(k, licences_orig_fichier[i])
                                        resultatComp.insert(k+1, nom_orig_fichier[i])
                                        resultatComp.insert(k+2, licences_distrib_fichier[j])
                                        resultatComp.insert(k+3, nom_orig_fichier[j])
                                        resultatComp.insert(k+4, etat)

                        		#ajoutEtatComp(k, licences_orig_fichier[i], nom_orig_fichier[i], licences_distrib_fichier[j], nom_distrib_fichier[j], etat)
					#fermetureBase()

			j=j+1
			k=k+5
		i=i+1
		l=k

	return resultatComp

