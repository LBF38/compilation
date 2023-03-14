# -*- encoding: utf-8 -*-


import logging

from compiler.abstract_syntax import (AstNode,Program,Declaration,Assignement,Body,Identifier,If,Else,While,Conjunction)

logger = logging.getLogger(__name__)


class ParsingException(Exception):
    pass


class Parser:
    def __init__(self, lexems):
        """
        Component in charge of syntaxic analysis.
        """
        self.lexems = lexems
        self.ast_root = AstNode()

    # ==========================
    #      Helper Functions
    # ==========================

    def accept(self):
        """
        Pops the lexem out of the lexems list and log its tag/value combination.
        """
        self.show_next()
        return self.lexems.pop(0)

    def show_next(self, n=1):
        """
        Returns the next token in the list WITHOUT popping it.
        """
        try:
            return self.lexems[n - 1]
        except IndexError:
            raise ParsingException("No more lexems left.")

    def expect(self, tag):
        """
        Pops the next token from the lexems list and tests its type through the tag.
        """
        next_lexem = self.show_next()
        if next_lexem.tag != tag:
            raise ParsingException(
                f"ERROR at {str(self.show_next().position)}: Expected {tag}, got {next_lexem.tag} instead"
            )
        return self.accept()

    def remove_comments(self):
        """
        Removes the comments from the token list by testing their tags.
        """
        self.lexems = [
            lexem for lexem in self.lexems if lexem.tag != "COMMENT"]

    # ==========================
    #     Parsing Functions
    # ==========================

    def parse(self):
        """
        Main function: launches the parsing operation given a lexem list.
        """
        try:
            self.remove_comments()
            program = self.parse_program()
        except ParsingException as err:
            logger.exception(err)
            raise
        return program

    def parse_program(self):
        """
        Parses a program which is a succession of assignments.
        """
        declarations_list = []
        statements_list = []
        self.expect("TYPE_INT")
        self.expect("KW_MAIN")
        self.expect("L_PAREN")
        self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")
        while(self.show_next().tag in ["TYPE_INT", "TYPE_FLOAT", "TYPE_CHAR", "TYPE_BOOL"]):
            declaration = self.parse_declaration()
            declarations_list.append(declaration)
        while(self.show_next().tag in ["IDENTIFIER", "KW_IF", "KW_WHILE"]):
            statement = self.parse_statement()
            statements_list.append(statement)
        self.expect("R_CURL_BRACKET")
        return Program(declarations_list, statements_list)

    def parse_declaration(self):
        type = self.parse_type()
        identifier = Identifier(self.expect("IDENTIFIER"))
        integer = None
        if(self.show_next().tag == "L_BRACKET"):
            self.expect("L_BRACKET")
            integer = self.expect("LIT_INT")
            self.expect("R_BRACKET")
        self.expect("SEMICOLON")
        return Declaration(type, identifier, integer)

    def parse_type(self):
        types = ["TYPE_BOOL", "TYPE_INT", "TYPE_FLOAT", "TYPE_CHAR"]
        for type in types:
            try:
                return self.expect(type)
            except ParsingException:
                pass
        raise ParsingException(
            f"ERROR at {self.show_next().position}: Expected {types}, got {self.show_next().tag} instead")

    def parse_statement(self):
        if(self.show_next().tag == "IDENTIFIER"):
            return self.parse_assignment()
        elif(self.show_next().tag == "KW_IF"):
            return self.parse_if_statement()
        elif(self.show_next().tag == "KW_WHILE"):
            return self.parse_while_statement()
        raise ParsingException(
            f"ERROR at {self.show_next().position}: Expected a statement, got {self.show_next().tag} instead")

    def parse_assignment(self):
        identifier = self.expect("IDENTIFIER")
        table_expression = None
        if (self.show_next().tag == "L_BRACKET"):
            self.expect("L_BRACKET")
            table_expression = self.parse_expression()
            self.expect("R_BRACKET")
        self.expect("OP_ASSIGN")
        expression = self.parse_expression()
        self.expect("SEMICOLON")
        return Assignement(identifier, table_expression, expression)

    def parse_if_statement(self):
        self.expect("KW_IF")
        self.expect("L_PAREN")
        condition = self.parse_expression()
        self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")
        body = Body([])
        while (self.show_next().tag in ["IDENTIFIER", "KW_IF", "KW_WHILE"]):
            statement = self.parse_statement()
            body.statements.append(statement)
        self.expect("R_CURL_BRACKET")
        else_= None
        if (self.show_next().tag == "KW_ELSE"):
            else_ = self.parse_else_statement()
        return If(condition, body, else_)

    def parse_else_statement(self):
        self.expect("KW_ELSE")
        self.expect("L_CURL_BRACKET")
        body = Body([])
        while (self.show_next().tag in ["IDENTIFIER", "KW_IF", "KW_WHILE"]):
            statement = self.parse_statement()
            body.statements.append(statement)
        self.expect("R_CURL_BRACKET")
        return Else(body)

    def parse_while_statement(self):
        self.expect("KW_WHILE")
        self.expect("L_PAREN")
        condition = self.parse_expression()
        self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")
        body = Body([])
        while (self.show_next().tag in ["IDENTIFIER", "KW_IF", "KW_WHILE"]):
            statement = self.parse_statement()
            body.statements.append(statement)
        self.expect("R_CURL_BRACKET")
        return While(condition, body)

    def parse_expression(self):
        self.parse_conjunction()
        while(self.show_next().tag == "OP_OR"):
            self.parse_conjunction()

    def parse_conjunction(self):
        conjunction = Conjunction(self.parse_equality())
        while(self.show_next().tag == "OP_AND"):
            self.parse_equality()

    def parse_equop(self):
        if(self.show_next().tag == "OP_EQUAL"):
            self.expect("OP_EQUAL")
        elif(self.show_next().tag == "OP_NEQUAL"):
            self.expect("OP_NEQUAL")
        else:
            raise ParsingException(
                f"ERROR at {self.show_next().position}: Expected OP_EQUAL or OP_NOT_EQUAL, got {self.show_next().tag} instead")

    def parse_equality(self):
        self.parse_relation()
        if(self.show_next().tag in ["OP_EQUAL", "OP_NOT_EQUAL"]):
            self.parse_equop()
            self.parse_relation()

    def parse_relation(self):
        self.parse_addition()
        if(self.show_next().tag in ["OP_LESS", "OP_GREATER", "OP_LESS_EQUAL", "OP_GREATER_EQUAL"]):
            self.parse_relop()
            self.parse_addition()

    def parse_relop(self):
        if(self.show_next().tag == "OP_LESS"):
            self.expect("OP_LESS")
        elif(self.show_next().tag == "OP_GREATER"):
            self.expect("OP_GREATER")
        elif(self.show_next().tag == "OP_LESS_EQUAL"):
            self.expect("OP_LESS_EQUAL")
        elif(self.show_next().tag == "OP_GREATER_EQUAL"):
            self.expect("OP_GREATER_EQUAL")
        else:
            raise ParsingException(
                f"ERROR at {self.show_next().position}: Expected OP_LESS, OP_GREATER, OP_LESS_EQUAL or OP_GREATER_EQUAL, got {self.show_next().tag} instead")

    def parse_addition(self):
        self.parse_term()
        while (self.show_next().tag in ["OP_PLUS", "OP_MINUS"]):
            self.parse_addop()
            self.parse_addition()

    def parse_addop(self):
        if(self.show_next().tag == "OP_PLUS"):
            self.expect("OP_PLUS")
        elif(self.show_next().tag == "OP_MINUS"):
            self.expect("OP_MINUS")
        else:
            raise ParsingException(
                f"ERROR at {self.show_next().position}: Expected OP_PLUS or OP_MINUS, got {self.show_next().tag} instead")

    def parse_term(self):
        self.parse_factor()
        while(self.show_next().tag in ["OP_MULT", "OP_DIV", "OP_MOD"]):
            self.parse_mulop()
            self.parse_factor()

    def parse_mulop(self):
        if(self.show_next().tag == "OP_MULT"):
            self.expect("OP_MULT")
        elif(self.show_next().tag == "OP_DIV"):
            self.expect("OP_DIV")
        elif(self.show_next().tag == "OP_MOD"):
            self.expect("OP_MOD")
        else:
            raise ParsingException(
                f"ERROR at {self.show_next().position}: Expected OP_MULT, OP_DIV or OP_MOD, got {self.show_next().tag} instead")

    def parse_factor(self):
        if(self.show_next().tag in ["OP_MINUS", "OP_NOT"]):
            self.parse_unaryop()
        self.parse_primary()

    def parse_unaryop(self):
        if(self.show_next().tag == "OP_MINUS"):
            self.expect("OP_MINUS")
        elif(self.show_next().tag == "OP_NOT"):
            self.expect("OP_NOT")
        else:
            raise ParsingException(
                f"ERROR at {self.show_next().position}: Expected OP_MINUS or OP_NOT, got {self.show_next().tag} instead")

    def parse_primary(self):
        if(self.show_next().tag == "IDENTIFIER"):
            self.expect("IDENTIFIER")
            if(self.show_next().tag == "L_BRACKET"):
                self.expect("L_BRACKET")
                self.parse_expression()
                self.expect("R_BRACKET")
        elif(self.show_next().tag in ["LIT_INT", "LIT_FLOAT", "LIT_CHAR", "LIT_TRUE", "LIT_FALSE"]):
            self.parse_literal()

    def parse_parenth(self):
        self.expect("L_PAREN")
        self.parse_expression()
        self.expect("R_PAREN")

    def parse_literal(self):
        if(self.show_next().tag == "LIT_INT"):
            self.expect("LIT_INT")
        elif(self.show_next().tag == "LIT_FLOAT"):
            self.expect("LIT_FLOAT")
        elif(self.show_next().tag == "LIT_CHAR"):
            self.expect("LIT_CHAR")
        elif(self.show_next().tag == "LIT_TRUE"):
            self.expect("LIT_TRUE")
        elif(self.show_next().tag == "LIT_FALSE"):
            self.expect("LIT_FALSE")
        else:
            raise ParsingException(
                f"ERROR at {self.show_next().position}: Expected LIT_INT, LIT_FLOAT, LIT_CHAR, LIT_TRUE or LIT_FALSE, got {self.show_next().tag} instead")
