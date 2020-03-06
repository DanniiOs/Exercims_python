from __future__ import division
from math import gcd


class Rational:
    def _init_(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.numer = self.simply().numer
        self.denom = self.simply().denom

    def _eq_(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def _repr_(self):
        return '{}/{}'.format(self.numer, self.denom)

    def _add_(self, other):
        self.numer = self.numer * other.denom + self.denom * other.numer
        self.denom = self.denom * other.denom
        return self.simply()

    def _sub_(self, other):
        self.numer = self.numer * other.denom - self.denom * other.numer
        self.denom = self.denom * other.denom
        return self.simply()

    def _mul_(self, other):
        self.numer = self.numer * other.numer
        self.denom = self.denom * other.denom
        return self.simply()

    def _truediv_(self, other):
        self.numer = self.numer * other.denom
        self.denom = self.denom * other.numer
        return self.simply()

    def _abs_(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)
        return self.simply()

    def _pow_(self, power):
        self.numer = self.numer ** power
        self.denom = self.denom ** power
        return self.simply()

    def _rpow_(self, base):
        return (base ** (self.numer / self.denom))

    def _simply_(self):
        agcd = gcd(self.numer, self.denom)
        self.numer = self.numer // agcd
        self.denom = self.denom // agcd
        return self.signs()

    def signs(self):
        if(self.denom < 0):
            self.numer = self.numer * -1
            self.denom = self.denom * -1
        return self
