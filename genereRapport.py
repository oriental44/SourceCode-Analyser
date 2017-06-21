print "genereRapport.py"
import sqlite3
conn = sqlite3.connect('licenceAnalyse.db')
cursor = conn.cursor()

rapport = open("RapportAnalyse.txt","w")

rapport.write("  --------------------- \n")
rapport.write("  | Rapport d'analyse | \n")
rapport.write("  --------------------- \n")
rapport.write("                  \n")
rapport.write("Licences incompatibles \n")
i=1
print "Generation du rapport merci de patienter"
for row in conn.execute("SELECT * FROM etatComp WHERE etat = 'non_compatibles';"):
	licence_a = row[1]
	nomfichier_a = row[2]
	licence_b = row[3]
	nomfichier_b = row[4]
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
	i=i+1
rapport.close
print "Fin de la generation du rapport"
