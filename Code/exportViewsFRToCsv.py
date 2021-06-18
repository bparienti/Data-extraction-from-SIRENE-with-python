import sqlite3 as db
import csv

# Run your query, the result is stored as `data`
with db.connect('insee.db') as conn:
    cur = conn.cursor()
    for i in range(1,10):
        sql = "SELECT * FROM Cat_" + str(i) + "_FR"
        cur.execute(sql)
        data = cur.fetchall()

        # Create the csv file
        with open('Cat_'+str(i)+'_FR.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # Add the header/column names
            header = ['siren','siret','categorieJuridiqueUniteLegale','denominationUniteLegale','nomUniteLegale','nomUsageUniteLegale','prenom1UniteLegale','prenomUsuelUniteLegale','denominationUsuelleEtablissement','numeroVoieEtablissement','indiceRepetitionEtablissement','complementAdresseEtablissement','distributionSpecialeEtablissement','typeVoieEtablissement','libelleVoieEtablissement','codePostalEtablissement','codeCommuneEtablissement','codeCedexEtablissement','libelleCedexEtablissement','libelleCommuneEtablissement','libelleCommuneEtrangerEtablissement','libellePaysEtrangerEtablissement','codePaysEtrangerEtablissement']
            writer.writerow(header)
            # Iterate over `data`  and  write to the csv file
            for row in data:
                writer.writerow(row)