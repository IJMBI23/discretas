### Definicion relacion

Sean $A$ y $B$ conjuntos. Una relacion $R$ es un conjunto de $A \times B$

A = ("a", "b", "c")
B = ("x", "y", "z")

AxB = {(a,b) for a in A for b in B}

print (AxB)

#Relacion como objeto
class Relation:
    """
    An OOP representation of a mathematical relation
    """
    def __init__(self, A, B = None, pairs = []):
        self.A = A
        self.B = B if B else A
        self.pairs = {p for p in pairs}

    def __contains__(self, pair):
        return pair in self.pairs

    def __str__(self):
        return f"Relation( {self.A}, {self.B}, {self.pairs})"

    def __len__(self):
        return len(self.pairs)

    def neighbors(self, x):
        return {b for (a, b) in self.pairs if a == x}


R = Relation({"a", "b"}, pairs=[("a", "a"), ("a", "b"), ("b", "b")])

print(("a", "b") in R)
print(len(R))

