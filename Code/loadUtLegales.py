import sqlite3
insee_db = "insee.db"
conn = sqlite3.connect(insee_db)
c = conn.cursor()
dropTableutlegales = "DROP TABLE IF EXISTS utlegales"
c.execute(dropTableutlegales)
c.execute("CREATE TABLE utlegales (siren Texte, prenom1UniteLegale Texte, prenomUsuelUniteLegale Texte, etatAdministratifUniteLegale Texte, nomUniteLegale Texte, nomUsageUniteLegale Texte, denominationUniteLegale Texte, categorieJuridiqueUniteLegale Texte)")

conn.commit()
counter = 0
db_list = []
with open("StockUniteLegale_utf8.csv", encoding='utf8') as infile:
    for line in infile:
        #if (counter > 5):
        #    break

        line = line.replace('"', '')
        data = line.split(",")
        if (counter > 0):
            if (data[20] == 'A'):
                siren = str(data[0])
                prenom1UniteLegale = str(data[6])
                prenomUsuelUniteLegale = str(data[10])
                etatAdministratifUniteLegale = str(data[20])
                nomUniteLegale = str(data[21])
                nomUsageUniteLegale = str(data[22])
                denominationUniteLegale = str(data[24])
                categorieJuridiqueUniteLegale = str(data[27])
               # print (siren + " " + prenom1UniteLegale +" " + prenomUsuelUniteLegale + " " + etatAdministratifUniteLegale +" " +nomUniteLegale + " " +  nomUsageUniteLegale + " " +denominationUniteLegale + " " + categorieJuridiqueUniteLegale)
                db_list.append((siren, prenom1UniteLegale, prenomUsuelUniteLegale, etatAdministratifUniteLegale, nomUniteLegale, nomUsageUniteLegale, denominationUniteLegale, categorieJuridiqueUniteLegale))

        counter += 1
        # print("Name: " + data[6] + " " + data[7] + " " + data[5])
        # print("Legal Name: " + data[4])
        # print(data[22], data[23])
        # print("\n\n")
        # print(line)
        # if counter == 5:
        #    break

    print(len(db_list))
    c.executemany("INSERT INTO utlegales VALUES (?, ?, ?, ?, ?, ?, ?, ?)", db_list)

    conn.commit()
    conn.close()