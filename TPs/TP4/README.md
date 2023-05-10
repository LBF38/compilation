# TP4 - Implémentation du pattern Visiteur

Création d'un visiteur simple à partir d'un AST construit à la main.

Cet exemple permet de mieux comprendre le fonctionnement du pattern visiteur et de son implémentation.
Ainsi, on constate qu'il est nécessaire de définir toutes les méthodes de toutes les classes de l'arbre de syntaxe abstraite afin de visiter tous les éléments de l'AST.

De plus, pour améliorer cela, on peut créer une classe abstraite contenant la définition de toutes les méthodes nécessaires pour visiter l'AST.
Ainsi, on pourra hériter de cette classe abstraite pour créer un visiteur qui ne contient que les méthodes qui nous intéressent.

Cet exemple très simple de visiteur permet de comprendre son fonctionnement et le va-et-vient entre les classes de l'AST et les méthodes du visiteur.
