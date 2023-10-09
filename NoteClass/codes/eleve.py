#calcul la moyenne d'une liste
def mean(liste):
	m = 0
	if len(liste) == 0:
		m = 0
	else:
		m = round(sum(liste)/len(liste),2)
	return m
	

class Eleve:
	def __init__(self, nom):
		self.nom = nom
		self.noteInterro = []
		self.noteDevoir = []
	
	def getNom(self):
		return self.nom
	
	def getNoteInterro(self):
		return self.noteInterro
	
	def getNoteDevoir(self):
		return self.noteDevoir
	
	#Recevoir une seul note, un float
	def setNoteInterro(self, note):
		if isinstance(note, float):
			self.noteInterro.append(note)
		else:
			self.noteInterro.extend(note)
		
	
	#Recevoir une seul note, un float
	def setNoteDevoir(self, note):
		if isinstance(note, float):
			self.noteDevoir.append(note)
		else:
			self.noteDevoir.extend(note)
	
	#
	def moyenneInterro(self):
		return mean(self.getNoteInterro())
	
	#Moyenne totale
	def moyenne(self):
		m = self.moyenneInterro()
		som = m + sum(self.getNoteDevoir())
		return round(som/3,2);

	def moyenneCoefficiee(self, coefficient = 1):
		return round(coefficient*self.moyenne(),2)



