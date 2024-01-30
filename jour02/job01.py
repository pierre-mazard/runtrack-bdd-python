import mysql.connector

#Création de la connexion à la base de données
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root!',
    database='LaPlateforme'
)

#Création du curseur
cursor = cnx.cursor()   

#Création de la requête
cursor.execute("SELECT * FROM etudiant")

#Récupération des données
result = cursor.fetchall()

#Affichage des données
for etudiant in result:
    print(etudiant)

#Fermeture du curseur
cursor.close()

#Fermeture de la connexion
cnx.close()