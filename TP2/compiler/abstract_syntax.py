"""Abstract syntax for the compiler.
This file defines the classes for the abstract syntax tree.
"""

from typing import List


class AST:
    def __init__(self) -> None:
        self.tree
    
class Program:
    def __init__(self, declarations, statements) -> None:
        self.declarations: List[Declaration] = declarations
        self.statements: List[Statement] = statements


class Declaration:
    def __init__(self, type_: int | str | bool | float, identifier, integer) -> None:
        self.type = type_
        self.identifier: Identifier = identifier
        self.integer: int = integer


class Assignement:
    def __init__(self, identifier, table_expression, expression) -> None:
        self.identifier: Identifier = identifier
        self.table_expression: Expression = table_expression
        self.expression: Expression = expression


class Expression:
    def __init__(self, left, operator, right) -> None:
        self.left = left
        self.operator = operator
        self.right = right


class Statement:
    def __init__(self, statement_type) -> None:
        self.statement_type: Assignement | If | While = statement_type


class Body:
    def __init__(self, statements) -> None:
        self.statements: List[Statement] = statements


class Else:
    def __init__(self,body) -> None:
        self.body:Body=body


class If(Statement):
    def __init__(self, condition, body, else_) -> None:
        self.condition: Expression = condition
        self.body: Body = body
        self.else_: Else = else_


class While(Statement):
    def __init__(self, condition, body) -> None:
        self.condition: Expression = condition
        self.body: Body = body

class Conjunction:
    def __init__(self,equalities) -> None:
        self.equalities: List[Equality] = equalities

class Equality:
    def __init__(self,first_relation,equoperator, second_relation) -> None:
        self.first_relation: Relation = first_relation
        self.second_relation: Relation = second_relation
        self.equoperator = equoperator

class Relation:
    def __init__(self,first_addition,reloperator, second_addition) -> None:
        self.first_addition: Addition = first_addition
        self.reloperator = reloperator
        self.second_addition: Addition = second_addition

class Addition:
    def __init__(self,addop,terms) -> None:
        self.terms: List[Term] = terms
        self.addop = addop

class Term:
    def __init__(self) -> None:
        self.factors: List[Factor] = factors
        
        

class Identifier:
    def __init__(self, name) -> None:
        self.name = name


if __name__ == "__main__":
    print("Testing abstract syntax tree")
    ast = Program(Declaration("int", "a", 1), Statement(Assignement("a", Expression(
        1, "+", 2)), Body(Statement(Assignement("a", Expression(1, "+", 2))))))
    print(ast)
