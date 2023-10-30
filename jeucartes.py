# Importation de la classe Carte et du module random
from cartes import *
import random


# Définition de la classe JeuCartes
class JeuCartes:
    # Constructeur de la classe JeuCartes
    def __init__(self, nbCartes=52):
        # Vérification que le nombre de cartes est correct
        if nbCartes not in [32, 52]:
            raise Exception(
                "Nombre de cartes incorrect, seuls 32 ou 52 sont acceptés")
        # Initialisation des attributs de la classe
        self.jeu = []  # Liste des cartes du jeu
        self.nbCartes = nbCartes  # Nombre de cartes dans le jeu

    # Définition des méthodes d'instances de la classe JeuCartes

    # Méthode qui retourne le nombre de cartes dans le jeu
    def getTailleJeu(self):
        """ Fonction qui retourne le nombre de cartes dans le jeu
        Valeur retournée de type int"""
        return self.nbCartes

    # Méthode qui crée la liste des cartes du jeu
    def creerJeu(self):
        """Crée la liste des cartes de l'attribut self.jeu"""
        # Si le jeu contient 32 cartes
        if self.getTailleJeu() == 32:
            # Création de la liste des cartes avec les noms et couleurs correspondants
            self.jeu = [Carte(carte, couleur)
                        for carte in noms32 for couleur in couleurs]
        # Si le jeu contient 52 cartes
        else:
            # Création de la liste des cartes avec les noms et couleurs correspondants
            self.jeu = [Carte(carte, couleur)
                        for carte in noms for couleur in couleurs]
        # Retourne la liste des cartes créées
        return self.jeu

    # Méthode qui retourne la liste des cartes du jeu
    def getJeu(self):
        """ Renvoie la liste des cartes correspondant à l'attribut self.jeu
        Valeur retournée de type list"""
        return self.jeu

    # Méthode qui mélange les cartes du jeu
    def melanger(self):
        """ Mélange les cartes du jeu"""
        random.shuffle(self.jeu)

    # Méthode qui distribue une carte à un joueur
    def distribuerCarte(self):
        """Cette fonction permet de distribuer une carte à un joueur.
        Valeur retournée : Objet de type Carte"""
        # Retourne une carte aléatoire de la liste des cartes du jeu
        return self.getJeu().pop(random.randint(0, len(self.getJeu())-1))

    # Méthode qui distribue un nombre de cartes à un nombre de joueurs
    def distribuerJeu(self, nbJoueurs, nbCartes):
        """Cette méthode distribue un nombre de carte nbCartes à un nombre de joueurs nbJoueurs.
        Dans la liste jeuDistribué, chaque élément est une liste de cartes distribuées à un joueur.
        Valeur retournée : type list"""
        # Vérification que le nombre de cartes à distribuer ne dépasse pas le nombre de cartes dans le jeu
        if nbJoueurs * nbCartes > self.getTailleJeu():
            print(
                f"Impossible de distribuer {nbCartes} cartes à {nbJoueurs} joueurs, le jeu ne contient que {self.getTailleJeu()} cartes")
        else:
            # Création d'une liste de listes pour stocker les cartes distribuées à chaque joueur
            jeuDistribué = [[] for j in range(nbJoueurs)]
            cartesDistribuées = 0
            # Tant que toutes les cartes n'ont pas été distribuées
            while cartesDistribuées < nbCartes:
                # Pour chaque joueur
                for i in range(nbJoueurs):
                    # Ajout d'une carte à la liste des cartes distribuées au joueur i
                    jeuDistribué[i].append(self.distribuerCarte())
                # Incrémentation du nombre de cartes distribuées
                cartesDistribuées += 1
            # Retourne la liste des cartes distribuées à chaque joueur
            return jeuDistribué


# Fonction de test de la classe JeuCartes
def testJeuCartes():
    """Test de la création d'un jeu, avec :
            - La création de cartes
            - 52 cartes
            - Un nombre de joueurs et de cartes à distribuer correct
            - Un nombre de joueurs et de cartes à distribuer incorrect"""
    # Création d'un jeu de 52 cartes
    jeu52 = JeuCartes(52)
    # Création de la liste des cartes du jeu
    L = jeu52.creerJeu()
    # Mélange des cartes du jeu
    jeu52.melanger()
    # Affichage des informations de la 3ème carte de la liste des cartes du jeu
    carte = L[2]
    print("Nom : ", carte.getNom())
    print("Couleur : ", carte.getCouleur())
    print("Valeur : ", carte.getValeur())

    # Distribution de 4 cartes à 3 joueurs
    distribution_3j_4c = jeu52.distribuerJeu(3, 4)
    for i in range(3):
        print("Joueur", i+1, ":")
        listeCartes = distribution_3j_4c[i]
        for c in listeCartes:
            print(c.getNom(), "de", c.getCouleur())
        print("\n")
    # Distribution de 10 cartes à 6 joueurs
    distribution_6j_10c = jeu52.distribuerJeu(6, 10)
