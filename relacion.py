### Definicion relacion

Sean $A$ y $B$ conjuntos. Una relacion $R$ es un conjunto de $A \times B$

A = ("a", "b", "c")
B = ("x", "y", "z")

AxB = {(a,b) for a in A for b in B}

print (AxB)

#Relacion como objeto
#Relacion como objeto
class Relation:
    """
    An OOP representation of a mathematical relation
    """
    def __init__(self, A, B = None):
        self.A = A
        self.B = B if B else A

    def __str__(self):
        return f"Relation( {self.A}, {self.B})"


R = Relation({"a", "b"})

