"""Abstract Syntax Definition
This file defines the abstract syntax of the language.
"""


from typing import List


class AstNode:
    def accept(self, visitor, args=None):
        name = self.__class__.__name__
        return getattr(visitor, 'visit' + name)(self, args)


class Circuit(AstNode):
    def __init__(self, identifier, input, output, body) -> None:
        self.identifier: Identifier = identifier
        self.input: Input = input
        self.output: Output = output
        self.body: Body = body


class Input(AstNode):
    def __init__(self, parameters) -> None:
        self.parameters: List[Parameter] = parameters


class Output(AstNode):
    def __init__(self, parameters) -> None:
        self.parameters = parameters


class Identifier(AstNode):
    def __init__(self, name: str) -> None:
        self.name: str = name


class Body(AstNode):
    def __init__(self, expressions) -> None:
        self.expressions = expressions


class Operator(AstNode):
    def __init__(self, name) -> None:
        self.name: str = name


class Expression(AstNode):
    def __init__(self, left, operator: Operator, right) -> None:
        self.left = left
        self.operator = operator
        self.right = right


class Parameter(AstNode):
    def __init__(self, identifier: Identifier) -> None:
        self.identifier = identifier


if __name__ == '__main__':
    from visitor_tp5 import SimpleVisitor

    print(f"test of {__name__}")
    ast = Circuit(Identifier("half_adder"), Input([Identifier("a"), Identifier("b")]), Output([Identifier(
        "sum"), Identifier("carry")]), Body([Expression(Identifier("sum"), Operator("="), Expression(Identifier("a"), Operator("XOR"), Identifier("b"))), Expression(Identifier("carry"), Operator("="), Expression(Identifier("a"), Operator("AND"), Identifier("b")))]))
    visitor = SimpleVisitor()
    print(visitor.visit(ast))
