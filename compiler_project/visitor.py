from compiler_project.abstract_syntax import (
    Abstract,
    AstNode,
    Class,
    Field,
    Identifier,
    Method,
    Parameter,
    TypeNode,
)


class Visitor:
    def visit(self, node: AstNode):
        return node.accept(self)


class PrettyPrinter(Visitor):
    def visitAbstract(self, _abstract: Abstract):
        return f"abstract {_abstract._class.accept(self)}"

    def visitClass(self, _class: Class):
        code = (
            f"class {_class.name.accept(self)} {{\n"
            f"{''.join([field.accept(self) for field in _class.fields])}\n"
            f"{''.join([method.accept(self) for method in _class.methods])}\n"
            f"\t{_class.name.accept(self)}"
            f"(this.{', this.'.join([param.name.accept(self) for param in _class.fields])});\n"
        )
        return code + "}\n"

    def visitField(self, field: Field):
        return f"\t{field.type.accept(self)} {field.name.accept(self)};\n"

    def visitMethod(self, method: Method):
        code = (
            f"\t{method.type.accept(self)} {method.name.accept(self)}"
            + f"({', '.join([param.accept(self) for param in method.params])})"
            + " {\n"
        )
        if method.body is not None:
            code += f"\t\t{method.body}\n"
        code += "\n\t}\n"
        return code

    def visitParameter(self, param: Parameter):
        return f"{param.type.accept(self)} {param.name.accept(self)}"

    def visitTypeNode(self, type: TypeNode):
        return type.value

    def visitIdentifier(self, identifier: Identifier):
        return identifier.value


class CodeGraph(Visitor):
    def visitAbstract(self, _abstract: Abstract):
        code = f"class {_abstract._class.name.accept(self)} {{\n"
        code += "\t<<abstract>>\n"
        code += (
            f"{''.join([field.accept(self) for field in _abstract._class.fields])}\n"
        )
        code += (
            f"{''.join([method.accept(self) for method in _abstract._class.methods])}\n"
        )
        return code + "}\n"

    def visitClass(self, _class: Class):
        code = f"class {_class.name.accept(self)} {{\n"
        code += f"{''.join([field.accept(self) for field in _class.fields])}\n"
        code += f"{''.join([method.accept(self) for method in _class.methods])}\n"
        return code + "}\n"

    def visitField(self, field: Field):
        return f"\t+{field.type.accept(self)} {field.name.accept(self)}\n"

    def visitMethod(self, method: Method):
        return (
            f"\t+{method.name.accept(self)}"
            + f"({', '.join([param.accept(self) for param in method.params])}) "
            + f"{method.type.accept(self)}\n"
        )

    def visitParameter(self, param: Parameter):
        return f"{param.name.accept(self)}"

    def visitTypeNode(self, type: TypeNode):
        return type.value

    def visitIdentifier(self, identifier: Identifier):
        return identifier.value
