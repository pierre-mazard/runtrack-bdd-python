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
    c.execute("SELECT * FROM animal WHERE id = %s", (id,))
    result = c.fetchone()
    if result :
        print("--------------------") 
        print("Animal déja existant, veuillez entrer un autre id")
        print("--------------------")
        return
    nom = input("Entrez le nom de l'animal : ")
    race = input("Entrez la race de l'animal : ")
    id_cage = input("Entrez l'id de la cage de l'animal : ")
    naissance = input("Entrez la date de naissance de l'animal (YYYY-MM-DD) : ")
    origine = input("Entrez le pays d'origine de l'animal : ")
    c.execute("INSERT INTO animal (id, nom, race, id_cage, naissance, origine) VALUES (%s, %s, %s, %s, %s, %s)", (id, nom, race, id_cage, naissance, origine))
    mydb.commit()
    print("Animal ajouté !")

def supprimer_animal():
    print("--------------------")
    id = input("Entrez l'id de l'animal à supprimer : ")
    print("--------------------")
    c.execute("DELETE FROM animal WHERE id = %s", (id,))
    mydb.commit()
    print("--------------------")
    print("Animal supprimé !")
    print("--------------------")

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
    column_names = [description[0] for description in c.description]
    animals = c.fetchall()
    print("--------------------")
    print(f"Nombre total d'animaux : {len(animals)}")
    print("--------------------")
    for animal in animals:
        for name, attribute in zip(column_names, animal):
            print(f"{name} : {attribute}")
        print("--------------------")


def montrer_cage():
    id_cage = input("Entrez l'id de la cage : ")
    c.execute("SELECT * FROM cage WHERE id = %s", (id_cage,))
    animals = c.fetchall()
    for animal in animals:
        print("--------------------")
        print(animal)
        print("--------------------")

def superficie_totale_cages():
    c.execute("SELECT SUM(superficie) FROM cage")
    superficie = c.fetchone()[0]
    print("--------------------")
    print(f"La superficie totale des cages est de {superficie} m².")
    print("--------------------")

def superficie_moyenne_cages():
    c.execute("SELECT AVG(superficie) FROM cage")
    superficie = c.fetchone()[0]
    print("--------------------")
    print(f"La superficie moyenne des cages est de {superficie} m².")
    print("--------------------")

def ajouter_cage():
    id = input("Entrez l'id de la cage : ")
    superficie = input("Entrez la superficie de la cage : ")
    capacite_max = input("Entrez la capacité maximale de la cage : ")
    c.execute("INSERT INTO cage (id, superficie, capacite_max) VALUES (%s, %s, %s)", (id, superficie, capacite_max))
    mydb.commit()
    print("--------------------")
    print("Cage ajoutée !") 
    print("--------------------")

def supprimer_cage():
    id = input("Entrez l'id de la cage à supprimer : ")
    c.execute("DELETE FROM cage WHERE id = %s", (id,))
    mydb.commit()
    print("--------------------")
    print("Cage supprimée !")  
    print("--------------------")

def modifier_cage():
    id = input("Entrez l'id de la cage à modifier : ")
    superficie = input("Entrez la nouvelle superficie de la cage : ")
    capacite_max = input("Entrez la nouvelle capacité maximale de la cage : ")
    c.execute("INSERT INTO cage (id, superficie) VALUES (%s, %s)", (id, superficie))
    mydb.commit()
    print("--------------------")
    print("Cage modifiée !")
    print("--------------------")
    
while True:
    print("1. Ajouter un animal")
    print("2. Supprimer un animal")
    print("3. Modifier un animal")
    print("4. Afficher tous les animaux")
    print("5. Afficher les animaux dans une cage")
    print("6. Calculer la superficie totale des cages")
    print("7. Calculer la superficie moyenne des cages")
    print("8. Ajouter une cage")
    print("9. Supprimer une cage")
    print("10. Modifier une cage")
    print("11. Quitter")
    choice = input("Choisissez une option : ")
    if choice == "1":
        ajouter_animal()
    elif choice == "2":
        supprimer_animal()
    elif choice == "3":
        modifier_animal()
    elif choice == "4":
        montrer_animal()
    elif choice == "5":
        montrer_cage()
    elif choice == "6":
        superficie_totale_cages()
    elif choice == "7":
        superficie_moyenne_cages()
    elif choice == "8":
        ajouter_cage()
    elif choice == "9":
        supprimer_cage()
    elif choice == "10":
        modifier_cage
    elif choice == "11":    
        break
c.close
mydb.close()
