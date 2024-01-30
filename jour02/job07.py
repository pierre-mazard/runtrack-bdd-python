import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.cnx.cursor()

    def create_employe(self, nom, prenom, salaire, id_service):
        self.cursor.execute("""
            INSERT INTO employe (nom, prenom, salaire, id_service)
            VALUES (%s, %s, %s, %s)
        """, (nom, prenom, salaire, id_service))
        self.cnx.commit()

    def read_employe(self, id):
        self.cursor.execute("""
            SELECT * FROM employe WHERE id = %s
        """, (id,))
        return self.cursor.fetchone()

    def update_employe(self, id, nom, prenom, salaire, id_service):
        self.cursor.execute("""
            UPDATE employe
            SET nom = %s, prenom = %s, salaire = %s, id_service = %s
            WHERE id = %s
        """, (nom, prenom, salaire, id_service, id))
        self.cnx.commit()

    def delete_employe(self, id):
        self.cursor.execute("""
            DELETE FROM employe WHERE id = %s
        """, (id,))
        self.cnx.commit()

    def close(self):
        self.cursor.close()
        self.cnx.close()

# Créer une instance de la classe Employe
employe = Employe('localhost', 'root', 'root!', 'Job07')

# Créer un nouvel employé
employe.create_employe('Gimeno', 'Denise', 6580.20, 2)

# Lire les informations d'un employé
print(employe.read_employe(1))

# Mettre à jour les informations d'un employé
employe.update_employe(1, 'Gimeno', 'Denise', 46000.00, 1)

# Lire les informations d'un employé
print(employe.read_employe(1))

# Supprimer un employé
employe.delete_employe(1)

# Fermer la connexion
employe.close()



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