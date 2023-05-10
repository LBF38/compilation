# Projet de compilation - Code Graph Compiler

Le projet de compilation a pour objectif de visualiser les liens dans le code.
Il s'appuiera sur la syntaxe du langage Dart comme premier exemple d'utilisation.
Il n'est pas nécessaire de vérifier que le code s'exécute correctement mais il faut qu'il respecte à minima la syntaxe Dart pour permettre la visualisation minime des liens entre objets.

<details>
<summary><h2>Attendus du projet compilation</h2></summary>

* [ ] Lexer
* [ ] Parser
* [ ] AST
* [ ] Pretty Printer (w/ Visitor)
* [ ] Documentation

</details>

## Objectifs

* Visualiser les liens entre les objets du type `class` / `interface` / `enum` / `typedef` / `abstract class`
* Visualiser les variables définies dans ces classes et fonctions.
* La visualisation sera représenté dans un langage de représentation de diagramme des classes.

## Idées pour l'implémentation

Pour réaliser une visualisation simple des classes et autres liens entre les objets d'un code, il est important de bien recenser ces types d'objets mais aussi de savoir comment les générer et gérer les liens entre eux.

Ainsi, on va se concentrer dans une première partie avec une version simplifiée à partir du langage Dart. Puis, cela pourra être étendu à d'autres langages ou amélioré en fonction des besoins/temps à disposition.

Concernant la génération de code, il est possible d'utiliser différents langages de représentation de diagramme de classe UML. Voici une liste non exhaustive de ces langages:

* [PlantUML](https://plantuml.com)
* [Mermaid](https://mermaid.js.org/) : [Mermaid class diagram syntax](https://mermaid.js.org/syntax/classDiagram.html)

Ceux-ci pourront être étendus à d'autres langages de représentation de diagramme de classe UML, en fonction des besoins/temps à disposition.

Pour ce projet, il sera principalement utilisé le langage Mermaid pour la génération de diagramme de classe. Ce choix est motivé par la simplicité de ce langage et sa bonne intégration dans les fichiers Markdown.

## Description du compilateur

Pour ce projet, l'objectif est de réaliser une version très simplifiée de l'ensemble des parties du compilateur afin de pouvoir commencer la génération de diagramme de classe. Chacune des parties composant le compilateur pourront ainsi être améliorées par la suite.

La version minimale du projet de compilation sera composée de 3 parties:

* [ ] Lexer
* [ ] Parser
* [ ] Visitor (one or more)

Il contient également la définition de l'arbre de syntaxe abstraite (AST) et d'une classe `Compiler` permettant de lancer et gérer la compilation.

## Installation

Pour installer le projet, veuillez télécharger ce dépôt et installer les dépendances avec la commande suivante:

```bash
python -m pip install -r requirements.txt
```

## Utilisation

Pour utiliser le projet et générer un diagramme de classe, il faut lancer le script `main.py` avec le fichier à compiler en paramètre:

```bash
python main.py <file>
```

L'option `--output` permet de spécifier le fichier de sortie du diagramme de classe:

```bash
python main.py <file> --output <output_file>
```

> **Note**
> Par défaut, le fichier de sortie est le nom du fichier d'entrée avec l'extension `.md`.

---

## Laboratoire

Dans cette partie, je vais présenter rapidement les différents tests et explorations que j'ai réalisé au cours de ma découverte des compilateurs, du cours et de son implémentation.

### Ruby

Après une première expérience de compilateur en python, au travers des différents TDs, j'ai voulu réimplémenter cela en Ruby qui est un langage bien plus adapté à la programmation objet.

Toutefois, faute de temps et n'ayant pas pu suffisamment apprendre sur Ruby, je n'ai pas pu aller plus loin dans la découverte des outils possibles pour réaliser le projet de compilation en Ruby.

### TypeScript

Ayant une petite expérience dans le développement web et connaissant mieux TypeScript que Ruby, j'ai également considéré l'option de réaliser le projet de compilation en TypeScript.
Toutefois, à nouveau, cela n'a pas été concluant.

### Python

Ainsi, j'ai décidé de reprendre les solutions réalisées en TDs afin de capitaliser sur celles-ci pour le projet.

### ANTLR/ANTLR4

Plus je réfléchissais au projet compilation, plus je me suis dit que mon projet constituait principalement la réalisation d'un visiteur qui génère le diagramme de classes à partir d'un AST. Ainsi, je pourrais utiliser la définition d'un langage déjà créé, comme le langage Dart, et me concentrer sur la génération du diagramme de classes en n'implémentant que la partie visiteur.

Ainsi, j'ai entamé des recherches sur le langage ANTLR et ANTLR4 qui permettent de définir un langage et de générer un visiteur pour celui-ci. De plus, il suffit de récupérer la définition du langage Dart au format ANTLR (`.g`/`.g4`) et de générer les fichiers adéquats pour le compilateur. La partie la plus fastidieuse serait alors de redéfinir toutes les fonctions du visiteur pour correspondre à ce que je souhaite faire.

Vous trouverez [ici](https://github.com/dart-lang/sdk/blob/master/tools/spec_parser/Dart.g) le fichier de définition du langage Dart au format ANTLR.

> **Warning**
> Ce fichier est au format ANTLR3 et non ANTLR4 (`.g4`). Ainsi, il est nécessaire d'utiliser la version 3.* d'ANTLR pour générer les fichiers adéquats (Lexer, Parser, Visitor, ...).

## Conclusion

Même si ce projet compilation n'est pas à la hauteur de mes attentes, il m'a permis de mieux comprendre les différentes parties d'un compilateur et de me rendre compte de la complexité de celui-ci. Ainsi, il est simple de réaliser un compilateur pour un projet ou un besoin particulier, mais cela peut vite devenir fastidieux ou compliqué lorsque l'on souhaite réaliser des opérations complexes ou de multiples possibilités.

## Auteurs

* [@LBF38](https://github.com/LBF38)
