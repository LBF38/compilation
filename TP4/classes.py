
class AST:
    def __init__(self) -> None:
        self.tree: list(AstNode)


class AstNode:
    def accept(self, visitor, args=None):
        name = self.__class__.__name__
        getattr(visitor, 'visit' + name)(self, args)


class Voiture(AstNode):
    def __init__(self) -> None:
        self.moteur = Moteur()
        self.roues = [Roue(), Roue(), Roue(), Roue()]
        self.carrosserie = Carrosserie()


class Moteur(AstNode):
    def __init__(self) -> None:
        pass


class Roue(AstNode):
    def __init__(self) -> None:
        pass


class Carrosserie(AstNode):
    def __init__(self) -> None:
        pass
