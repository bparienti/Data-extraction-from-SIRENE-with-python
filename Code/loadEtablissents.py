import sqlite3
insee_db = "insee.db"
conn = sqlite3.connect(insee_db)
c = conn.cursor()
c.execute("CREATE TABLE etablissements (siren Texte, siret Texte, complementAdresseEtablissement Texte, numeroVoieEtablissement Texte, indiceRepetitionEtablissement Texte, typeVoieEtablissement Texte, libelleVoieEtablissement Texte, codePostalEtablissement Texte, libelleCommuneEtablissement Texte, libelleCommuneEtrangerEtablissement Texte, distributionSpecialeEtablissement Texte, codeCommuneEtablissement Texte, codeCedexEtablissement Texte, libelleCedexEtablissement Texte, codePaysEtrangerEtablissement Texte, libellePaysEtrangerEtablissement Texte, etatAdministratifEtablissement Texte, denominationUsuelleEtablissement Texte)")
conn.commit()
counter = 0
db_list = []
with open("StockEtablissement_utf8.csv", encoding='utf8') as infile:
    for line in infile:
        line = line.replace('"', '')
        data = line.split(",")
        if (counter > 0):
            if (data[40] == 'A'):
                siren = data[0]
                siret = data[2]
                complementAdresseEtablissement = data[11]
                numeroVoieEtablissement = data[12]
                indiceRepetitionEtablissement = data[13]
                typeVoieEtablissement = data[14]
                libelleVoieEtablissement = data[15]
                codePostalEtablissement = data[16]
                libelleCommuneEtablissement = data[17]
                libelleCommuneEtrangerEtablissement = data[18]
                distributionSpecialeEtablissement = data[19]
                codeCommuneEtablissement = data[20]
                codeCedexEtablissement = data[21]
                libelleCedexEtablissement = data[22]
                codePaysEtrangerEtablissement = data[23]
                libellePaysEtrangerEtablissement = data[24]
                etatAdministratifEtablissement = data[40]
                denominationUsuelleEtablissement = data[44]
                db_list.append((siren, siret, complementAdresseEtablissement, numeroVoieEtablissement, indiceRepetitionEtablissement, typeVoieEtablissement, libelleVoieEtablissement, codePostalEtablissement, libelleCommuneEtablissement, libelleCommuneEtrangerEtablissement, distributionSpecialeEtablissement, codeCommuneEtablissement, codeCedexEtablissement, libelleCedexEtablissement, codePaysEtrangerEtablissement, libellePaysEtrangerEtablissement, etatAdministratifEtablissement, denominationUsuelleEtablissement))

        counter += 1
        # print("Name: " + data[6] + " " + data[7] + " " + data[5])
        # print("Legal Name: " + data[4])
        # print(data[22], data[23])
        # print("\n\n")
        # print(line)
        # if counter == 5:
        #    break

    print(len(db_list))
    c.executemany("INSERT INTO etablissements VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )", db_list)

    conn.commit()
    conn.close()