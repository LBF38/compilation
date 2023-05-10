class Ponctuation_ruleset:
    L_PAREN = "L_PAREN"
    R_PAREN = "R_PAREN"
    L_CURL_BRACKET = "L_CURL_BRACKET"
    R_CURL_BRACKET = "R_CURL_BRACKET"
    L_SQUARE_BRACKET = "L_SQUARE_BRACKET"
    R_SQUARE_BRACKET = "R_SQUARE_BRACKET"
    SEMICOLON = "SEMICOLON"
    COMMA = "COMMA"


class Keyword_ruleset:
    MAIN = "KW_MAIN"
    VOID = "KW_VOID"
    IF = "KW_IF"
    ELSE = "KW_ELSE"
    WHILE = "KW_WHILE"
    RETURN = "KW_RETURN"
    ABSTRACT = "KW_ABSTRACT"
    CLASS = "KW_CLASS"
    TYPEDEF = "KW_TYPEDEF"
    FINAL = "KW_FINAL"
    THIS = "KW_THIS"


class Type_ruleset:
    INT = "TYPE_INT"
    DOUBLE = "TYPE_DOUBLE"
    DYNAMIC = "TYPE_DYNAMIC"
    BOOL = "TYPE_BOOL"
    STRING = "TYPE_STRING"
    LIST = "TYPE_LIST"
    VOID = Keyword_ruleset.VOID


class Operator_ruleset:
    PLUS = "OP_PLUS"
    MINUS = "OP_MINUS"
    MULT = "OP_MULT"
    DIV = "OP_DIV"
    MOD = "OP_MOD"
    OR = "OP_OR"
    AND = "OP_AND"
    EQUAL = "OP_EQUAL"
    NOT_EQUAL = "OP_NOT_EQUAL"
    NOT = "OP_NOT"
    GREATER_EQUAL = "OP_GREATER_EQUAL"
    LESS_EQUAL = "OP_LESS_EQUAL"
    GREATER = "OP_GREATER"
    LESS = "OP_LESS"
    ASSIGN = "OP_ASSIGN"
    DOT = "OP_DOT"


class Literal_ruleset:
    FLOAT = "LIT_FLOAT"
    INT = "LIT_INT"
    STRING = "LIT_STRING"
    TRUE = "LIT_TRUE"
    FALSE = "LIT_FALSE"


class Identifier_ruleset:
    IDENTIFIER = "IDENTIFIER"


class Cleaning_ruleset:
    COMMENT = "COMMENT"
    WHITESPACE = "WHITESPACE"


LEXEM_RULES = [
    # Comments and whitespaces
    (r"\/\/.*", Cleaning_ruleset.COMMENT),
    (r"[ \t\n]+", Cleaning_ruleset.WHITESPACE),
    # Special characters - Ponctuation
    (r"\(", Ponctuation_ruleset.L_PAREN),
    (r"\)", Ponctuation_ruleset.R_PAREN),
    (r"\{", Ponctuation_ruleset.L_CURL_BRACKET),
    (r"\}", Ponctuation_ruleset.R_CURL_BRACKET),
    (r"\[", Ponctuation_ruleset.L_SQUARE_BRACKET),
    (r"\]", Ponctuation_ruleset.R_SQUARE_BRACKET),
    (r";", Ponctuation_ruleset.SEMICOLON),
    (r",", Ponctuation_ruleset.COMMA),
    # Keywords
    (r"\bmain\b", Keyword_ruleset.MAIN),
    (r"\bvoid\b", Keyword_ruleset.VOID),
    (r"\bif\b", Keyword_ruleset.IF),
    (r"\belse\b", Keyword_ruleset.ELSE),
    (r"\bwhile\b", Keyword_ruleset.WHILE),
    (r"\breturn\b", Keyword_ruleset.RETURN),
    (r"\babstract\b", Keyword_ruleset.ABSTRACT),
    (r"\bclass\b", Keyword_ruleset.CLASS),
    (r"\btypedef\b", Keyword_ruleset.TYPEDEF),
    (r"\bfinal\b", Keyword_ruleset.FINAL),
    (r"\bthis\b", Keyword_ruleset.THIS),
    # Types
    (r"\bint\b", Type_ruleset.INT),
    (r"\bdouble\b", Type_ruleset.DOUBLE),
    (r"\bdynamic\b", Type_ruleset.DYNAMIC),
    (r"\bbool\b", Type_ruleset.BOOL),
    (r"\bString\b", Type_ruleset.STRING),
    (r"\bList\b", Type_ruleset.LIST),
    # (r"\bList<()>\b", "TYPE_LIST"), # TODO: List<type> => ou dans le parser ?
    # Operators
    (r"\+", Operator_ruleset.PLUS),
    (r"\-", Operator_ruleset.MINUS),
    (r"\*", Operator_ruleset.MULT),
    (r"\/", Operator_ruleset.DIV),
    (r"\%", Operator_ruleset.MOD),
    (r"\|\|", Operator_ruleset.OR),
    (r"\&\&", Operator_ruleset.AND),
    (r"\=\=", Operator_ruleset.EQUAL),
    (r"\!\=", Operator_ruleset.NOT_EQUAL),
    (r"\!", Operator_ruleset.NOT),
    (r"\>\=", Operator_ruleset.GREATER_EQUAL),
    (r"\<\=", Operator_ruleset.LESS_EQUAL),
    (r"\>", Operator_ruleset.GREATER),
    (r"\<", Operator_ruleset.LESS),
    (r"\=", Operator_ruleset.ASSIGN),
    (r"\.", Operator_ruleset.DOT),
    # Literals
    (r"[0-9]+\.[0-9]+", Literal_ruleset.FLOAT),
    (r"[0-9]+", Literal_ruleset.INT),
    (r"\'[a-zA-Z0-9]+\'", Literal_ruleset.STRING),
    (r"\"[a-zA-Z0-9]+\"", Literal_ruleset.STRING),
    (r"\btrue\b", Literal_ruleset.TRUE),
    (r"\bfalse\b", Literal_ruleset.FALSE),
    # Identifiers
    (r"[a-zA-Z_][a-zA-Z0-9_]*", Identifier_ruleset.IDENTIFIER),
]
