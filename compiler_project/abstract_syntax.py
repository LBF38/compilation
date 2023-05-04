class AstNode:
    def accept(self, visitor, args=None):
        name = self.__class__.__name__
        return getattr(visitor, "visit" + name)(self, args)


# Pas obligé de redéfinir tout le langage Dart de base
# et n'utiliser que les éléments nécessaires pour réaliser la visualisation de code.
# Attention !!! Cela peut générer des frustations de la part de l'utilisateur
# car son code risque de ne pas pouvoir s'exécuter.
# Objectif du langage: permettre de visualiser le code
# et les dépendances entre les éléments


class Class(AstNode):
    def __init__(self, name, fields, methods):
        self.name = name
        self.fields = fields
        self.methods = methods


class Field(AstNode):
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Method(AstNode):
    def __init__(self, name, type, params, body):
        self.name = name
        self.type = type
        self.params = params
        self.body = body


class Parameter(AstNode):
    def __init__(self, name, type):
        self.name = name
        self.type = type


class TypeNode(AstNode):
    def __init__(self, type) -> None:
        self.type = type
