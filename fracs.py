import math
from copy import deepcopy

class Rational:
    def __init__(self, num, denom):
        if not isinstance(num, int):
            raise RuntimeError('numerator must be integral')
        if not isinstance(denom, int):
            raise RuntimeError('denominator must be integral')

        self.num = num
        self.denom = denom

        self.reduce()

    def reduce(self):
        negative = (self.denom < 0 and self.num > 0) or (self.denom > 0 and self.num < 0)
        if negative:
            if self.denom < 0:
                self.denom = -self.denom
                self.num = -self.num

        g = int(math.gcd(self.num, self.denom))
        if g == 1:
            return
        self.num //= g
        self.denom //= g

    def invert(self):
        tmp = self.num
        self.num = self.denom
        self.denom = tmp

        self.reduce()

        return self

    def __add__(self, other):
        if isinstance(other, int):
            return self + Rational(other, 1)
        if isinstance(other, Rational):
            final_denom = self.denom * other.denom
            selfnum = self.num * other.denom
            othernum = other.num * self.denom

            self.num = selfnum + othernum
            self.denom = final_denom

            self.reduce()

            return self

        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            return self + Rational(other, -1)

        if isinstance(other, Rational):
            copy = deepcopy(other)
            copy.num = -copy.num
            return self + copy

        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return self * Rational(other, 1)

        if isinstance(other, Rational):
            self.num *= other.num
            self.denom *= other.denom

            self.reduce()

            return self

        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            return self * Rational(1, other)

        if isinstance(other, Rational):
            return self * other.invert()

        return NotImplemented

    def __floordiv__(self, other):
        self = self / other
        self.num = int(math.floor(float(self)))
        self.denom = 1

        return self

    def __lt__(self, other):
        return float(self) < float(other)

    def __eq__(self, other):
        self.reduce()
        other.reduce()
        return self.num == other.num and self.denom == other.denom

    def __le__(self, other):
        return self < other or self == other

    def __float__(self):
        return self.num / self.denom

    def __repr__(self):
        return '{}'.format(float(self))

def test(N=10):
    d = {}
    for i in range(1, N):
        for j in range(1,N):
            if Rational(i, j) > Rational(1,1):
                continue
            if i == j:
                continue
            d[(i,j)] = Rational(i,j)
            if N * N < 1000:
                print('{}/{} -> {}'.format( i, j, Rational(i,j)))

    l = [float(f) for f in sorted(d.values())]
    l = sorted(list(set(l)))
    import matplotlib.pyplot as plt
    plt.plot(l, [1]*len(l), linestyle='', marker='|')
    plt.show()
    if N * N < 1000:
        print(l)
    MM = -1
    prev = Rational(0,1)

    import numpy as np

    print(np.diff(l).max())

    for r in l:
        continue
        print(np.diff(np.array(l)), r.num, r.denom)

