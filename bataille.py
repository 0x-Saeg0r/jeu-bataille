# Importation des classes nécessaires
from cartes import *
from joueurs import *
from jeucartes import *

# Définition de la classe Bataille


class Bataille:
    # Initialisation de la partie
    def __init__(self, nbJoueurs=2, nbCartes=52, cartesParJoueur=26):
        # Nombre de joueurs
        self.nbJoueurs = nbJoueurs
        # Nombre de cartes dans le jeu
        self.nbCartes = nbCartes
        # Création et mélange du jeu de cartes
        self.jeu = JeuCartes(nbCartes)
        self.jeu.creerJeu()
        self.jeu.melanger()
        # Création des joueurs
        self.joueurs = [Joueur("Joueur " + str(i+1)) for i in range(nbJoueurs)]
        # Distribution des cartes aux joueurs
        jeu = self.jeu.distribuerJeu(nbJoueurs, cartesParJoueur)
        for j in range(nbJoueurs):
            self.joueurs[j].setMain(jeu[j])
        # Initialisation du tas de cartes
        self.tas = []
        self.partiesMax = 1000
        self.parties = 0

    def lireTas(self):
        return [(carte.getNom(), carte.getCouleur()) for carte in self.tas]

    # Fonction pour jouer une partie
    def jouer(self):
        partie = True
        while partie == True and self.parties < self.partiesMax:
            
                    
            tasValeurs = []
            self.tas = []

            for i in range(self.nbJoueurs):
                carteJouee = self.joueurs[i].jouerCarte()
                self.tas.append(carteJouee)
                tasValeurs.append(carteJouee.getValeur())

            if tasValeurs.count(max(tasValeurs)) > 1:
                print("############## Bataille ! ##############")
                partie = False
                
            else:
                winner = tasValeurs.index(max(tasValeurs))

                print(f"Le joueur {self.joueurs[winner].getNom()} a gagné le tour. Le tas était {self.lireTas()}")

                for j in range(len(self.tas)):
                    self.joueurs[winner].insererMain(self.tas[j])

            for k in range(self.nbJoueurs):
                if self.joueurs[k].getNbCartes() == 0:
                    print("Le joueur", self.joueurs[k].getNom(), "a perdu !")
                    partie = False
                else:
                    print("Le joueur", self.joueurs[k].getNom(), "a", self.joueurs[k].getNbCartes(), "cartes.")
            self.parties +=1
            
            if self.parties == self.partiesMax:
                print("Nombre de parties maximum atteint !")

# Création d'une partie de bataille avec 2 joueurs par défaut
jeu = Bataille(2,52,2)
# Lancement de la partie
jeu.jouer()
