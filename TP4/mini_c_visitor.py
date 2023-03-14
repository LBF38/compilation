import os
from TP2.compiler.abstract_syntax import *
from TP2.compiler.p4rser import *
from TP2.compiler.lexer import *


class VisitorMiniC:

    def visit(self, ast, args=None):
        ast.accept(self, args)

    def visitProgram(self, program: Program, args):
        for declaration in program.declarations:
            self.visit(declaration)
        for statement in program.statements:
            self.visit(statement)

    def visitDeclaration(self, declaration: Declaration, args):
        self.visit(declaration.type)
        self.visit(declaration.identifier)
        # ...

    # TODO: implement the rest of the visit methods to make a simple visitor


if __name__ == '__main__':
    lexer = Lexer()
    lexems = lexer.lex_file(os.path.join(
        os.getcwd(), "TP2/examples/example1.c"))
    parser = Parser(lexems)
    program = parser.parse()
    visitor = VisitorMiniC()
    program.accept(visitor)
