# -*- encoding: utf-8 -*-

import sys


class Parser:
    def __init__(self, lexems):
        """
        Component in charge of syntaxic analysis.
        """
        self.lexems = lexems

    # ==========================
    #      Helper Functions
    # ==========================

    def error(self, message):
        """
        Error template.
        """
        print(f"ERROR at {str(self.peek().position)}: {message}")
        sys.exit(1)

    def accept(self):
        """
        Pops the lexem out of the lexems list and log its tag/value combination.
        """
        self.peek()
        return self.lexems.pop(0)

    def show_next(self, n=1):
        """
        Returns the next token in the list WITHOUT popping it.
        """
        try:
            return self.lexems[n - 1]
        except IndexError:
            self.error("No more lexems left.")

    def expect(self, tag):
        """
        Pops the next token from the lexems list and tests its type through the tag.
        """
        next_lexem = self.peek()
        if next_lexem.tag == tag:
            return self.consume()
        else:
            self.error(f"Expected {tag}, got {next_lexem.tag} instead")

    def remove_comments(self):
        """
        Removes the comments from the token list by testing their tags.
        """
        self.lexems = [lexem for lexem in self.lexems if lexem.tag != "COMMENT"]

    # ==========================
    #     Parsing Functions
    # ==========================

    def parse(self):
        """
        Main function: launches the parsing operation given a lexem list.
        """
        self.remove_comments()
        self.parse_program()

    def parse_program(self):
        """
        Parses a program which is a succession of assignments.
        """
        self.expect("TYPE_INT")
        self.expect("KW_MAIN")
        self.expect("L_PAREN")
        self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")
        # Your code here!
        self.expect("R_CURL_BRACKET")

    def parse_assignment(self):
        ...

    def parse_declaration(self):
        ...

    ...
