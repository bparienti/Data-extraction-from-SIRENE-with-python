
# Data-extraction-from-SIRENE-with-python

## Introduction
Concernant la base SIRENE, l'INSEE, fournit des exports de sa base au format CSV

On les trouve à cette adresse : [Base SIRENE](https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/)

Ces exports sont extrêmement volumineux :

 - StockUniteLegale pèse zipé pret de 1Go 
 - StockEtablissement zipé pret de 1,3Go

Dans ce contexte il a fallut trouver une solution pour ouvrir et sortir de ces fichiers des listes de données nous concernant :

 - Seulement les données actives, 
 - Dans toutes les catégories,  
 - Des entreprises françaises
 - Des entreprises étrangères

Exploiter des fichiers de cette taille avec Excel et power query, n'est pas fiable et surtout pas réalisable.

Exploiter des fichiers dans une base de données mySQL ? Non après 1ers test, mysql ne répondait plus : table de + de 20 GO

La solution a donc été de lire ce fichier via un script PYTHON, de créer des Tables et Vues avec justes les données souhaitées

Merci d'être indulgent, je n'avait jamais fait de python avant ca, je suis sur qu'on peut faire beaucoup mieux.

## Description de la solution
Outils utilisés :
- python 3.8.3
- IDE : pyCharm
- DB Browser (SQLite)

=> Tous ces outils sont en free ware



Sources :
- fichier stockUnitéLégale_utf8.csv (en provenance de l'INSEE)
- fichier stockEtablissement_utf8.csv (en provenance de l'INSEE)

## Description des fichiers :
### loadEtablissements.py 
Charge tous les établissements actifs (et seulements les colonnes souhaitées) dans la base Insee.db, dans la table 'etablissements'

### loadUtLegales.py :
Charge toutes les unités légales actives (et seulements les colonnes souhaitées) dans la base Insee.db, dans la table 'utLegales'

### CreateViewFR.py  :
Crée toutes les vues FR des ut légales et leurs établissements associées localisées en france

### createViewETR.py :
crée toutes les vues ETR des ut légales et leurs établissements associées localisées à l'étranger

### createViewAllCat.py :
crée une vue des ut légales et leurs établissements associés => permet de créer des requêtes pour vériffier la taille du contenu des colonnes importées tout critères confondus

### exportViewsFR.py :
export toutes les vues FR dans un fichier portant le même nom que la vue dans un .CSV

### exportViewsETR.py :
export toutes les vues ETR dans un fichier portant le même nom que la vue dans un .CSV


ATTENTION :  ces programmes sont a exécuter dans cet ordre :

 1. tous les load[...].csv 
 2. tous les create[...].csv 
 3. tous les export[...].csv

Sortie :
- les fichiers CSV
- la base SQLite3 insee.db



Les données explotables sorties de Sirene 
18 fichiers / catégories :

9 Fichiers / catégories des entreprises Françaises
9 Fichiers / catégories des entreprises étrangères
