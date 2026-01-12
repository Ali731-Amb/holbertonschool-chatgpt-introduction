#!/usr/bin/python3
import sys

for arg in sys.argv[1:]:
    nouveau_texte = arg.replace("a", "@")
    print(nouveau_texte)