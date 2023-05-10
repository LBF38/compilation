# :gear: Cours de compilation

Cours de compilation @ ENSTA Bretagne.

Ce dépôt contient les TPs et le projet de compilation. Vous trouverez ci-dessous les liens vers les différents TPs et le projet.

## :link: Liens vers les TPs

- [TP1](TPs/TPs/TP1/README.md)
- [TP2](TPs/TP2/)
- [TP3](TPs/TP3/)
- [TP4](TPs/TP4/README.md)
- [TP5](TPs/TP5/README.md)

## :link: Lien vers le projet compilation - Code Graph Compiler

Le projet de compilation est disponible dans le dossier `compiler_project`.
Vous pouvez commencer par lire le [README](compiler_project/README.md) du projet.

## :bulb: Problèmes rencontrés

- `ModuleNotFoundError: No module named '<name>'` :
  - Si cela est un module créé par nos soins, il faut l'ajouter au niveau des packages/modules de notre environnement virtuel.
  - Ainsi, on doit créer un fichier `__init__.py` dans le dossier du module.
  - Puis, à l'aide du fichier `setup.py`, on ajoute le module à l'environnement virtuel avec la commande : `pip install -e .` (à réaliser dans le dossier principal du projet. Ici, dans le dossier `compilation`)
