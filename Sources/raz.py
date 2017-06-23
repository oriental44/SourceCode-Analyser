print "fichier bdd.py"
import sqlite3
conn = sqlite3.connect('licenceAnalyse.db')
cursor = conn.cursor()
print "Connexion reussie"
cursor.execute("DROP TABLE fichier;")
#cursor.execute("DROP TABLE etatComp;")

#Sauvegarde des modifs
conn.commit()
#Fermeture du curseur
cursor.close()

