print "Fichier interaction.py"
from bdd import *
def remplissageBdd():
	print 'Appel bdd'
	#ajoutFichier("toto", "gpl")
	i=0
	with open("result.txt") as f:
		for line in f:
			print ("DEBUG=>"+line)
			x=line.split(" ")
			print x
			print x[1]
			nomFichier = x[1]
			pos = nomFichier.find("\n")
			nom = nomFichier[:pos]
			i=i+1
			ajoutFichier(i,nom,x[0])
		fermetureBase()
