#!/usr/bin/python3
import sys

def factorial(n):
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

f = factorial(int(sys.argv[1]))
print(f)

if len(sys.argv) > 1:
    nombre = int(sys.argv[1])
    f = factorial(nombre)
    print(f"Le résultat de {nombre}! est : {f}")
else:
    print("Erreur : Vous devez entrer un nombre (ex: python factorial.py 10)")