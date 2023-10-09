

'''
Ensemble de fonctions supplémentaires

Clément Adandé 
07 oct 2023
'''
#****************************************************
#Convertir un string de liste de nombres en liste
def stringListToList(liste):
	#liste est un string contenant une liste de nombres
	#Par exemple, liste = "[10,12,0]"
	if liste == "[]":
		liste = []
	else:
		liste = liste[1:-1]#Retirer les crochets
		liste = liste.split(',')#découper en liste avec la virgule
		liste = [float(n) for n in liste]#convert each item to float
	return liste

#*****************************************************
#Retourner nom de l'élève
def getNom(eleve):
	return eleve.getNom()

#*****************************************************
#Gérer l'affichage des données
def separateur(string = ''):
	N = 40
	liste = string.split('\n')
	M = max([len(l) for l in liste])
	if N >= M:
		print('**'+('*'*N)+'**')
		for i in range(len(liste)):
			M = len(liste[i])
			R = N-M-1
			print('**'+' '+liste[i]+(' '*R)+'**')
		print('**'+'*'*N+'**')
	else :
		print('**'+('*'*M)+'**')
		for i in range(len(liste)):
			m = len(liste[i])
			R = M-m+1
			print('*'+' '+liste[i]+(' '*R)+'*')
		print('**'+'*'*M+'**')

#*****************************************************
#Créer un tableau
def tableau(num, nom, interro, devoir):
	nC1 = 25
	nC2 = 7
	N = len(nom)
	string = f"{num}. {nom}"+(" "*(nC1-N))+'*'
	for i in range(len(interro)):
		l = len(str(interro[i]))
		string += f" {interro[i]}"+" "*(nC2-l)
	string += '*'
	for i in range(len(devoir)):
		string += f" {devoir[i]} "
	print(string)

def tableauLatex(num, nom, interro, devoir, m1 = 0, m2 = 0, m3 = 0):
	string = f"{num}&{nom}"
	for i in range(len(interro)):
		string += f"&{interro[i]}"
	for i in range(len(devoir)):
		string += f"&{interro[i]}"
	string += f"&{m1}&{m2}&{m3}"
	string +="\\\\ \\hline\n"
	return string

def enteteDocLatex():
	separateur("Renseignez ces champs pour exporter les fichiers" )
	trimestre = input("Trimestre (ex premier, deuxième, trimestre) : ")
	annee = input("Année-scolaire (ex 2022 - 2023) : ")
	etablissement = input("Etablissement : ")
	classe = input("Classe (ex 5e C) : ")
	discipline = input("Discipline (ex Mathématiques) : ")
	coefficient = input("Coefficient (ex 3) : ")
	
	#***********************************************************
	textdoc = "\\documentclass{article}\n\\usepackage[upright]{fourier}\n\\usepackage{tabulary}\n"
	textdoc += "\\usepackage[margin=2.5cm]{geometry}\n\\begin{document}\n"
	textdoc += "%************************************************\n\n"
	textdoc += "\\begin{center}\n\n\\textbf{\\textsc{Fiche de notes du "
	textdoc += f"{trimestre} "#form
	textdoc += "trimestre}}\n\n"
	textdoc += "\\end{center}\n\n\\medskip\n\n"
	textdoc +="\\textbf{Année scolaire :} "
	textdoc += f"{annee}\n\n"#form
	textdoc += "\\textbf{Etablissement :} "
	textdoc += f"{etablissement}\n\n"
	textdoc += "\\textbf{Classe :} "
	textdoc += f"{classe}\n\n"#form
	textdoc += "\\textbf{Discipline :} "
	textdoc += f"{discipline}\n\n"#form
	textdoc += "\\textbf{Coefficient :} "
	textdoc += f"{coefficient}\n\n"#form
	textdoc += "\\begin{center}"
	
	return textdoc

#
def titleTab(nbrI, nbrD):
	tab = "\\begin{tabular}{|c|p{5cm}|*"
	tab += f"{nbrI}"#form
	tab += "{c|}*"
	tab += f"{nbrD}"#form
	tab += "{c|}c|c|c|}\n\\hline\n"
	return tab

#Ligne du tableau
def firstLigneTab(nbrI, nbrD):
		#Ajouter l'en-tête du tableau
		title = "N\\char6 & Nom et prénom & \\multicolumn{"
		title += f"{nbrI}"#form
		title += "}{c|}{Interrogations} & \\multicolumn{"
		title += f"{nbrD}"#form
		title += "}{c|}{Devoirs}&Moy. Interro.& Moy. tot. & Moy. coeff.\\\\\\hline\\hline\n"
		return title
	
def piedDocLatex():
	return "\\end{tabular}\n\end{center}\n\\end{document}"

if __name__ == '__main__':
	#separateur("Bienvenu.e sur NoteClass")

	#separateur("Menu\n1. Créer une classe\n2. Charger une classe\n3. Quitter")

	#separateur("Programme de gestion de notes d'une discipline\nExport des données aux formats csv et pdf\n")
	
	print(tableauLatex(1, "Carl", [12.5, 16.23, 10.0], [19, 10]))
	
	
