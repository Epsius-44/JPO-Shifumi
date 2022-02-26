import src.functions as shifumi

# Variables globales
options = ['Pierre', 'Feuille', 'Ciseaux']
score = [0, 0]


def game():
    shifumi.affichage_regles()
    while score[0] != 3 and score[1] != 3:
        saisie_j1, saisie_j2 = shifumi.saisie_joueur('Joueur 1'), shifumi.saisie_joueur('Joueur 2')
        shifumi.affichage_choix('Joueur 1', options[saisie_j1], 'Joueur 2', options[saisie_j2])
    if score[0] == 3:
        print('Bravo joueur 1 vous gagnez la partie')
    else:
        print('Bravo joueur 2 vous gagnez la partie')


def main():
    while True:
        saisie = input('Voulez vous lancer une partie de Pierre / Feuille / Ciseaux ? (O)ui / (N)on : ').upper()
        if saisie in ['O', 'N']:
            if saisie == 'O':
                score[0], score[1] = 0, 0
                game()
            else:
                return 0
        else:
            print('Saisie incorrect !')


main()
