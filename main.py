import src.functions as shifumi

# Variables globales
options = ['Pierre', 'Feuille', 'Ciseaux']
score = [0, 0]


def test_gagnant(nom_j1, saisie_j1, nom_j2, saisie_j2, game_score):
    print('Égalité !')
    return game_score


def game():
    global score
    shifumi.affichage_regles()
    while score[0] != 3 and score[1] != 3:
        saisie_j1 = shifumi.saisie_joueur('Joueur 1')
        saisie_j2 = shifumi.saisie_joueur('Joueur 2')
        shifumi.affichage_choix('Joueur 1', options[saisie_j1], 'Joueur 2', options[saisie_j2])
        score = test_gagnant('Joueur 1', saisie_j1, 'Joueur 2', saisie_j2, score)
        shifumi.affichage_score('Joueur 1', 'Joueur 2', score)
    if score[0] == 3:
        print('Bravo joueur 1 vous gagnez la partie')
    else:
        print('Bravo joueur 2 vous gagnez la partie')


def main():
    global score
    while True:
        saisie = input('Voulez vous lancer une partie de Pierre / Feuille / Ciseaux ? (O)ui / (N)on : ').upper()
        if saisie in ['O', 'N']:
            if saisie == 'O':
                score = [0, 0]
                game()
            else:
                return 0
        else:
            print('Saisie incorrect !')


main()
