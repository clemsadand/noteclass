import os
#*****************************************************
#Menu
def menu():
	separateur("Bienvenu.e sur votre NoteClass\nProgramme de gestion des notes d'une\n classe")
	#
	string = "Menu\n"
	string += "1. Créer une classe\n"
	string += "2. Charger une classe\n"
	string += "3. Aides\n"
	string += "4. Quitter"
	separateur(string)

from classe import Classe
from fonctions import separateur

#****************************************************
def sousMenu(classe, filename):
	#
	separateur("Vous êtes bien dans la classe")
	#
	string = "Menu\n"
	string += "1. Voir les notes\n"
	string += "2. Ajouter une note d'interrogation\n"
	string += "3. Ajouter une note de devoir\n"
	string += "4. Calculer la moyenne totale\n"
	string += "5. Retour\n"
	string += "6. Quitter"
	separateur(string)
	#
	choix = input("Choisir une option : ")
	
	if choix == '1':
		classe.afficherClasse()
		retour(classe, filename)
	elif choix == '2':
		classe.setNoteInterro()
		classe.sauvegarder(filename)
		#
		retour(classe, filename)
	elif choix == '3':
		classe.setNoteDevoir()
		classe.sauvegarder(filename)
		#
		retour(classe, filename)
	elif choix == '4':
		coefficient = input("Coefficient de la matière : ")
		classe.sauvegarder(filename)
		classe.sauvegarderMoyennes(filename, int(coefficient))
		#
		separateur("La moyenne a été calculé")
		#separateur("")
		#choix = input("Choisir une option : ")
		classe.sauvegarderEnPdf(int(coefficient), filename)
		separateur("Deux fichiers ont été générés")
		retour(classe, filename)
	elif choix == '5':
		retourPrincipal()
	else:
		quitter()

#*************************************************	
def retourPrincipal():
	separateur("1. Retour\n2. Quitter")
	choix = input("Choisir une option : ")
	
	if choix == '1':
		retourPrincipal()
	else:
		quitter()

#**************************************************
def retour(classe, filename):
	separateur("Menu\n1. Retour\n2. Quitter")
	choix = input("Choisir une option : ")
	#
	if choix == '1':
		sousMenu(classe, filename)
	else:
		quitter()

#***************************************************
def option1():
	nomClasse = input("Nom de la classe (ex. classe4emath) : ")
	#
	cpt = 1
	while (("/" in nomClasse) | (" " in nomClasse)) & (cpt < 3) :
		print("Le nom n'est pas valide !!!")
		nomClasse = input("Nom de la classe (ex. classe4emath) : ")
		cpt += 1
	
	if cpt == 3:
		quitter()
	else:
		#
		effectif = input("Effectif de la classe : ")
		
		#Créer d'une classe
		classe = Classe(int(effectif))
		classe.setNom(nomClasse)
		#Créer un nom de fichier	
		filename = classe.getNom().lower()+".csv"
		
		#
		print("Entrer nom et prénom des élèves")
		#Ajout des élèves
		classe.setListEleves()
		#Afficher le sous-menu
		sousMenu(classe, filename)

#***************************************************
def option2():
	#
	filename = input("Entrer le nom du fichier : ")
	cpt = 1
	while ((not os.path.exists(filename)) & (cpt < 3)):
		print("Le fichier n'existe pas !!!")
		filename = input("Entrer le nom du fichier : ")
		cpt += 1
	
	if cpt == 3:
		print("Retour et créer une classe")
		retourPrincipal()
	else:
		#On charge la classe si le fichier existe
		if os.path.exists(filename):
			#Teste si le fichier est vide
			if os.stat(filename).st_size == 0:
				print("Ce fichier est vide")
				retourPrincipal()
			else:
				#Créer une classe
				classe = Classe()
				#Charger les données à partir d'un fichier csv
				classe.setListEleves(filename)
				#Afficher le sous-menu
				sousMenu(classe, filename)
		else:
			retourPrincipal()
		

#***************************************************
def quitter():
	print("A bientôt")
	exit()

#***************************************************
def aides():
	string = "* NoteClass permet de gérer les notes \nd'une classe"
	string += "* Comment NoteClass fonctionne ?\n"
	string += "NoteClass fonctionne sur la base des\n données fournies par son utilisateur\n"
	string += "* L'interface de NoteClass est assez\n intuitif pour que son utilisateur se\n retrouve facilement\n"
	string += "* Comment utiliser NoteClass ?\n"
	string += "Vous pouvez créer classe ou bien\n charger une classe déjà créée\n"
	string += "** Pour créer une classe, il faut un\n nom. Le nom doit être une suite de\n caractère sans espace.\n"
	string += "** Pour charger une classe, il suffit de\n renseigner le nom du fihcier\n (format .csv). Précisez le simplement\n le chemin menant vers ce fichier\n"
	string += "Merci d'utiliser NoteClass !"
	separateur(string)
#*****************************************************
