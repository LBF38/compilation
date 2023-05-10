# Cours de compilation

Cours de compilation @ ENSTA Bretagne.

## Liens vers les TPs

- [TP1](TPs/TPs/TP1/README.md)
- [TP2](TPs/TP2/)
- [TP3](TPs/TP3/)
- [TP4](TPs/TP4/README.md)
- [TP5](TPs/TP5/README.md)

## Problèmes rencontrés

- `ModuleNotFoundError: No module named '<name>'` :
  - Si cela est un module créé par nos soins, il faut l'ajouter au niveau des packages/modules de notre environnement virtuel.
  - Ainsi, on doit créer un fichier `__init__.py` dans le dossier du module.
  - Puis, à l'aide du fichier `setup.py`, on ajoute le module à l'environnement virtuel avec la commande : `pip install -e .` (à réaliser dans le dossier principal du projet. Ici, dans le dossier `compilation`)
