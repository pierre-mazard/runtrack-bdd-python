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

def ajouter_animal():
    id = input("Entrez l'id de l'animal : ")
    nom = input("Entrez le nom de l'animal : ")
    race = input("Entrez la race de l'animal : ")
    id_cage = input("Entrez l'id de la cage de l'animal : ")
    naissance = input("Entrez la date de naissance de l'animal (YYYY-MM-DD) : ")
    origine = input("Entrez le pays d'origine de l'animal : ")
    c.execute("INSERT INTO animal (id, nom, race, id_cage, naissance, origine) VALUES (%s, %s, %s, %s, %s, %s)", (id, nom, race, id_cage, naissance, origine))
    mydb.commit()
    print("Animal ajouté !")

def supprimer_animal():
    id = input("Entrez l'id de l'animal à supprimer : ")
    c.execute("DELETE FROM animal WHERE id = %s", (id,))
    mydb.commit()
    print("Animal supprimé !")

def modifier_animal():
    id = input("Entrez l'id de l'animal à modifier : ")
    nom = input("Entrez le nouveau nom de l'animal : ")
    race = input("Entrez la nouvelle race de l'animal : ")
    id_cage = input("Entrez le nouvel id de la cage de l'animal : ")
    naissance = input("Entrez la nouvelle date de naissance de l'animal (YYYY-MM-DD) : ")
    origine = input("Entrez le nouveau pays d'origine de l'animal : ")
    c.execute("INSERT INTO ANIMAL (id, nom, race, id_cage, naissance, origine) VALUES (%s, %s, %s, %s, %s, %s)", (id, nom, race, id_cage, naissance, origine))
    mydb.commit()
    print("Animal modifié !")

def montrer_animal():
    c.execute("SELECT * FROM animal")
    animals = c.fetchall()
    for animal in animals:
        print(animal)

def montrer_cage():
    id_cage = input("Entrez l'id de la cage : ")
    c.execute("SELECT * FROM cage WHERE id = %s", (id_cage,))
    animals = c.fetchall()
    for animal in animals:
        print(animal)

def superficie_totale_cages():
    c.execute("SELECT SUM(superficie) FROM cage")
    superficie = c.fetchone()[0]
    print(f"La superficie totale des cages est de {superficie} m².")

def superficie_moyenne_cages():
    c.execute("SELECT AVG(superficie) FROM cage")
    superficie = c.fetchone()[0]
    print(f"La superficie moyenne des cages est de {superficie} m².")

def ajouter_cage():
    id = input("Entrez l'id de la cage : ")
    superficie = input("Entrez la superficie de la cage : ")
    capacite_max = input("Entrez la capacité maximale de la cage : ")
    c.execute("INSERT INTO cage (id, superficie) VALUES (%s, %s)", (id, superficie))
    mydb.commit()
    print("Cage ajoutée !") 

def supprimer_cage():
    id = input("Entrez l'id de la cage à supprimer : ")
    c.execute("DELETE FROM cage WHERE id = %s", (id,))
    mydb.commit()
    print("Cage supprimée !")  

def modifier_cage():
    id = input("Entrez l'id de la cage à modifier : ")
    superficie = input("Entrez la nouvelle superficie de la cage : ")
    capacite_max = input("Entrez la nouvelle capacité maximale de la cage : ")
    c.execute("INSERT INTO cage (id, superficie) VALUES (%s, %s)", (id, superficie))
    mydb.commit()
    print("Cage modifiée !")

