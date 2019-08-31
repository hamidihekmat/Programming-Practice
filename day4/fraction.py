

'''
@auth: Hekmat Hamidi
@purpose: To create and undestand how OOP works in python
'''
class Fraction:
    def __init__(self, num, den):
        '''
        Constructors for the class fraction -> numerator
                                            -> denominator
        '''
        self.num = num
        self.den = den

    def gcd(self,num, den):
        GCD = 0
        l = [num, den]
        g = max(l)
        m = min(l)
        n = g % m
        if n == 0:
            GCD = m
        while n != 0:
            GCD = n
            g = m
            m = n
            n = g % m
        return GCD

    def __str__(self):
        '''
        __str__ method overides the pre-existing object method
        allows the instance to be printed -> converts into str
        '''
        return '{}/{}'.format(str(self.num), str(self.den))

    def __add__(self, other):
        '''
        __add__ method allows fractions to be added
        f1.__add__(f2)
        '''
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        newden = self.den * other.den
        common = self.gcd(newnum,newden)
        # we return a fraction object with the numerator and denominator
        return Fraction(newnum//common,newden//common)

    def __sub__(self, other):
        '''
        __add__ method allows fractions to be subtracted
        f1.__sub__(f2)
        '''
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        newden = self.den * other.den
        common = self.gcd(newnum,newden)
        # we return a fraction object with the numerator and denominator
        return Fraction(newnum//common,newden//common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common,newden//common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum

    def __le__(self, other):
        f1 = self.num / self.den
        f2 = other.num / other.den
        return f1 < f2
    def __ge__(self, other):
        f1 = self.num / self.den
        f2 = other.num / other.den
        return f1 > f2

    def __gt__(self, other):
        f1 = self.num / self.den
        f2 = other.num / other.den
        return f1 > f2

    def __lt__(self, other):
        f1 = self.num / self.den
        f2 = other.num / other.den
        return f1 < f2

    def shownum(self):
        return self.num
        
    def showden(self):
        return self.den
