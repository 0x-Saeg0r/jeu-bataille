#############################################
#              Titre: Bataille              #
#           Auteur : Arthur Le Gall         #
#            Date: 6 Novembre 2023          #
#############################################


# Importation des classes nécessaires
from cartes import *
from joueurs import *
from jeucartes import *
import sys
sys.setrecursionlimit(10000)

# Définition de la classe Bataille
class Bataille:
    """
    Classe représentant le jeu de la bataille.

    Attributes:
    - nbJoueurs (int): le nombre de joueurs dans la partie.
    - nbCartes (int): le nombre de cartes dans le jeu.
    - jeu (JeuCartes): le jeu de cartes utilisé pour la partie.
    - joueurs (list): la liste des joueurs de la partie.
    - tas (list): la liste des cartes jouées lors d'un tour.
    - partiesMax (int): le nombre maximum de parties à jouer.
    - parties (int): le nombre de parties jouées.

    Methods:
    - __init__(self, nbJoueurs=2, nbCartes=52, cartesParJoueur=26): initialise la partie.
    - lireTas(self): retourne une liste de tuples représentant les cartes dans le tas.
    - egalite(self): gère le cas d'égalité entre les joueurs.
    - jouer(self, partie=True): joue une partie de la bataille.
    """

    def __init__(self, nbJoueurs=2, nbCartes=52, cartesParJoueur=26):
        """
        Initialise la partie de la bataille.

        Args:
        - nbJoueurs (int): le nombre de joueurs dans la partie.
        - nbCartes (int): le nombre de cartes dans le jeu.
        - cartesParJoueur (int): le nombre de cartes distribuées à chaque joueur.

        Returns:
        None
        """
        self.nbJoueurs = nbJoueurs
        self.nbCartes = nbCartes
        self.jeu = JeuCartes(nbCartes)
        self.jeu.creerJeu()
        self.jeu.melanger()
        self.joueurs = [Joueur("Joueur " + str(i+1)) for i in range(nbJoueurs)]
        jeu = self.jeu.distribuerJeu(nbJoueurs, cartesParJoueur)
        for j in range(nbJoueurs):
            self.joueurs[j].setMain(jeu[j])
        self.tas = []
        self.partiesMax = 10000
        self.parties = 0

    def lireTas(self):
        """
        Retourne une liste de tuples représentant les cartes dans le tas.

        Args:
        None

        Returns:
        - list: une liste de tuples représentant les cartes dans le tas.
        """
        return [(carte.getNom(), carte.getCouleur()) for carte in self.tas]

    def egalite(self):
        """
        Si les joueurs ont joué une carte de même valeur alors cette méthode est appelée.        
        """
        if self.joueurs[0].getNbCartes() < 2 or self.joueurs[1].getNbCartes() < 2:
            ### Cas où un des joueurs n'a pas assez de cartes pour continuer la partie
            if self.joueurs[0].getNbCartes() == 0 or self.joueurs[1].getNbCartes() == 0:
                print("Fin de jeu, un des joueurs n'a plus de cartes.")
                tasValeurs = []
                for i in self.tas:
                    tasValeurs.append(i.getValeur())
                gagnant = 0 if tasValeurs.index(
                    max(tasValeurs)) % 2 == 0 else 1
                for i in self.tas:
                    self.joueurs[gagnant].insererUneCarte(i)
            ### Cas où il a juste assez pour refaire une bataille
            else:
                print(
                    "Egalité mais un des joueurs n'a pas assez de cartes pour continuer la partie.")
                # Bataille UNE CARTE
                carteJoueur1 = self.joueurs[0].jouerCarte()
                carteJoueur2 = self.joueurs[1].jouerCarte()
                self.tas.append(carteJoueur1)
                self.tas.append(carteJoueur2)
                if carteJoueur1.estSuperieureA(carteJoueur2):
                    for i in self.tas:
                        self.joueurs[0].insererUneCarte(i)
                    self.tas = []
                    print(
                        f"Vainqueur de la manche: {self.joueurs[0].getNom()}, ({self.joueurs[0].getNbCartes()}, {self.joueurs[1].getNbCartes()}, {self.joueurs[0].getNbCartes() + self.joueurs[1].getNbCartes()}))")
                elif carteJoueur1.estInferieureA(carteJoueur2):
                    for i in self.tas:
                        self.joueurs[1].insererUneCarte(i)
                    print(
                        f"Vainqueur de la manche: {self.joueurs[1].getNom()}, ({self.joueurs[0].getNbCartes()}, {self.joueurs[1].getNbCartes()}, {self.joueurs[0].getNbCartes() + self.joueurs[1].getNbCartes()}))")
                else:
                    self.jouer(False)
        ### Cas où le joueur a assez de cartes pour continuer la partie
        else:
            print("Egalité, bataille !")
            carteJoueur1 = self.joueurs[0].jouerCarte()
            carteJoueur2 = self.joueurs[1].jouerCarte()
            self.tas.append(carteJoueur1)
            self.tas.append(carteJoueur2)
            carteJoueur1 = self.joueurs[0].jouerCarte()
            carteJoueur2 = self.joueurs[1].jouerCarte()
            self.tas.append(carteJoueur1)
            self.tas.append(carteJoueur2)
            if carteJoueur1.estSuperieureA(carteJoueur2):
                for i in self.tas:
                    self.joueurs[0].insererUneCarte(i)
                self.tas = []
                print(
                    f"Vainqueur de la manche: {self.joueurs[0].getNom()}, ({self.joueurs[0].getNbCartes()}, {self.joueurs[1].getNbCartes()}, {self.joueurs[0].getNbCartes() + self.joueurs[1].getNbCartes()}))")
            elif carteJoueur1.estInferieureA(carteJoueur2):
                for i in self.tas:
                    self.joueurs[1].insererUneCarte(i)
                self.tas = []
                print(
                    f"Vainqueur de la manche: {self.joueurs[1].getNom()}, ({self.joueurs[0].getNbCartes()}, {self.joueurs[1].getNbCartes()}, {self.joueurs[0].getNbCartes() + self.joueurs[1].getNbCartes()}))")
            else:
                self.egalite()

    def jouer(self, partie=True):
        """
        Joue une partie de la bataille.

        Args:
        - partie (bool): True si c'est le début de la partie, False sinon.

        Returns:
        None
        """
        # Vérification que la partie n'est pas terminée
        if partie:
            print(
                f"Début de la partie. ({self.joueurs[0].getNbCartes()}, {self.joueurs[1].getNbCartes()}, {self.joueurs[0].getNbCartes() + self.joueurs[1].getNbCartes()})")
            # Création des cartes
            carteJoueur1 = self.joueurs[0].jouerCarte()
            carteJoueur2 = self.joueurs[1].jouerCarte()
            # Vérification des cartes et assignation en conséquence
            if carteJoueur1.estSuperieureA(carteJoueur2):
                self.joueurs[0].insererMain(carteJoueur1, carteJoueur2)
                print(
                    f"Vainqueur de la manche: {self.joueurs[0].getNom()}, ({self.joueurs[0].getNbCartes()}, {self.joueurs[1].getNbCartes()}, {self.joueurs[0].getNbCartes() + self.joueurs[1].getNbCartes()}))")
            elif carteJoueur1.estInferieureA(carteJoueur2):
                self.joueurs[1].insererMain(carteJoueur2, carteJoueur1)
                print(
                    f"Vainqueur de la manche: {self.joueurs[1].getNom()}, ({self.joueurs[0].getNbCartes()}, {self.joueurs[1].getNbCartes()}, {self.joueurs[0].getNbCartes() + self.joueurs[1].getNbCartes()}))")
            else:
                self.tas.append(carteJoueur1)
                self.tas.append(carteJoueur2)
                self.egalite()
        # Vérification que la partie n'est pas terminée
        if self.parties < self.partiesMax and self.joueurs[0].getNbCartes() > 0 and self.joueurs[1].getNbCartes() > 0:
            self.parties += 1
            self.jouer()
        # Si la partie est terminée
        else:
            print(
                f"Fin de la partie. Le gagnant est le {self.joueurs[0].getNom() if self.joueurs[0].getNbCartes() > 0 else self.joueurs[1].getNom()} avec ses {self.joueurs[0].getNbCartes() if self.joueurs[0].getNbCartes() > 0 else self.joueurs[1].getNbCartes()} cartes.")
            partie = False


# Création d'une partie de bataille avec 2 joueurs par défaut
jeu = Bataille(2, 52, 26)
# Lancement de la partie
jeu.jouer()
