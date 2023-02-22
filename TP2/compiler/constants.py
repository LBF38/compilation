LEXEM_REGEXES = [
    # Comments and whitespaces
    (r"\/\/.*", "COMMENT"),
    (r"[ \t\n]+", None),
    # Special characters
    (r"\(", "L_PAREN"),
    (r"\)", "R_PAREN"),
    (r"\{", "L_CURL_BRACKET"),
    (r"\}", "R_CURL_BRACKET"),
    # Keywords
    (r"int", "TYPE_INT"),
    (r"main", "KW_MAIN"),
]
