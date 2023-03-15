import os

from compiler.abstract_syntax import (
    Body, Declaration, Else, Expression, Program)
from compiler.lexer import Lexer
from compiler.p4rser import Parser


class VisitorMiniC:

    def visit(self, ast, args=None):
        ast.accept(self, args)

    def visitProgram(self, program: Program, args):
        for declaration in program.declarations:
            self.visit(declaration)
        for statement in program.statements:
            self.visit(statement)

    def visitDeclaration(self, declaration: Declaration, args):
        print(
            f"Declaration: {declaration.type} {declaration.identifier} {declaration.integer};")

    def visitAssignement(self, identifier, table_expression, expression):
        print(f"{identifier} {table_expression} = {expression};")

    def visitIf(self, condition: Expression, body: Body, else_: Else):
        self.visit(condition)
        self.visit(body)
        self.visit(else_)

    # TODO: implement the rest of the visit methods to make a simple visitor


if __name__ == '__main__':
    lexer = Lexer()
    lexems = lexer.lex_file(os.path.join(
        os.getcwd(), "examples/example1.c"))
    parser = Parser(lexems)
    program = parser.parse()
    visitor = VisitorMiniC()
    program.accept(visitor)
    print("test")
