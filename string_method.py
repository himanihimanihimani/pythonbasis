course = "python for beginners"
print(course[-2])
print(course[0:3])
print(course[0:])
print(course[:50])
# print(course[50])
print(course[1:-1])
print(len(course))
place = "himani"
print(place.capitalize())
print(place.upper())
print(place.count("i"))
print(place.replace("h", "n"))

txt = "Hello welcome to my universe."
x = txt.endswith(";")
print(x)
Y = txt.startswith("H")
print(Y)
print(place.find('m'))
print(place.find('z'))  #if string not found then it returns -1
text = ("30000")
x = text.zfill(16)
print(f"zfilled  {x}")

address = "Kohalpur"
print(address[::2])  # print every second character
print(address[::-1])  # print reverse
# stripsplit join
# strip removes trailing whitespaces.
# splitbreturns a list.
# join it concatenates string with another string
string_example = " Hello world "
print(string_example)
print(string_example.strip())
print(string_example.split())
a = string_example.split()  # make a variable for above string
print(a[0])



jwt_token = "jsdkjksjd.jkdsjks.jksjdsks.skjkslk.skkslasjdi,shhjshgjh.jsjhjjsdhj.shhjhjs"
b = jwt_token.split(".")
print(b)
print(b[0])
print(b[1])

place = " Himani sapkota"
d = (place.strip())
print(d)
e ="aa".join(d)
print(e)

f = place.split()
g ="".join(f)
print(g)


