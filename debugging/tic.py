def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)

def verifier_victoire(grille):
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != " ": return True
        if grille[0][i] == grille[1][i] == grille[2][i] != " ": return True
    if grille[0][0] == grille[1][1] == grille[2][2] != " ": return True
    if grille[0][2] == grille[1][1] == grille[2][0] != " ": return True
    return False

def morpion():
    grille = [[" "] * 3 for _ in range(3)]
    joueur = "X"
    coups = 0

    while coups < 9:
        afficher_grille(grille)
        try:
            ligne = int(input(f"Joueur {joueur}, ligne (0, 1, 2) : "))
            colonne = int(input(f"Joueur {joueur}, colonne (0, 1, 2) : "))
            
            if ligne not in range(3) or colonne not in range(3):
                print("Hors limites ! Choisissez 0, 1 ou 2.")
                continue
                
            if grille[ligne][colonne] == " ":
                grille[ligne][colonne] = joueur
                coups += 1
                if verifier_victoire(grille):
                    afficher_grille(grille)
                    print(f"Bravo ! Le joueur {joueur} a gagné !")
                    return
                joueur = "O" if joueur == "X" else "X"
            else:
                print("Case déjà occupée !")
        except ValueError:
            print("Entrée invalide ! Veuillez saisir un chiffre.")

    afficher_grille(grille)
    print("Match nul !")

if __name__ == "__main__":
    morpion()