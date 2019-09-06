

class Car(object):
    def __init__(self):
        self.speed = 0
    def move(self):
        ine = input()
        if ine == 'u':
            self.speed += 1
            print(self.speed)
        if ine == 'q':
            exit()



car1 = Car()

while True:
    car1.move()
