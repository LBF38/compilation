class Types:
    INT = "int"
    DOUBLE = "double"
    DYNAMIC = "dynamic"


listoftypes = [
    Types().__getattribute__(atype)
    for atype in dir(Types)
    if not atype.startswith("__")
]
# print([atype for atype in Types])
print(listoftypes)
print(type(listoftypes))
print([type(atype) for atype in listoftypes])
