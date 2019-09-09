


class Fraction(object):
    def __init__(self, num, den):
        '''
        Constructors for the class fraction -> numerator
                                            -> denominator
        '''
        self.num = num
        self.den = den

    def __str__(self):
        '''
        __str__ method overides the pre-existing object method
        allows the instance to be printed -> converts into str
        '''
        return '{}/{}'.format(str(self.num), str(self.den))

    def __add__(self, otherfraction):
        '''
        __add__ method allows fractions to be added
        f1.__add__(f2)
        '''
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        # we return a fraction object with the numerator and denominator
        return Fraction(newnum, newden)




myf = Fraction(1,4)
myf2 = Fraction(1,2)
print(myf + myf2)

# Progress
# need to add the add method
