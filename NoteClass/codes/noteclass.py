from eleve import Eleve
from classe import Classe
import os
from fonctions import *
from menu import *
	
def main():
	#
	menu()	
	choix = input("Choisir une option : ")
	#
	if choix == '1':
		option1()
	elif choix == '2':
		option2()
	elif choix == '3':
		aides()
		retourPrincipal()
	else:
		quitter()

if __name__ == '__main__':
	main()
