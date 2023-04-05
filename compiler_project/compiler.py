import os
from compiler_project.lexer import Lexer
from compiler_project.paarser import Parser


class Compiler:
    def compile(self, filename):
        """Compile the given file.

        Args:
            filename (str): name of the file to compile

        Returns:
            ASTNode: Abstract Syntax Tree of the code in the file
        """
        lexer = Lexer()
        lexer.lex_file(filename)
        parser = Parser(lexer.lexems)
        ast = parser.parse()
        return ast


if __name__ == "__main__":
    compiler = Compiler()
    ast = compiler.compile(os.path.join(
        os.path.dirname(__file__), "fixtures/class.dart"))
    print(ast)
