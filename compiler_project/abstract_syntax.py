class AstNode:
    def accept(self, visitor, args=None):
        name = self.__class__.__name__
        return getattr(visitor, 'visit' + name)(self, args)
