import sqlite3
insee_db = "insee.db"
conn = sqlite3.connect(insee_db)
c = conn.cursor()

#Drop Adn Create allViews
dropView = "DROP VIEW IF EXISTS allCat"

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
          "utlegales.siren = etablissements.siren "

cat = "create view AllCat as select "
c.execute(cat + BaseRequest)
conn.commit()
conn.close()