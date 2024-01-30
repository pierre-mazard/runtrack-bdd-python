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
cursor.execute("SELECT SUM(superficie) FROM etage")

#Récupération des données
result = cursor.fetchone()

#Affichage des données
print(f"La superficie de La Plateforme est de {result[0]} m2")

#Fermeture du curseur
cursor.close()

#Fermeture de la connexion
cnx.close()