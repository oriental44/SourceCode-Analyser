#!/bin/bash
echo "Souhaitez-vous accéder au fichier de configuration?[o/n]"
read choix
echo $choix
if [ $choix == "o" ]
then
	nano setting.xml
elif [ $choix == "n" ]
then
	echo "ok"
else
	echo "tant pis"
fi
echo "Entrer le chemin du fichier à analyser"
read chemin
echo $chemin
cd $chemin
pwd
echo "début traitement ohcount"
ohcount -l  > result.txt
echo "Traitement Ohcount terminée"
mv result.txt /home/stage/Documents/Analyse/Sources
cd
echo "Déplacement terminé"
cd Documents/Analyse/Sources
pwd
python init.py
python analyse.py
python raz.py
cd
echo "fin prog"
