NoteClass permet de gérer les notes d'une classe dans une matière donnée.
Conçu selon les règles de calculs de moyenne au Bénin, il peut être modifié.

**Mode usage**
L'interface de NoteClass est assez simple à comprendre
Il peut être utilisé soit en créant une classe soit en chargeant un fihcier csv.
Pour une première fois, il faut créer une classe. Et pour les autres fois, charg
er simplement un fichier (spécifier le chemin du fichier).

Il suffit d'éxecuter le fichier /codes/noteclass.py pour utiliser NoteClass.

**Exporter les données**
Les données sont exportées au format .csv, .tex et .pdf. Les fichiers sont créés quand vous calculer la moyenne totale et le fichier .csv lorsque vous arrêtez le programme. Ils sont placés dans le dossier /output. 



**Formule de calcul**
La moyenne des interrogation (MI) est obtenu en faisant la somme des interrogations divisée par le nombre d'interrogations renseignées.

La moyenne totale (MT) est calculée est obtenu en faisant la somme de MI et des notes de devoirs (deux devoirs sont prévus par trimestre) divisée par 3.

****
