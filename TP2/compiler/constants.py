LEXEM_REGEXES = [
    # Comments and whitespaces
    (r"\/\/.*", "COMMENT"),
    (r"[ \t\n]+", None),
    # Special characters
    (r"\(", "L_PAREN"),
    (r"\)", "R_PAREN"),
    (r"\{", "L_CURL_BRACKET"),
    (r"\}", "R_CURL_BRACKET"),
    (r"\[", "L_SQUARE_BRACKET"),
    (r"\]", "R_SQUARE_BRACKET"),
    (r";", "SEMICOLON"),
    # Keywords
    (r"\bmain\b", "KW_MAIN"),
    (r"\bif\b", "KW_IF"),
    (r"\belse\b", "KW_ELSE"),
    (r"\bwhile\b", "KW_WHILE"),
    (r"\bint\b", "TYPE_INT"),
    (r"\bbool\b", "TYPE_BOOL"),
    (r"\bfloat\b", "TYPE_FLOAT"),
    (r"\bchar\b", "TYPE_CHAR"),
    # Operators
    (r"\+", "OP_PLUS"),
    (r"\-", "OP_MINUS"),
    (r"\*", "OP_MULT"),
    (r"\/", "OP_DIV"),
    (r"\%", "OP_MOD"),
    (r'\|\|', 'OP_OR'),
    (r"\&\&", "OP_AND"),
    (r"\=\=", "OP_EQUAL"),
    (r"\!\=", "OP_NOT_EQUAL"),
    (r"\!", "OP_NOT"),
    (r"\>\=", "OP_GREATER_EQUAL"),
    (r"\<\=", "OP_LESS_EQUAL"),
    (r"\>", "OP_GREATER"),
    (r"\<", "OP_LESS"),
    (r"\=", "OP_ASSIGN"),
    # Literals
    (r"[0-9]+\.[0-9]+", "LIT_FLOAT"),
    (r"[0-9]+", "LIT_INT"),
    (r"\'[a-zA-Z0-9]+\'", "LIT_CHAR"),
    (r"\"[a-zA-Z0-9]+\"", "LIT_CHAR"),
    (r"\btrue\b", "LIT_TRUE"),
    (r"\bfalse\b", "LIT_FALSE"),
    # Identifiers
    (r"[a-zA-Z_][a-zA-Z0-9_]*", "IDENTIFIER")
]
