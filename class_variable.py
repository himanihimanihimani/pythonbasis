class Person:
    raise_amount = 1.5 #class variable banko jo same class ma matr use garna milx
    def __init__( self,name,pay):
        self.name = name
        self.pay = pay
    def get_name(self):
        return self.name

    def appy_raise(self):
        self.pay = int(self.pay*self.raise_amount)
        return self.pay
p_1=Person("Himani", 200)
print(p_1.pay)
p_1.appy_raise()
print(p_1.pay)
