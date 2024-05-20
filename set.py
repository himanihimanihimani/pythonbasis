#set store multiple value in single variable
my_set = {1, 2, 3, 4, 5, 6, 5, 43, 3, 12, 1, 2}
print(my_set)
this_set = {"apple", "mango", "banana", "cherry", True, 1, 2}
print(this_set)
this_set1 = {"apple", "mango", "banana", "cherry", False, 0, 2}
print(this_set1)

a = {"npj", "ktm", "bardiya"}
a.add("btl")
print(a)

set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {3, 4, 5, 6, 7, 8}
set_3 = set_1.union(set_2)
print(f"union:{set_3}")
set_4 = set_1.intersection(set_1)
print(f"intersection:{set_4}")

#multiple set intersection
set_5 = {1, 2, 3, 4, 5, 6}
set_6 = {1, 2, 3, 4, 5}
set_7 = {5, 6, 7}
set_8 = set_5.intersection(set_6)
set_9 = set_8.intersection(set_7)
print(set_9)
#Difference
set_10 = {"Google", "chrome", "apple"}
set_11 = {"apple", "microsoft"}
set_12 = set_10.difference(set_11)
print(set_12)

#python frozenset()
# A frozenset is an unorderd and uninxed collection of unique elements.
#It is a immultable.it is also called an immutable set.
# since the elements are fixed,unlike sets you can't add or remove elements

fruits = {"Apple", "Banana", "cherry", "Apple", "kiwi"}
basket = frozenset(fruits)
print("unique elements:", basket)
#add new fruit throws an error!
basket.add("orange")
print("after adding new elements:", basket)
city = {"npj", "klp", "Basghdi", "ppt"}
city_1 =  frozenset(city)
print(city_1.union(basket))

