#!/usr/bin/python3
import sys

def factorial(n):
    """
    [Description de la fonction] :
    Calcule la factorielle d'un nombre entier de manière récursive. 
    La fonction multiplie l'entier par la factorielle de l'entier précédent 
    jusqu'à atteindre le cas de base (0).

    [Paramètres] :
    n (int) : Le nombre entier positif dont on veut calculer la factorielle.

    [Retourne] :
    int : Le résultat de n! (le produit de tous les entiers de 1 à n). 
          Retourne 1 si n est égal à 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# --- Bloc d'exécution principal ---
if len(sys.argv) > 1:
    try:
        # Conversion de l'argument de la ligne de commande en entier
        nombre = int(sys.argv[1])
        
        if nombre < 0:
            print("Erreur : La factorielle n'est pas définie pour les nombres négatifs.")
        else:
            f = factorial(nombre)
            print(f)
            
    except ValueError:
        print("Erreur : Veuillez fournir un nombre entier valide.")
else:
    print("Usage: python3 script.py <nombre>")