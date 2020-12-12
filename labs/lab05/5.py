from math import gcd

class Rational:
    nom: int
    denom: int

    def __init__(self, nom, denom) -> None:
        if denom == 0:
            raise Exception()
        self.nom = nom
        self.denom = denom
        self.reduce()

    def reduce(self):
        if self.denom < 0:
            self.nom *= -1
            self.denom *= -1
        gcd_nom_denom = gcd(self.nom, self.denom)
        self.nom = self.nom // gcd_nom_denom
        self.denom = self.denom // gcd_nom_denom

    @classmethod
    def from_str(cls, arg):
        negative = (arg[0] == '-')
        if negative:
            nom, denom = arg[1:].split('/')
        else:
            nom, denom = arg.split('/')

        return cls(nom=-int(nom) if negative else int(nom), denom=int(denom))

    def to_float(self):
        return float(self.nom) / float(self.denom)

    def __add__(self, second):
        res = Rational(nom = self.nom*second.denom + self.denom*second.nom, denom = self.denom*second.denom)
        res.reduce()
        return res

    def __mul__(self, second):
        res = Rational(nom = self.nom*second.nom, denom = self.denom*second.denom)
        res.reduce()
        return res

    def __sub__(self, second):
        res = Rational(nom = self.nom*second.denom - self.denom*second.nom, denom = self.denom*second.denom)
        res.reduce()
        return res

    def __truediv__(self, second):
        res = Rational(nom = self.nom*second.denom, denom = self.denom*second.nom)
        res.reduce()
        return res


def test_reduce():
    a = Rational(1,1)
    assert a.nom == 1
    assert a.denom == 1

    b = Rational(4,6)
    assert b.nom == 2
    assert b.denom == 3


def test_operations():
    x = Rational(5,6)
    y = Rational(2,7)

    z = x + y
    assert z.nom == 47
    assert z.denom == 42

    z = x - y
    assert z.nom == 23
    assert z.denom == 42

    z = x * y
    assert z.nom == 5
    assert z.denom == 21

    z = x / y
    assert z.nom == 35
    assert z.denom == 12

def test_parse_from_string():
    x = Rational.from_str('3/9')
    assert x.nom == 1
    assert x.denom == 3

    y = Rational.from_str('-3/9')
    assert y.nom == -1
    assert y.denom == 3

def test_cast_to_float():
    x = Rational(1,16)
    as_float = x.to_float()
    assert as_float == 0.0625

test_reduce()
test_operations()
test_parse_from_string()
test_cast_to_float()
