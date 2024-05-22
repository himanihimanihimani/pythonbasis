#classes inpython are used for creating objects that bundle.
#data(attributes) and methods(functions) together.
#They serve as blueprints for creating instances,which are individual objects with their own unique attributes and behavior.

# self
#the word self is used to represent the instance of a class.
#by using the "self" keyword use acess the attributes and methods of the class in python.

# **init** method
#"**int**" is a reserved method in python clase.
# it is called as constructor &this method is called when an object is created from the class
#and it allows the class to initialization the attributes of the class.


class Emplyoee:
    def __init__(self, first, last, email, address):
        self.first = first
        self.last = last
        self.email = email
        self.address = address

    def fullname(self):  #create method
        return self.first, self.last

    def  em_email(self):
        return self.email

    def emp_address(self):
        return self.address

    def abc(self):
        return self.fullname()


emp_1 = Emplyoee("Himani", "Sapkota", "sapkotahimani59@gmail.com", "KLP")
print(emp_1.fullname())
print(emp_1. em_email())

emp_2 = Emplyoee("XYZ","ABC","xyzabc@gmail.com","NPJ")
print(emp_2.fullname())
print(emp_2.emp_address())