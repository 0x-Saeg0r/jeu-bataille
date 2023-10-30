# Importe les classes Carte et JeuCartes depuis les fichiers cartes.py et jeucartes.py
from cartes import *
from jeucartes import *

# Définit la classe Joueur
class Joueur:
    # Constructeur de la classe Joueur
    def __init__(self, nom, nbCartes=0):
        self.nom = nom
        self.nbCartes = nbCartes
        self.main = []
    
    # Setter pour la main du joueur
    def setMain(self, main):
        self.main = main
        self.nbCartes = len(main)
    
    # Getter pour le nom du joueur
    def getNom(self):
        return self.nom
    
    # Getter pour le nombre de cartes du joueur
    def getNbCartes(self):
        return self.nbCartes
    
    # Méthode pour jouer une carte, retourne la dernière carte du jeu et la supprime de la main du joueur
    def jouerCarte(self):
        if len(self.main) == 0:
            return None
        else:
            value = self.main.pop(-1)
            self.nbCartes = len(self.main)
            return value
    
    # Méthode pour insérer une carte dans la main du joueur, au début de sa main
    def insererMain(self, carte):
        self.main.insert(0, carte)
        self.nbCartes = len(self.main)
    
    # Méthode pour afficher la main du joueur
    def montrerMain(self):
        return [(carte.getNom(), carte.getCouleur()) for carte in self.main]
            
        
# Fonction de test pour la classe Joueur
def testJoueur():
    """ Test de la classe Joueur, on vérifie :
            - la création d'un joueur avec un nom correct
            - la distribution de cartes à un joueur
            - l'affichage du nom et du nombre de cartes d'un joueur
            - l'affichage de la main d'un joueur
            - le fait de jouer une carte
            - le fait d'insérer une carte dans la main d'un joueur"""
    # Crée un joueur avec le nom "Joueur 1"
    joueur1 = Joueur("Joueur 1")
    # Affiche le nom du joueur
    print("Nom : ", joueur1.getNom())
    # Affiche le nombre de cartes du joueur
    print("Nombre de cartes : ", joueur1.getNbCartes())
    # Crée un jeu de 32 cartes, le mélange et distribue les cartes aux joueurs
    jeu32 = JeuCartes(32)
    jeu32.creerJeu()
    jeu32.melanger()
    L = jeu32.distribuerJeu(2, 2)
    # Donne la main du joueur 1
    joueur1.setMain(L[0])
    # Affiche la main du joueur 1
    print("Main du joueur 1 : ", joueur1.montrerMain())
    # Joue une carte et l'affiche
    cJouée = joueur1.jouerCarte()
    print("Carte jouée : ", cJouée.getNom(), cJouée.getCouleur())
    # Insère une carte dans la main du joueur 1 et l'affiche
    joueur1.insererMain(Carte('As', 'PIQUE'))
    print("Main du joueur 1 : ", joueur1.montrerMain())
    
