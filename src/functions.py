def affichage_regles():
    print('\n==============================================================')
    print('=== Rappel des règles  :')
    print('== - La pierre écrase les ciseaux et gagne.')
    print('== - La feuille enveloppe la pierre et gagne.')
    print('== - Les ciseaux découpent la feuille et gagnent.')
    print('== ')
    print('=== Le premier joueur qui gagne 3 manches gagne la partie')
    print('==============================================================\n')


def affichage_choix(nom_j1, choix_j1, nom_j2, choix_j2):
    print('\n==============================================================')
    print(f'== - Choix {nom_j1} : {choix_j1}')
    print(f'== - Choix {nom_j2} : {choix_j2}')
    print('==============================================================\n')


def affichage_score(nom_j1, nom_j2, score):
    print('\n==============================================================')
    print(f'== - Score {nom_j1} : {score[0]}')
    print(f'== - Score {nom_j2} : {score[1]}')
    print('==============================================================\n')


def affichage_gagnant(nom_j1, nom_j2, score):
    if score[0] == 3:
        print(f'Bravo {nom_j1} vous gagnez la partie')
    else:
        print(f'Bravo {nom_j2} vous gagnez la partie')


def saisie_joueur(nomJoueur):
    while True:
        saisie = input('> ' + nomJoueur + ' \n(1) - Pierre \n(2) - Feuille \n(3) - Ciseaux\nFaites votre choix : ')
        if saisie not in ["1", "2", "3"]:
            print('Proposition incorrecte, veuillez respecter le format souhaité')
        else:
            return int(saisie)
