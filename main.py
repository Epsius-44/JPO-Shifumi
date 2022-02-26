import src.functions as shifumi

# Variables globales
options = ['Pierre', 'Feuille', 'Ciseaux']
score = [0, 0]


# saisie : 0 pour Pierre, 1 pour Feuille, 2 pour Ciseaux
def test_gagnant(nom_j1, saisie_j1, nom_j2, saisie_j2, game_score):
    if saisie_j1 == saisie_j2:
        print('Égalité ! Personne ne gagne de point.')
    elif saisie_j1 == 1 and saisie_j2 == 3:
        print(f'{nom_j1} gagne la manche !')
        game_score[0] += 1
    elif saisie_j2 == 1 and saisie_j1 == 3:
        print(f'{nom_j2} gagne la manche !')
        game_score[1] += 1
    elif saisie_j1 > saisie_j2:
        print(f'{nom_j1} gagne la manche !')
        game_score[0] += 1
    else:
        print(f'{nom_j2} gagne la manche !')
        game_score[1] += 1
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
