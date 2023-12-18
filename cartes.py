# Définition des variables globales
# Tuple contenant les couleurs des cartes
couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet',
        'Dame', 'Roi', 'As']  # Liste contenant les noms des cartes
# Liste contenant les noms des cartes pour un jeu de 32 cartes
noms32 = ['7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
           '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}  # Dictionnaire contenant les valeurs des cartes

# Définition de la classe Carte


class Carte:
    def __init__(self, nom, couleur):
        """Constructeur de la classe Carte
        nom : str, nom de la carte
        couleur : str, couleur de la carte"""
        if nom not in noms:  # Vérification que le nom est correct
            raise Exception("Nom incorrect")
        elif couleur not in couleurs:  # Vérification que la couleur est correcte
            raise Exception("Couleur incorrecte")
        else:
            self.nom = nom
            self.couleur = couleur
            # Récupération de la valeur de la carte dans le dictionnaire valeurs
            self.valeur = valeurs[nom]

    # Définition des méthodes d'instances avec contrôle
    def setNom(self, nom):  # Setter pour le nom
        """Méthode permettant de modifier le nom de la carte
        nom : str, nouveau nom de la carte"""
        if nom not in noms:  # Vérification que le nom est correct
            raise Exception("Nom incorrect")
        else:
            self.nom = nom
            self.valeur = valeurs[nom]  # Mise à jour de la valeur de la carte

    def getNom(self):  # Getter pour le nom
        """Méthode permettant de récupérer le nom de la carte"""
        return self.nom

    def getCouleur(self):  # Getter pour la couleur
        """Méthode permettant de récupérer la couleur de la carte"""
        return self.couleur

    def getValeur(self):  # Getter pour la valeur
        """Méthode permettant de récupérer la valeur de la carte"""
        return self.valeur

    # Méthode permettant de comparer la valeur de la carte actuelle avec celle d'une autre carte, 
    # retourne True si la valeur de la carte actuelle est supérieure à celle de la carte passée en paramètre, False sinon
    def estSuperieureA(self, carte):
        """Méthode permettant de comparer la valeur de la carte actuelle avec celle d'une autre carte
        carte : Carte, carte à comparer"""
        if self.getValeur() > carte.getValeur():
            return True
        else:
            return False

    # Méthode permettant de comparer la valeur de la carte actuelle avec celle d'une autre carte, 
    # retourne True si la valeur de la carte actuelle est inférieure à celle de la carte passée en paramètre, False sinon
    def estInferieureA(self, carte):
        """Méthode permettant de comparer la valeur de la carte actuelle avec celle d'une autre carte
        carte : Carte, carte à comparer"""
        if self.getValeur() < carte.getValeur():
            return True
        else:
            return False

# Définition de la fonction testCarte
def testCarte():
    """Fonction permettant de tester la classe Carte"""
    valetCoeur = Carte('Valet', 'COEUR')  # Création d'une carte
    print("Nom : ", valetCoeur.getNom())  # Affichage du nom de la carte
    # Affichage de la couleur de la carte
    print("Couleur : ", valetCoeur.getCouleur())
    # Affichage de la valeur de la carte
    print("Valeur : ", valetCoeur.getValeur())
    valetCoeur.setNom('As')  # Modification du nom de la carte
    # Affichage du nouveau nom de la carte
    print("Nouveau nom : ", valetCoeur.getNom())
    # Affichage de la nouvelle valeur de la carte
    print("Nouvelle valeur : ", valetCoeur.getValeur())
    # Création d'une carte avec des valeurs incorrectes (pour tester l'exception)
    dameCarreau = Carte('DAAAme', 'Caroooot')

testCarte()