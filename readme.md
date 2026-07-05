## Intro
  This project is a simple implemantation of a tac (Three Adress Code)
    
## Requirements
  - Binary arithmetic expressions: x + y, x – y, x / y, x * y, x ^ y, etc.
  - Arithmetic expressions with balanced parentheses: (x + y), x * (y+z), (x / (y-z)), etc.
  - Relational expressions: (x > y), x <= (y+z), (x <> (y-z)), etc.
  - Variable declaration: var int x, y | real s | etc.
  - Declaration of vectors and matrices: int x[10]; | real m[10][20]; | etc.
  - Assignment of vectors and matrices: a = v[i]; | v[i] = v[j]; | v[i] = a; | a = m[i][j]; | m[i][j] = p[i][j]; | etc. 
  - Repetition Command: while ( a > b ) { comandos }.
  - Control flow command: if ( a > b ) { comandos } else {comandos}.
  - Display a context-appropriate error message when the input sentence does not conform to the grammar.

## Require package
  - $: pip install ply

## Dev package
  - $: pip install pytest

## Run
  - Add some code into codigo.txt
  - $: python main.py

## Run test
  - $: pytest
