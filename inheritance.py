class person:
    def __init__(self,name,place):
        self.name =name
        self.place = place

    def info(self):
        return (self.name,self.place)

class Emplyoee(person):
    pass

a = Emplyoee("ABC","NPJ")
print(a.info())

class Dog:
    def eat(self):
        print("Dog is eating")

class Animal(Dog):
    def display(self):
        print("Display")

a = Animal()
a.display()
a.eat()

class He:
    def hear(self):
        print("He can hear")
        def see(self):
            print("He can see")
class She:
    def walk(self):
        print("She can walk")

class person(He,She):
    pass
a = person()
a.hear()
a.walk()