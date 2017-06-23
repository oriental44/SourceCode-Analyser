print "genereRapport.py"
import sqlite3
from compare import *

def redactionRapport():
	donnees = comparaison()

	conn = sqlite3.connect('licenceAnalyse.db')
	cursor = conn.cursor()

	rapport = open("RapportAnalyse.txt","w")

	rapport.write("  --------------------- \n")
	rapport.write("  | Rapport d'analyse | \n")
	rapport.write("  --------------------- \n")
	rapport.write("                  \n")
	rapport.write("Licences incompatibles \n")

	print "Generation du rapport merci de patienter"

	i=0
	while i < len(donnees):
		if donnees[i+4] == "non_compatibles":
			licence_a = donnees[i]
	       		nomfichier_a = donnees[i+1]
       			licence_b = donnees[i+2]
        		nomfichier_b = donnees[i+3]
			rapport.write(str(i))
		        rapport.write(" * ")
	        	rapport.write(str(licence_a))
		        rapport.write("  |  ")
	        	rapport.write(str(licence_b))
	        	rapport.write(" * \n")
		        rapport.write(str(i))
	        	rapport.write(" * ")
	        	rapport.write(str(nomfichier_a))
		       	rapport.write("  |  ")
	       		rapport.write(str(nomfichier_b))
        		rapport.write(" * \n")
	        	rapport.write("----------------------------------------------- \n")
        	i=i+5

	rapport.close
	print "Fin de la generation du rapport"
