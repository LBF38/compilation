# -*- encoding: utf-8 -*-

import os
import pytest

from compiler.lexer import Lexer
from compiler.p4rser import Parser
@pytest.mark.parametrize("test_program", ["example1.c", "example2.c", "example3.c", "example4.c", "example5.c"])

# Add your parser tests here!


def test_parse_complete(test_program):
    lexer = Lexer()
    lexems = lexer.lex_file(os.path.join(os.getcwd(),"examples/" + test_program))
    print(lexems)
    parser = Parser(lexems)
    parser.parse()
