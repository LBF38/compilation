
from abstract_syntax import (AstNode,Circuit,Identifier,Body,Input,Output,Expression,Operator,Parameter)


class Visitor:
    def visit(self, node: AstNode):
        return node.accept(self)

class SimpleVisitor(Visitor):
    def visitCircuit(self, circuit:Circuit,args):
        code_string=f"circuit {circuit.identifier.accept(self)}\n"
        code_string+=f"\t{circuit.input.accept(self,args)}\n"
        code_string+=f"\t{circuit.output.accept(self)}\n"
        code_string+=f"\t{circuit.body.accept(self)}\n"
        code_string+="end"
        return code_string
    
    def visitIdentifier(self,identifier:Identifier,args):
        return identifier.name
    
    def visitInput(self,input:Input,args):
        input_string="input "
        for parameter in input.parameters:
            input_string+=parameter.accept(self)
            input_string+=", "
        input_string=input_string[:-2]
        return input_string
    
    def visitOutput(self,output:Output,args):
        output_string="output "
        for parameter in output.parameters:
            output_string+=parameter.accept(self)
            output_string+=", "
        output_string=output_string[:-2]
        return output_string
    
    def visitBody(self, body:Body,args):
        body_string=""
        for expression in body.expressions[:-1]:
            body_string+=expression.accept(self)+"\n\t"
        body_string+=body.expressions[-1].accept(self)
        return body_string
    
    def visitExpression(self,expression:Expression,args):
        return f"{expression.left.accept(self)} {expression.operator.accept(self)} {expression.right.accept(self)}"
    
    def visitOperator(self,operator:Operator,args):
        return operator.name
    
    def visitParameter(self,parameter:Parameter,args):
        return parameter.identifier.accept(self)
    