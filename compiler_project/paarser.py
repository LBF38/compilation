# -*- encoding: utf-8 -*-


import logging

from compiler_project.abstract_syntax import (
    AstNode,
    Class,
    Field,
    Method,
    Parameter,
    TypeNode,
)
from compiler_project.lexer import Lexem
from compiler_project.rules import (
    Cleaning_ruleset,
    Identifier_ruleset,
    Keyword_ruleset,
    Operator_ruleset,
    Ponctuation_ruleset,
    Type_ruleset,
)

logger = logging.getLogger(__name__)


class ParsingException(Exception):
    pass


class Parser:
    def __init__(self, lexems: list[Lexem]):
        """
        Component in charge of syntaxic analysis.
        """
        self.lexems: list[Lexem] = lexems
        self.ast_root = AstNode()
        self.types: list[str] = [
            Type_ruleset().__getattribute__(attr)
            for attr in dir(Type_ruleset())
            if not attr.startswith("__")
        ]

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

    def expect(self, tag: str):
        """
        Pops the next token from the lexems list and tests its type through the tag.
        """
        next_lexem = self.show_next()
        if next_lexem.tag != tag:
            raise ParsingException(
                f"ERROR at {str(self.show_next().position)}: "
                + f"Expected {tag}, got {next_lexem.tag} instead"
            )
        return self.accept()

    def remove_comments(self):
        """
        Removes the comments from the token list by testing their tags.
        """
        self.lexems = [
            lexem for lexem in self.lexems if lexem.tag != Cleaning_ruleset.COMMENT
        ]

    # ==========================
    #     Parsing Functions
    # ==========================

    def parse(self):
        """
        Main function: launches the parsing operation given a lexem list.
        """
        try:
            self.remove_comments()
            code_graph = self.parse_code()
        except ParsingException as err:
            logger.exception(err)
            raise err
        return code_graph

    def parse_code(self):
        """
        Parses the code for visualizing the links between objects.
        """
        if self.show_next().tag == Keyword_ruleset.CLASS:
            return self.parse_class()
        # elif(self.show_next().tag == "INTERFACE"):
        #     return self.parse_interface()
        else:
            raise ParsingException("ERROR: Expected class or interface")

    def parse_class(self):
        """
        Parses a class.
        """
        # TODO: separate the different steps of the parsing process
        # (class, constructor, fields, methods, etc.)
        self.expect(Keyword_ruleset.CLASS)
        class_name = self.expect(Identifier_ruleset.IDENTIFIER)
        self.expect(Ponctuation_ruleset.L_CURL_BRACKET)
        methods: list[Method] = []
        fields: list[Field] = []
        # TODO: refactor with guard clauses and errors.
        while self.show_next().tag != Ponctuation_ruleset.R_CURL_BRACKET:
            if self.show_next().tag in self.types:
                if self.show_next(2).tag == Identifier_ruleset.IDENTIFIER:
                    if self.show_next(3).tag == Ponctuation_ruleset.L_PAREN:
                        methods.append(self.parse_method())
                    else:
                        fields.append(self.parse_field())
            if self.show_next().tag == Identifier_ruleset.IDENTIFIER:
                identifier = self.expect(Identifier_ruleset.IDENTIFIER)
                if identifier.value != class_name.value:
                    raise ParsingException("ERROR: Expected class name")
                self.expect(Ponctuation_ruleset.L_PAREN)
                constructor_params = []
                if self.show_next().tag == Keyword_ruleset.THIS:
                    self.expect(Keyword_ruleset.THIS)
                    self.expect(Operator_ruleset.DOT)
                    constructor_params.append(
                        self.expect(Identifier_ruleset.IDENTIFIER)
                    )
                while self.show_next().tag == Ponctuation_ruleset.COMMA:
                    self.expect(Ponctuation_ruleset.COMMA)
                    self.expect(Keyword_ruleset.THIS)
                    self.expect(Operator_ruleset.DOT)
                    constructor_params.append(
                        self.expect(Identifier_ruleset.IDENTIFIER)
                    )
                self.expect(Ponctuation_ruleset.R_PAREN)
                self.expect(Ponctuation_ruleset.SEMICOLON)
        self.expect(Ponctuation_ruleset.R_CURL_BRACKET)
        return Class(class_name.value, fields, methods)

    def parse_method(self) -> Method:
        method_type = self.parse_type()
        method_name = self.expect(Identifier_ruleset.IDENTIFIER)
        self.expect(Ponctuation_ruleset.L_PAREN)
        # parse parameters
        parameters = self.parse_parameters()
        self.expect(Ponctuation_ruleset.R_PAREN)
        self.expect(Ponctuation_ruleset.L_CURL_BRACKET)
        # parse method body
        method_body = self.parse_method_body()
        self.expect(Ponctuation_ruleset.R_CURL_BRACKET)
        return Method(method_name, method_type, parameters, method_body)

    def parse_field(self) -> Field:
        field_type = self.parse_type()
        field_name = self.expect(Identifier_ruleset.IDENTIFIER)
        self.expect(Ponctuation_ruleset.SEMICOLON)
        return Field(field_name, field_type)

    def parse_type(self):
        for type in self.types:
            if self.show_next().tag == type:
                return TypeNode(self.expect(type).value)

    def parse_parameters(self) -> list[Parameter]:
        if self.show_next().tag == Ponctuation_ruleset.R_PAREN:
            return []
        params: list[Parameter] = []
        params_type = self.parse_type()
        params_identifier = self.expect(Identifier_ruleset.IDENTIFIER)
        params.append(Parameter(params_identifier, params_type))
        while self.show_next().tag == Ponctuation_ruleset.COMMA:
            self.expect(Ponctuation_ruleset.COMMA)
            params_type = self.parse_type()
            params_identifier = self.expect(Identifier_ruleset.IDENTIFIER)
            params.append(Parameter(params_identifier, params_type))
        return params

    def parse_method_body(self):
        # TODO: implement method body parsing for general cases
        # Here, it is only to work with the `class.dart` example file.
        self.expect(Keyword_ruleset.RETURN)
        identifier = self.expect(Identifier_ruleset.IDENTIFIER)
        self.expect(Ponctuation_ruleset.SEMICOLON)
        return identifier.value
