import random



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
'''
p = Person('Hekmat', 22)
p.add_friend('Shahram')
print(p)
'''

class Student(Person):

    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    
    def change_major(self, major):
        r = random.random()
        if r < 0.25:
            print('I have homework!')
        else:
            print('I dont have homework!')
        
    def __str__(self):
        return 'Student: {} is {} years old and majoring in {}'.format(self.name, self.age, self.major)

    
s = Student('Hekmat', 22, 'Computer Programming')



class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag # class variable always stays the same!
        Rabbit.tag += 1
        '''
        When an instance is created, the self.rid will be 1
        after other instances the self.rid will be incremented by 1 
        '''

    def get_rid(self):
        print(self.rid)

    def __add__(self, other):
        # return object rabbit
        return Rabbit(0, self, other)



r1 = Rabbit(3, 'Greg', 'Heedong')
r2 = Rabbit(3, 'Dan', 'Fan')

s = r1 + r2

s.get_rid()