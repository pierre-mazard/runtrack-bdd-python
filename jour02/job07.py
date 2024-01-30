import mysql.connector

#Création de la connexion à la base de données
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root!',
    database='Job07'
)

#Création du curseur
cursor = cnx.cursor()   

#Création de la requête 1
cursor.execute("SELECT * FROM employe WHERE salaire > 3000")

#Récupération des données
result1 = cursor.fetchall()

#Création de la liste des noms
noms = [f"{nom[1]} {nom[2]}" for nom in result1]

#Affichage des données
print(f"Les employés dont le salaire est supérieur à 3000 € sont :")
for nom in noms:
    print(nom)

# Création de la requête 2
cursor.execute("SELECT employe.nom, employe.prenom, service.nom AS service FROM employe JOIN service ON employe.id_service = service.id") 

# Récupération des données 
result2 = cursor.fetchall()

# Création d'un tableau des données
tableau = [[f"{nom[0]} {nom[1]}", nom[2]] for nom in result2]

# Affichage des données
print("\n")
print(f"Les employés et leur service sont :")
for nom, service in tableau:
    print(f"{nom} - {service}")

#Fermeture du curseur
cursor.close()

#Fermeture de la connexion
cnx.close()