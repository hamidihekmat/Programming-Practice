
class Animal(object):

    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=''):
        self.name = newname

    def __str__(self):
        return str(self.age) + ' ' +  str(self.name)


class Cat(Animal):

    def speak(self):
        print('meow')

    def __str__(self):
        return 'Cat: ' + str(self.age) + ' ' + str(self.name)



class Person(Animal):

    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        self.friends.append(fname)

    def speak(self):
        print('hello')

    def age_diff(self, other):
        diff = self.age - other
        print(abs(diff), 'years different')

    def __str__(self):
        return 'person: ' + str(self.name) + str(self.age) + str(self.friends)

p = Person('Hekmat', 22)
p.add_friend('Shahram')
print(p)




'''
c = Cat(9)
c.set_name('Tommy')
print(c)
c.speak()
'''


'''
myanim = Animal(4)
myanim.set_name()
a = Animal(3)
a.set_name('Ace')
print(myanim.get_age())
print(myanim.get_name())
print(myanim)
print(a)
'''
