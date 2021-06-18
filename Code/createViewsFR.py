import sqlite3
insee_db = "insee.db"
conn = sqlite3.connect(insee_db)
c = conn.cursor()

#Drop Adn Create allViews
dropView = "DROP VIEW IF EXISTS allCat"
for i in range(1,10):
    viewToDrop = "Cat_"+str(i)+"_FR"
    c.execute("DROP VIEW IF EXISTS " + viewToDrop)


BaseRequest = " utlegales.siren, " \
          " etablissements.siret, " \
          " utlegales.categorieJuridiqueUniteLegale, " \
          " utlegales.denominationUniteLegale," \
          " utlegales.nomUniteLegale, " \
          " utlegales.nomUsageUniteLegale, " \
          " utlegales.prenom1UniteLegale," \
          " utlegales.prenomUsuelUniteLegale," \
          " etablissements.denominationUsuelleEtablissement," \
          " etablissements.numeroVoieEtablissement," \
          " etablissements.indiceRepetitionEtablissement," \
          " etablissements.complementAdresseEtablissement," \
          " etablissements.distributionSpecialeEtablissement," \
          " etablissements.typeVoieEtablissement," \
          " etablissements.libelleVoieEtablissement," \
          " etablissements.codePostalEtablissement," \
          " etablissements.codeCommuneEtablissement," \
          " etablissements.codeCedexEtablissement," \
          " etablissements.libelleCedexEtablissement," \
          " etablissements.libelleCommuneEtablissement," \
          " etablissements.libelleCommuneEtrangerEtablissement," \
          " etablissements.libellePaysEtrangerEtablissement," \
          " etablissements.codePaysEtrangerEtablissement" \
          " from utlegales, etablissements" \
          " where " \
          "utlegales.siren = etablissements.siren " \
          "and etablissements.codePostalEtablissement is not null" \
          " and etablissements.codePostalEtablissement <> ''"

for j in range(1,10):
    cat = "create view Cat_"+str(j) + "_FR as select "
    catw = " and utlegales.categorieJuridiqueUniteLegale like '"+str(j)+"%' LIMIT 100"
    c.execute(cat + BaseRequest + catw)
    conn.commit()


conn.close()