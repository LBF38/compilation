# -*- encoding: utf-8 -*-

import os
import pytest

from compiler.lexer import Lexer

# Add your lexer tests here!

@pytest.mark.parametrize("string,expected", [(["// Bonjour _%^%&@*134qfsv"], "COMMENT")])
def test_lex_one_lexem(string, expected):
    lexer = Lexer()
    lexems = lexer.lex(string)
    assert len(lexems) == 1
    assert lexems[0].tag == expected

@pytest.mark.parametrize("test_program", ["example1.c", "example2.c", "example3.c", "example4.c", "example5.c"])
def test_lex_complete(test_program):
    lexer = Lexer()
    lexer.lex_file(os.path.join(os.getcwd(), "examples/" + test_program))
