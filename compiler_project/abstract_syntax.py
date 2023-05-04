class AstNode:
    def accept(self, visitor, args=None):
        name = self.__class__.__name__
        return getattr(visitor, "visit" + name)(self)


# Pas obligé de redéfinir tout le langage Dart de base
# et n'utiliser que les éléments nécessaires pour réaliser la visualisation de code.
# Attention !!! Cela peut générer des frustations de la part de l'utilisateur
# car son code risque de ne pas pouvoir s'exécuter.
# Objectif du langage: permettre de visualiser le code
# et les dépendances entre les éléments


class Identifier(AstNode):
    def __init__(self, value: str) -> None:
        self.value: str = value


class Class(AstNode):
    def __init__(self, name: Identifier, fields, methods):
        self.name: Identifier = name
        self.fields: list[Field] = fields
        self.methods: list[Method] = methods


class Field(AstNode):
    def __init__(self, name, type):
        self.name: Identifier = name
        self.type: TypeNode = type


class Method(AstNode):
    def __init__(self, name: Identifier, type, params, body):
        self.name: Identifier = name
        self.type: TypeNode = type
        self.params: list[Parameter] = params
        self.body = body


class Parameter(AstNode):
    def __init__(self, name, type):
        self.name: Identifier = name
        self.type: TypeNode = type


class TypeNode(AstNode):
    def __init__(self, value) -> None:
        self.value: str = value
