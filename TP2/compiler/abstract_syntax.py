"""Abstract syntax for the compiler.
This file defines the classes for the abstract syntax tree for the mini-C. (learning purpose)
"""

from abc import ABCMeta
from typing import List


class AstNode:
    def accept(self, visitor, args=None):
        name = self.__class__.__name__
        getattr(visitor, f"visit{name}")(self, args)


class Program(AstNode):
    def __init__(self, declarations, statements) -> None:
        self.declarations: List[Declaration] = declarations
        self.statements: List[Statement] = statements


class Declaration(AstNode):
    def __init__(self, type_: int | str | bool | float, identifier, integer) -> None:
        self.type = type_
        self.identifier: Identifier = identifier
        self.integer: int = integer


class Statement(AstNode):
    pass


class Assignement(Statement):
    def __init__(self, identifier, table_expression, expression) -> None:
        self.identifier: Identifier = identifier
        self.table_expression: Expression = table_expression
        self.expression: Expression = expression


class Expression(AstNode):
    def __init__(self, left, operator, right) -> None:
        self.left = left
        self.operator = operator
        self.right = right


class Body(AstNode):
    def __init__(self, statements) -> None:
        self.statements: List[Statement] = statements


class Else(Statement):
    def __init__(self, body) -> None:
        self.body: Body = body


class If(Statement):
    def __init__(self, condition, body, else_) -> None:
        self.condition: Expression = condition
        self.body: Body = body
        self.else_: Else = else_


class While(Statement):
    def __init__(self, condition, body) -> None:
        self.condition: Expression = condition
        self.body: Body = body


class Conjunction(AstNode):
    def __init__(self, equalities) -> None:
        self.equalities: List[Equality] = equalities


class Equality(AstNode):
    def __init__(self, first_relation, equoperator, second_relation) -> None:
        self.first_relation: Relation = first_relation
        self.second_relation: Relation = second_relation
        self.equoperator = equoperator


class Relation(AstNode):
    def __init__(self, first_addition, reloperator, second_addition) -> None:
        self.first_addition: Addition = first_addition
        self.reloperator = reloperator
        self.second_addition: Addition = second_addition


class Addition(AstNode):
    def __init__(self, addop, terms) -> None:
        self.terms: List[Term] = terms
        self.addop = addop


class Term(AstNode):
    def __init__(self, factors, mulop) -> None:
        self.factors: List[Factor] = factors
        self.mulop = mulop


class Factor(AstNode):
    def __init__(self, unaryop, primary) -> None:
        self.unaryop = unaryop
        self.primary: Primary = primary


class Primary(AstNode):
    pass


class PrimaryExpression(Primary):
    def __init__(self, identifier, expression: Expression | None = None) -> None:
        self.identifier: Identifier = identifier
        self.expression: Expression | None = expression


class PrimaryLiteral(Primary):
    def __init__(self, type, value) -> None:
        self.value = value
        self.type = type


class PrimaryParenth(Primary):
    def __init__(self, parenth) -> None:
        self.parenth: Parenth = parenth


class Parenth(AstNode):
    def __init__(self, expression) -> None:
        self.expression: Expression = expression


class Identifier(AstNode):
    def __init__(self, name) -> None:
        self.name = name


if __name__ == "__main__":
    print("Testing abstract syntax tree")
    # ast = Program(Declaration("int", "a", 1), Assignement("a", None,Expression(
    #     1, "+", 2)), Body(Assignement("a", None,Expression(1, "+", 2))))
    ast2 = Program(Declaration("int", "a", "5"), Body(
        Assignement("a", None, Expression(1, "+", 2))))
    print(ast2)
