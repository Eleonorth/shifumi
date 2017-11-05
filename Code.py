# Création d'un jeu de pierre, papier ciseau
from random import randint
import os
import time  # on importe ce module pour interompre l'exécution aux points-clés


# On crée trois variables : pierre, papier et ciseaux, que nous assimilons à une valeur chiffrée, ce qui simplifiera le code.
rock = 1
paper = 2
scissors = 3
game=1

# On fixe les régles  du jeu, ainsi que le nom en chaine de caractère de chaque variable.
names = {rock: "pierre", paper:"papier", scissors:"ciseaux"}
rules = {rock:scissors,paper:rock, scissors:paper}  # on définit les régles ici, quelle variable est supérieure à l'autre.

player_score=0
computer_score=0    # on démarre avec tous les scores à zéro.


# Définissons une première fonction : play

def play():
    print("Nous allons jouer à pierre, papier, ciseaux!")   # On annonce le jeu
     # On crée une première boucle avec la fonction "game", définie plus loin.
    while game ==1:
        player = move()                 # Première étape : le joueur joue son déplacement (fonction définie plus loin)
        computer = randint(1, 3)         # C'est au tour de l'ordinateur d'effectuer son déplacement. Il jouera un nombre aléatoire compris
                                    # entre 1 et 3 correspondant à chaque variable du jeu.
        results(player, computer)        # la fonction "result" stocke le résultat de la partie
        scores()
        wanna_replay()            # Fonction qui relance le jeu, pour le tour suivant

# Définissons la fonction "move" qui permet au joueur de faire son déplacement

def move():
    while True:                 # On commence la fonction dans une boucle while. Le joueur choisit un chiffre entre 1 et 3 (selon la
                                # définition affichée.
        print                   # Afficher le message suivant
        player=input("Pierre =1\nPapier= 2\nCiseaux=3\nFaites votre choix: ")
        # Demande au joueur de rentrer un chiffre (attention: retourne un string. On attribue la variable "player" à la valeur
        # qu'il rentrera dans l'exécuteur.

        try:                            # nous allons ici gérer les erreurs ou exceptions éventuelles.
            player = int(player)        # on transforme la valeur entrée en un entier
            if player in (1,2,3):       # Ici on vérifie que le joueur a bien entré 1,2 ou 3.
                return player           # Si c'est le cas, la fonction retournera la valeur choisie.
        except ValueError:              # Si l'exception est un ValueError, on affiche le message d'erreur et on relance la boucle.
            pass
        print("Oups, il y a une erreur. Veuillez choisir 1(pierre), 2 (papier) ou 3(ciseaux).")

# Définissons la fonction "result" qui enregistrera les scores
def results(player,computer):   # ici prend deux variables : le score du joueur et le score de l'ordinateur
    print("1...")
    time.sleep(1)               # On lance un petit compte à rebours pour ménager le suspense.
    print("2...")
    time.sleep(2)
    print("3!")
    time.sleep(0.5)
    print("L'ordinateur a choisi {0} !".format(names[computer]))
    # Cette ligne affiche le choix de l'ordinateur grâce à string.format()
    # Le {0} définit l'endroit où nous insérerons le mouvement, que nous avons précédemment défini comme un nombre.
    # Le [computer] indique le code pour chercher le mouvement généré aléatoirement (le nom ayant été défini plus tôt dans la fonction
    # "game", et insérera la valeur générée à la place du {0}.

    global player_score, computer_score
    # "global" permet de modifier la variable, qui peut être utilisée en dehors de cette portion de code.

    # Contrôlons maintenant les résultats du jeu :
    # Premier cas de figure : l'égalité.
    if player == computer:
        print("Egalité!")

    # Deuxième cas de figure : le joueur gagne.
    else:
        if rules[player] == computer:      # Si le mouvement perdant du joueur est égal à celui de l'ordinateur, le joueur gagne.
            print("Votre victoire est assurée!")
            player_score += 1
        else:                              # Dans les autres cas, le pc gagne.
            print("L'ordinateur rit de votre défaite...")
            computer_score += 1

# Nous définissons la fonction "scores"
def scores():
    global player_score, computer_score
    print("POINTS")
    print("Joueur: ", player_score)
    print("Ordinateur: ", computer_score)


# Enfin, définissons la fonction "play again"
def wanna_replay():
    replay_condition = 1
    while replay_condition == 1:
        global game
        game = 1
        answer = input("Voulez-vous continuer à jouer? o/n ")
        if answer in ("o", "O", "oui", "Oui", "OUI"):
            game=1
            return game
            replay_condition=0
        elif answer in ("n", "N", "non", "Non", "NON"):
            print("Merci d'avoir joué avec nous. A la prochaine!")
            game =2
            return game
            replay_condition=0
        else:
            print("Je n'ai pas compris votre réponse.")
            replay_condition = 1


# Et maintenant la partie "exécuteur" :

if __name__== "__main__" :
    play()
    os.system("pause")


