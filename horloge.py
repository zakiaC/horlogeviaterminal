# -*- coding: utf-8 -*-


#-------------------------------------------------------------------------------
# Nom du programme : Horloge de Zakia
# Version :1
# Objectif du programme :
#
# Auteur:Zakia Chabane
# date de création : 5 mai 2020
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
#Importation des bibliothèques nécessaires au fonctionnement du programme
#-------------------------------------------------------------------------------

import math 
import time

quitter = 'n'

while quitter != 'o' :
    print("Heure courante",time.strftime('%H:%M:%S'))
    quitter = input("Voulez-vous quitter le programme (o/n) ? ")

print("A bientôt")
