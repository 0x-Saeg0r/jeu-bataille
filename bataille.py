# Importation des classes nécessaires
from cartes import *
from joueurs import *
from jeucartes import *

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
    - jouer(self): joue une partie de la bataille.
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
        self.partiesMax = 100000
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

    def jouer(self):
        """
        Joue une partie de la bataille.

        Args:
        None

        Returns:
        None
        """
        partie = True
        while partie == True and self.parties < self.partiesMax:

            tasValeurs = []
            self.tas = []
            savedTas = []

            for i in range(self.nbJoueurs):
                carteJouee = self.joueurs[i].jouerCarte()
                self.tas.append(carteJouee)
                tasValeurs.append(carteJouee.getValeur())

            if tasValeurs.count(max(tasValeurs)) > 1:
                print("############## Bataille ! ##############")
                savedTas = self.tas
                self.tas = []
                tasValeurs = []
                for k in range(self.nbJoueurs):
                    cartejouee = self.joueurs[k].jouerCarte()
                    self.tas.append(cartejouee)
                    tasValeurs.append(cartejouee.getValeur())
                winner = tasValeurs.index(max(tasValeurs))
                for p in range(len(self.tas)):
                    self.joueurs[winner].insererMain(self.tas[p])
                for q in range(len(savedTas)):
                    self.joueurs[winner].insererMain(savedTas[q])

            else:
                winner = tasValeurs.index(max(tasValeurs))

                print(
                    f"Le joueur {self.joueurs[winner].getNom()} a gagné le tour. Le tas était {self.lireTas()}")

                for j in range(len(self.tas)):
                    self.joueurs[winner].insererMain(self.tas[j])

            for k in range(self.nbJoueurs):
                if self.joueurs[k].getNbCartes() == 0:
                    print("Le joueur", self.joueurs[k].getNom(), "a perdu !")
                    partie = False
                else:
                    print("Le joueur", self.joueurs[k].getNom(
                    ), "a", self.joueurs[k].getNbCartes(), "cartes.")
            self.parties += 1

            if self.parties == self.partiesMax:
                print("Nombre de parties maximum atteint !")


# Création d'une partie de bataille avec 2 joueurs par défaut
jeu = Bataille(2, 52, 26)
# Lancement de la partie
jeu.jouer()
