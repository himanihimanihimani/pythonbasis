# python decorater allows to change the behavior of a function without modifying the function itself and takes another function as a parameter.
def decrotater_function(orignal_function):
    def wrapper_function(*args, **kwargs):
        print("start.....")
        result = orignal_function(*args, **kwargs)
        print(result)
        print("End......")
        return result

    return wrapper_function


@decrotater_function
def name(a):
    return a


@decrotater_function
def place(b):
    return b


x = name("david")
print(x)
y = place("NPK")
print(y)


