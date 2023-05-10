import os
from compiler_project.abstract_syntax import AstNode
from compiler_project.lexer import Lexer
from compiler_project.paarser import Parser
from compiler_project.visitor import CodeGraph, PrettyPrinter


class Compiler:
    def __init__(self):
        self.ast = AstNode()
        self.output_filename = "code_graph_output"
        self.output_token = False
        self.output_pretty = False

    def compile(self, filename) -> AstNode:
        """Compile the given file.

        Args:
            filename (str): name of the file to compile

        Returns:
            ASTNode: Abstract Syntax Tree of the code in the file
        """
        lexer = Lexer()
        lexer.lex_file(filename)
        parser = Parser(lexer.lexems)
        self.ast = parser.parse()
        self.code_graph_generated = self.ast.accept(CodeGraph())
        with open(self.output_filename + ".md", "w") as f:
            f.write(self.code_graph_generated)
        if self.output_pretty:
            pretty_code = self.ast.accept(PrettyPrinter())
            with open(self.output_filename + "_pretty.dart", "w") as f:
                f.write(pretty_code)
        if self.output_token:
            print("Tokens: \n")
            print(lexer.lexems)
        return self.ast


if __name__ == "__main__":
    compiler = Compiler()
    compiler.compile(os.path.join(os.path.dirname(__file__), "fixtures/class.dart"))
    print(compiler.ast.accept(PrettyPrinter()))
    print(compiler.ast.accept(CodeGraph()))
