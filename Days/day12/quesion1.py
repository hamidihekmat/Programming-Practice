
'''
Construct a class hierarchy for people on a college campus. Include faculty, staff, and students.
What do they have in common? What distinguishes them from one another?

'''


class People:

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def getName(self):
        return self.name

    def getDob(self):
        return self.dob

    def setName(self, newName):
        self.name = newName

    def setDob(self, newDob):
        self.dob = newDob



class Faculty(People):

    def __init__(self, name, dob, role):
        super().__init__(name, dob)
        self.setName(name)
        self.setDob(dob)
        self.role = role

    def getRole(self):
        return self.role

    def setRole(self, newRole):
        self.role = newRole

    def __str__(self):
        return 'My name is {} and my role is {}!'.format(self.name, self.role)




p = Faculty('Hekmat', '05/12/1997', 'Prof')

print(p.getName())
p.setName('Kevin')
print(p.getName())
print(p.getRole())
print(p)
