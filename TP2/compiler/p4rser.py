# -*- encoding: utf-8 -*-


import logging

logger = logging.getLogger(__name__)


class ParsingException(Exception):
    pass


class Parser:
    def __init__(self, lexems):
        """
        Component in charge of syntaxic analysis.
        """
        self.lexems = lexems

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
            self.parse_program()
        except ParsingException as err:
            logger.exception(err)
            raise

    def parse_program(self):
        """
        Parses a program which is a succession of assignments.
        """
        self.expect("TYPE_INT")
        self.expect("KW_MAIN")
        self.expect("L_PAREN")
        self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")
        while(self.show_next().tag in ["TYPE_INT", "TYPE_FLOAT", "TYPE_CHAR", "TYPE_BOOL"]):
            self.parse_declaration()
        while(self.show_next().tag in ["IDENTIFIER", "KW_IF", "KW_WHILE"]):
            self.parse_statement()
        self.expect("R_CURL_BRACKET")

    def parse_declaration(self):
        self.parse_type()
        self.expect("IDENTIFIER")
        if(self.show_next().tag == "L_BRACKET"):
            self.expect("L_BRACKET")
            self.expect("LIT_INT")
            self.expect("R_BRACKET")
        self.expect("SEMICOLON")

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
            self.parse_assignment()
        elif(self.show_next().tag == "KW_IF"):
            self.parse_if_statement()
        elif(self.show_next().tag == "KW_WHILE"):
            self.parse_while_statement()

    def parse_assignment(self):
        self.expect("IDENTIFIER")
        if (self.show_next().tag == "L_BRACKET"):
            self.expect("L_BRACKET")
            self.parse_expression()
            self.expect("R_BRACKET")
        self.expect("OP_ASSIGN")
        self.parse_expression()
        self.expect("SEMICOLON")

    def parse_if_statement(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_else_statement(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_while_statement(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_expression(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_conjunction(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_equop(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_equality(self):
        if(self.show_next().tag != "IDENTIFIER"):
            raise ParsingException(
                "Expected IDENTIFIER, got {next_lexem.tag} instead")
        self.parse_relation()

    def parse_relation(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_relop(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_addition(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_addop(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_term(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_mulop(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_factor(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_unaryop(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_primary(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_parenth(self):
        # TODO: Implement
        raise Exception("This is unimplemented")

    def parse_identifier(self):
        self.expect("IDENTIFIER")

    def parse_literal(self):
        # TODO: Implement
        raise Exception("This is unimplemented")
