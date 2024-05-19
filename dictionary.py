info ={
    #"key": "value"
    "name": "Himani",
    "address": "KLP",
    "age": 24,
    "is_verified": True,
}
print(info["name"])
print(info)
info["address"] = "KTM"#changes values of dictionary
print(info["address"])
print(info)
del info["is_verified"]#delet the key
print(info)
info["gender"]="FEMALE"#Add key in dictionary
print(info)
for key,value in info.items():
    print(f' "key:{key}":value{value}')

#nested dictionary
my_family ={
    "child1":{
        "name": "ABC",
        "year": 2001
    },
"child2":{
    "name": "XYZ",
     "year": 2003
},
"child3":{
    "name": "MNQ",
    "year": 2005
}
}
print(my_family["child2"]["name"])
del my_family["child3"]["year"]
my_family["child1"]["Gender"] ="Male"
print(my_family)