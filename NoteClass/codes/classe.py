from eleve import Eleve
import os
from os import path
import subprocess
from fonctions import *
#Classe Classe
class Classe:
	def __init__(self, effectif = 0):
		self.listEleves = []
		self.effectif = effectif
		self.nom = ''
		#self.coefficient = coefficient
	
	def setNom(self, nom):
		self.nom = nom
	
	def getNom(self):
		return self.nom
	#Créer une classe à partir d'un fichier
	#ou via une interaction
	def setListEleves(self, filename = None):
		if filename:
			#Ouvrir un fichier
			f = open(filename, 'r')
			for ligne in f:
				liste = ligne.split(';')
				liste[-1] = liste[-1][:-1]#Supprimer \n
				eleve = Eleve(liste[0])
				eleve.setNoteInterro(stringListToList(liste[1]))
				#print(liste[2] == "[]")
				eleve.setNoteDevoir(stringListToList(liste[2]))
				self.listEleves.append(eleve)
			f.close()
		else:
			cpt = 0
			#suivant = True
			while (cpt < self.effectif):
				cpt += 1
				#print(str(cpt)+' : ')
				nom = input("Elève "+str(cpt) +" : ")
				eleve = Eleve(nom)
				self.listEleves.append(eleve)
				#suivant = (input("Ajouter un élève (o/n) : ")).lower() == 'o'	
			print("La classe a été chargé")
	
	#Ajouter une note d'interro
	def setNoteInterro(self):
		print("Note d'interrogation")
		for eleve in self.listEleves:
			note = input("> "+eleve.getNom()+" : ")
			eleve.setNoteInterro(float(note))
	
	#Ajouter une note de devoir
	def setNoteDevoir(self):
		print("Note de devoir")
		for eleve in self.listEleves:
			note = input("> "+eleve.getNom()+" : ")
			eleve.setNoteDevoir(float(note))
	
	#Sauvegarder les données dans un fichier
	def sauvegarder(self, filename):
		#Trier la liste des élèves
		self.sort()
		#Récuperer nom du fichier
		filename = filename.split("/")
		filename = filename[-1]
		#Sauvegarder dans le dossier /output
		filename = "../output/"+filename
		print(filename)
		#Enregistrer les données dans un fichier csv
		f = open(filename, 'w')
		for eleve in self.listEleves:
			ligne = "{};{};{}\n".format(eleve.getNom(),   eleve.getNoteInterro(), eleve.getNoteDevoir())
			f.write(ligne)
		f.close()
	
	#Sauvegarder les données dans un fichier csv avec les moyennes
	def sauvegarderMoyennes(self, filename, coefficient):
		#Trier la liste des élèves
		self.sort()
		#Récuperer nom du fichier
		filename = filename.split("/")
		filename = filename[-1]
		#Sauvegarder dans le dossier /output
		filename = "../output/"+filename
		#Enregistrer les données dans un fichier csv
		f = open(filename, 'w')
		for eleve in self.listEleves:
			ligne = "{};{};{};{};{};{}\n".format(eleve.getNom(),   eleve.getNoteInterro(), eleve.getNoteDevoir(), eleve.moyenneInterro(), eleve.moyenne(), eleve.moyenneCoefficiee(coefficient))
			f.write(ligne)
		f.close()
	
	def afficherClasse(self):
		cpt = 0
		for eleve in self.listEleves:
			cpt += 1
			tableau(cpt, eleve.getNom(), eleve.getNoteInterro(), eleve.getNoteDevoir())
		
	def sauvegarderEnPdf(self, coefficient, filename):
		#Nom du fichier d'exportation en pdf
		nf = filename.split('/')
		nf = nf[-1].split('.')[0]
		nomDocTex = "../output/" + nf +".tex"#Format .tex
		nomDocPdf = "../output/" + nf +".pdf"#Format .pdf
		#Ouverture du fichier document.tex
		f = open(nomDocTex, 'w')
		cpt = 0
		#Contenu du document
		f.write(enteteDocLatex())
		#Nombre d'interro et de devoir
		nbrI = len(self.listEleves[0].getNoteInterro())
		nbrD = len(self.listEleves[0].getNoteDevoir())
		#Tête du tableau
		f.write(titleTab(nbrI, nbrD))
		#Ajouter d'une nouvelle ligne
		f.write(firstLigneTab(nbrI, nbrD))
		for eleve in self.listEleves:
			cpt += 1
			#Ajouter une ligne au tableau
			ligne = tableauLatex(cpt, eleve.getNom(), eleve.getNoteInterro(), eleve.getNoteDevoir(), eleve.moyenneInterro(), eleve.moyenne(), eleve.moyenneCoefficiee(coefficient))
			f.write(ligne)
		#Pied du document
		f.write(piedDocLatex())
		#Fermer le fichier
		f.close()
		
		#Compiler le fichier document.tex
		subprocess.run(["pdflatex", nomDocTex])
		#Déplacer dans le dossier output
		#nf = nf+".pdf"
		subprocess.run(["mv", nf+".pdf", nomDocPdf])
		#Supprimer les fichiers aux et log
		subprocess.run(["rm", nf+".aux", nf+".log"])
		#
		subprocess.run(["xdg-open", nomDocPdf])
	
	
	#Trier la liste des élèves par ordre alphabétique
	def sort(self):
		self.listEleves.sort(key = getNom)



if __name__ == '__main__':
    #eleve = Eleve('Aîchatou', 'Diana')
    classe = Classe()
    classe.setListEleves("classe4emathsc.csv")
    classe.sauvegarderEnPdf()
    
