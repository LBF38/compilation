
import re
import sys
import os

regexExpressions = [
    # Whitespace
    (r'[ \n]+', None),

    # Keywords
    (r'import', 'KW_IMPORT'),
    (r'from', 'KW_FROM'),
    (r'as', 'KW_AS'),
    (r'class', 'KW_CLASS'),
    (r'self', 'KW_SELF'),
    (r'__init__', 'KW_INIT'),
    (r'__name__', 'KW_NAME'),
    (r'__main__', 'KW_MAIN'),
    (r'__str__', 'KW_STR'),
    (r'def', 'KW_DEF'),
    (r'if', 'KW_IF'),
    (r'elif', 'KW_ELIF'),
    (r'else', 'KW_ELSE'),
    (r'for', 'KW_FOR'),
    (r'in', 'KW_IN'),
    (r'while', 'KW_WHILE'),
    (r'break', 'KW_BREAK'),
    (r'continue', 'KW_CONTINUE'),
    (r'return', 'KW_RETURN'),
    (r'pass', 'KW_PASS'),
    (r'and', 'KW_AND'),
    (r'or', 'KW_OR'),
    (r'not', 'KW_NOT'),
    (r'is', 'KW_IS'),
    (r'None', 'KW_NONE'),
    (r'True', 'KW_TRUE'),
    (r'False', 'KW_FALSE'),
    (r'print', 'KW_PRINT'),
    (r'\t', 'KW_TAB'),
    

    # Operators
    (r'\+', 'PLUS'),
    (r'\-', 'MINUS'),
    (r'\*', 'MULT'),
    (r'\/', 'DIV'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\.', 'DOT'),
    (r'\,', 'COMMA'),
    (r'\:', 'COLON'),
    (r'\;', 'SEMICOLON'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r'\[', 'LBRACKET'),
    (r'\]', 'RBRACKET'),
    (r'\<', 'LT'),
    (r'\>', 'GT'),
    (r'\<\=', 'LTE'),
    (r'\>\=', 'GTE'),
    (r'\=\=', 'EQ'),
    (r'\=', 'ASSIGN'),
    (r'\!\=', 'NEQ'),
    (r'\!', 'NOT'),
    (r'\&\&', 'AND'),
    (r'\|\|', 'OR'),
    # (r'\"', 'QUOTE'),
    
    # Literals
    (r'\".*\"', 'STRING'),
    (r'\d+\.\d+', 'FLOAT'),
    (r'\d+', 'INTEGER'),

    # Identifiers
    (r'[a-zA-Z][a-zA-Z0-9_]+', 'IDENTIFIER'),
]


class Lexem:
    '''
    Our token definition:
    lexem (tag and value) + position in the program raw text
    Parameters
    ----------
    tag: string
        Name of the lexem's type, e.g. IDENTIFIER
    value: string
        Value of the lexem,       e.g. integer1
    position: integer tuple
        Tuple to point out the lexem in the input file (line number, position)
    '''

    def __init__(self, tag=None, value=None, position=None):
        self.tag = tag
        self.value = value
        self.position = position

    def __repr__(self):
        return self.tag


class Lexer:
    '''
    Component in charge of the transformation of raw data to lexems.
    '''

    def __init__(self, lexems=None):
        self.lexems = lexems if lexems is not None else []

    def lex(self, inputText):
        '''
        Main lexer function:
        Creates a lexem for every detected regular expression
        The lexems are composed of:
            - tag
            - values
            - position
        SEE lexem for more info
        '''
        # Crawl through the input file
        for lineNumber, line in enumerate(inputText):
            lineNumber += 1
            position = 0
            # Crawl through the line
            while position < len(line):
                match = None
                for lexemRegex in regexExpressions:
                    pattern, tag = lexemRegex
                    regex = re.compile(pattern)
                    match = regex.match(line, position)
                    if match:
                        data = match.group(0)
                        # This condition is needed to avoid the creation of whitespace lexems
                        if tag:
                            lexem = Lexem(tag, data, [lineNumber, position])
                            self.lexems.append(lexem)
                        # Renew the position
                        position = match.end(0)
                        break
                # No match detected --> Wrong syntax in the input file
                if not match:
                    print("No match detected on line and position:")
                    print(line[position:])
                    sys.exit(1)

        return self.lexems


if __name__ == "__main__":
    # Test the lexer
    lexer = Lexer()
    filenames = ["pythoncode.py"]
    for filename in filenames:
        filename = os.path.join(os.path.dirname(__file__), filename)
        with open(filename, "r") as f:
            inputText = f.readlines()
            lexer.lex(inputText)
            print("Lexems for file", filename)
            print(lexer.lexems)
