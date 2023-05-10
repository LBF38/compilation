# TP5

Elaboration d'un visiteur plus complexe : le Checker.

L'objectif de ce visiteur est de vérifier que toutes les variables utilisées dans leur contexte sont bien déclarées.
Ainsi, une variable doit soit être déclaré dans le contexte global du programme, soit dans l'un des contextes locaux englobant son utilisation.
Pour mettre en place cela, on peut créer par exemple un dictionnaire contenant l'ensemble des variables déclarées dans le contexte courant.
Chaque dictionnaire représente donc le contexte d'un bloc de code.
S'il on veut vérifier la définition d'une variable ou son utilisation, il nous suffit de vérifier que la variable fait partie de l'un des dictionnaires accessibles à partir du contexte d'utilisation.

## Question 7 - Définitions des règles du langage étudié

Ces règles permettent de définir la syntaxe du langage et de rejeter ce que l'on ne souhaite pas.

- **`circuit`** *identifier*
  - **`input`** *identifier* (`,` *identifier*)$*$
  - **`output`** *identifier* (`,` *identifier*)$*$
  - *body*
- **`end`**
- *body* := *out_statement* (`\n` *out_statement*)$*$
- *out_statement* := *output* *operator* *in_statement*
- *in_statement* := *input* (*operator* *input*)?
- *operator* := `+` | `-` | `*` | `/` | `^`
