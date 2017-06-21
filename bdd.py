print "fichier bdd.py"
import sqlite3
conn = sqlite3.connect('licenceAnalyse.db')
cursor = conn.cursor()
print "Connexion reussie"

def ajoutFichier(id, nom, licence):
	cursor.execute("INSERT INTO fichier VALUES (?, ?, ?);", (id, nom, licence))

	#Sauvegarde des modifs
	conn.commit()
def isCompatible(licence_orig, licence_distrib):
	licence_originale = []
	licence_distribution = []
	licence_orig_presente = False
	licence_distrib_presente = False
	i=0
	for row in conn.execute("SELECT licence_distrib FROM compatible;"):
		#licence_dest = row[0]
		licence_distribution.insert(i, row[0])
		j = 0
		if licence_distrib == licence_distribution[i]:
			licence_distrib_presente = True
			for row in conn.execute("SELECT licence_orig FROM compatible;"):
				#licence_originale = row[0]
				licence_originale.insert(j, row[0])
				if licence_orig == licence_originale[j]:
					licence_orig_presente = True
					return True
			return False
	return False

def ajoutEtatComp(id, licence_orig, fichier_orig, licence_distrib, fichier_distrib, etat):
	conn.execute("INSERT INTO etatComp VALUES (?,?,?,?,?,?);", (id, licence_orig, fichier_orig, licence_distrib, fichier_distrib, etat))
	conn.commit()

#def recupFichierEtLicence():
	#liste_fichier_licence=[]
	#i=0
	#for row in conn.execute("SELECT nom, licence FROM fichier;"):
	#	liste_fichier_licence.insert(i, row[0], row[1])
	#	i=i+1
	#return liste_fichier_licence

def recupListeLicencesOrig():
	licence_originale = []
	i=0
	for row in conn.execute("SELECT licence_orig FROM compatible;"):
		licence_originale.insert(i, row[0])
		i=i+1
	print "retour liste licences originales"
	return licence_originale

def recupListeLicencesDistrib():
        licence_distribution = []
	i=0
        for row in conn.execute("SELECT licence_distrib FROM compatible;"):
                licence_distribution.insert(i, row[0])
		i=i+1
        print "retour liste licences distrib"
        return licence_distribution

def recupListeLicencesFichier():
	licence_fichier = []
	nom_fichier = []
	i = 0
	for row in conn.execute("SELECT licence FROM fichier;"):
                licence_fichier.insert(i, row[0])
                i=i+1
	j = 0
	for row in conn.execute("SELECT nom FROM fichier;"):
		nom_fichier.insert(j, row[0])
		j=j+1
        print "retour liste licences fichiers"
        return licence_fichier,nom_fichier

def recupListeTtesLicences():
	licence = []
        i = 0
        for row in conn.execute("SELECT nom FROM licence;"):
                licence.insert(i, row[0])
                i=i+1
        print "retour liste de toutes les licences"
        return licence


def fermetureBase():
	#Fermeture du curseur
	cursor.close()
