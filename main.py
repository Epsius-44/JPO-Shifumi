def main():
    relance_partie = True
    while relance_partie:
        saisie = input('Voulez vous lancer une partie de Pierre / Feuille / Ciseaux ? (O)ui / (N)on : ').upper()
        if saisie in ['O', 'N']:
            if saisie == 'O':
                # Boucle de jeu
                return 0
            else:
                relance_partie = False
        else:
            print("Saisie incorrect !")


main()
