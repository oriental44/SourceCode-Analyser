print "init bdd.py"
import sqlite3
conn = sqlite3.connect('licenceAnalyse.db')
cursor = conn.cursor()
print "Connexion reussie"
cursor.execute("create table if not exists fichier(id integer primary key, nom TEXT, licence TEXT, FOREIGN KEY(licence) REFERENCES licence_orig(nom));")
#cursor.execute("create table if not exists etatComp(id integer primary key, licence_orig TEXT, fichier_orig TEXT, licence_distrib TEXT,fichier_distrib TEXT, etat TEXT);")
#Sauvegarde des modifs
conn.commit()
#Fermeture du curseur
cursor.close()

