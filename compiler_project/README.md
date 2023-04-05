# Notes sur le projet de compilation

Le projet de compilation a pour objectif de visualiser les liens dans le code.
Il s'appuiera sur la syntaxe du langage Dart, principalement.
Il n'est pas nécessaire de vérifier que le code s'exécute correctement mais il faut qu'il respecte à minima la syntaxe Dart pour permettre la visualisation minime des liens entre objets.

## Objectifs

* Visualiser les liens entre les objets du type class / interface / enum / typedef / abstract class
* Visualiser les variables définies dans ces classes et fonctions.
* La visualisation sera représenté dans un langage de représentation de diagramme des classes.

## Idées pour l'implémentation

Pour réaliser une visualisation simple des classes et autres liens entre les objets d'un code, il est important de bien recenser ces types d'objets mais aussi de savoir comment les générer et gérer les liens entre eux.

Ainsi, on va se concentrer dans une première partie avec une version simplifiée à partir du langage Dart. Puis, cela pourra être étendu à d'autres langages ou amélioré en fonction des besoins/temps à disposition.

Concernant la génération de code, il est possible d'utiliser différents langages de représentation de diagramme de classe UML. Voici une liste non exhaustive de ces langages:

* PlantUML
* Mermaid

Ceux-ci pourront être étendus à d'autres langages de représentation de diagramme de classe UML, en fonction des besoins/temps à disposition.
