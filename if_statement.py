from numbers import Number

a= 200
b= 33
if b>a:
    print("b is greater than a")
elif a== b:
    print("a and b are equal")
else:
    print("a is greater than b")

is_hot = False
is_cold = False
if is_hot or is_cold:
    print("Drink more water and keep your body warm")
#elif is_cold:
    #print("keep your body warm")
else:
    print("its a lovely day")


amount=1000
is_good_credit=False
if is_good_credit:
    down_payment=amount*(10/100)
    print(down_payment)
else:
    down_payment=amount*(20/100)
    print(down_payment)


speed=80
if speed>60:
 print("accident can be occur")
else:
    print("safe mode")

n = int(input("Enter number  "))
if n % 2 == 0:
    print("Number is even")
else:
    print("Odd Number")


