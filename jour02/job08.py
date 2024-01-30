import mysql.connector

#Connexion à la base de données
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root!",
    database="zoo"
)

#Création d'un curseur
c = mydb.cursor()

def add_animal():
    id = input("Entrez l'id de l'animal : ")
    nom = input("Entrez le nom de l'animal : ")
    race = input("Entrez la race de l'animal : ")
    id_cage = input("Entrez l'id de la cage de l'animal : ")
    naissance = input("Entrez la date de naissance de l'animal : ")
    origine = input("Entrez le pays d'origine de l'animal : ")
    c.execute("INSERT INTO animal (id, nom, race, id_cage, naissance, origine) VALUES (%s, %s, %s, %s, %s, %s)", (id, nom, race, id_cage, naissance, origine))
    mydb.commit()
    print("Animal ajouté !")

def delete_animal():
    id = input("Entrez l'id de l'animal à supprimer : ")
    c.execute("DELETE FROM animal WHERE id = %s", (id,))
    mydb.commit()
    print("Animal supprimé !")