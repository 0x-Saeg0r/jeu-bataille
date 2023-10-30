# Définition des variables globales
couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE') # Tuple contenant les couleurs des cartes
noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As'] # Liste contenant les noms des cartes
noms32 = ['7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As'] # Liste contenant les noms des cartes pour un jeu de 32 cartes
valeurs = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8,
           '9' : 9, '10' : 10, 'Valet' : 11, 'Dame' : 12, 'Roi' : 13, 'As' : 14} # Dictionnaire contenant les valeurs des cartes

# Définition de la classe Carte
class Carte:
    def __init__(self, nom, couleur):
        """Constructeur de la classe Carte
        nom : str, nom de la carte
        couleur : str, couleur de la carte"""
        if nom not in noms: # Vérification que le nom est correct
            raise Exception("Nom incorrect")
        elif couleur not in couleurs: # Vérification que la couleur est correcte
            raise Exception("Couleur incorrecte")
        else:
            self.nom = nom
            self.couleur = couleur
            self.valeur = valeurs[nom] # Récupération de la valeur de la carte dans le dictionnaire valeurs
        
    # Définition des méthodes d'instances avec contrôle
    def setNom(self, nom): # Setter pour le nom
        """Méthode permettant de modifier le nom de la carte
        nom : str, nouveau nom de la carte"""
        if nom not in noms: # Vérification que le nom est correct
            raise Exception("Nom incorrect")
        else:
            self.nom = nom
            self.valeur = valeurs[nom] # Mise à jour de la valeur de la carte
            
    def getNom(self): # Getter pour le nom
        """Méthode permettant de récupérer le nom de la carte"""
        return self.nom
    
    def getCouleur(self): # Getter pour la couleur
        """Méthode permettant de récupérer la couleur de la carte"""
        return self.couleur
    
    def getValeur(self): # Getter pour la valeur
        """Méthode permettant de récupérer la valeur de la carte"""
        return self.valeur
    
    def estSuperieureA(self, carte): 
        """Méthode permettant de comparer la valeur de la carte actuelle avec celle d'une autre carte
        carte : Carte, carte à comparer"""
        if self.getValeur() > carte.getValeur():
            return True
        else:
            return False
        
    def estInferieureA(self, carte):
        """Méthode permettant de comparer la valeur de la carte actuelle avec celle d'une autre carte
        carte : Carte, carte à comparer"""
        if self.getValeur() < carte.getValeur():
            return True
        else:
            return False        
        
def testCarte():
    """Fonction permettant de tester la classe Carte"""
    valetCoeur = Carte('Valet', 'COEUR') # Création d'une carte
    print("Nom : ", valetCoeur.getNom()) # Affichage du nom de la carte
    print("Couleur : ", valetCoeur.getCouleur()) # Affichage de la couleur de la carte
    print("Valeur : ", valetCoeur.getValeur()) # Affichage de la valeur de la carte
    valetCoeur.setNom('As') # Modification du nom de la carte
    print("Nouveau nom : ", valetCoeur.getNom()) # Affichage du nouveau nom de la carte
    print("Nouvelle valeur : ", valetCoeur.getValeur()) # Affichage de la nouvelle valeur de la carte
    dameCarreau = Carte('DAAAme', 'Caroooot') # Création d'une carte avec des valeurs incorrectes (pour tester l'exception)

print(valeurs["4"])