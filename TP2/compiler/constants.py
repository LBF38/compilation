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
    (r"int", "TYPE_INT"),
    (r"main", "KW_MAIN"),
    (r"if", "KW_IF"),
    (r"else", "KW_ELSE"),
    (r"while", "KW_WHILE"),
    (r"bool", "TYPE_BOOL"),
    (r"float", "TYPE_FLOAT"),
    (r"char", "TYPE_CHAR"),
    # Operators
    (r"\+", "OP_PLUS"),
    (r"\-", "OP_MINUS"),
    (r"\*", "OP_MULT"),
    (r"\/", "OP_DIV"),
    (r"\%", "OP_MOD"),
    (r'\|\|', 'OP_OR'),
    (r"\&\&", "OP_AND"),
    (r"\!", "OP_NOT"),
    (r"\=", "OP_ASSIGN"),
    (r"\=\=", "OP_EQUAL"),
    (r"\!\=", "OP_NOT_EQUAL"),
    (r"\>", "OP_GREATER"),
    (r"\>=", "OP_GREATER_EQUAL"),
    (r"\<", "OP_LESS"),
    (r"\<=", "OP_LESS_EQUAL"),
    # Literals
    (r"[0-9]+\.[0-9]+", "LIT_FLOAT"),
    (r"[0-9]+", "LIT_INT"),
    (r"\'[a-zA-Z0-9]\'", "LIT_CHAR"),
    (r"\"[a-zA-Z0-9]\"", "LIT_CHAR"),
    (r"true", "LIT_TRUE"),
    (r"false", "LIT_FALSE"),
    # Identifiers
    (r"[a-zA-Z_][a-zA-Z0-9_]*", "IDENTIFIER")
]
