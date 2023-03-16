# TP5

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
