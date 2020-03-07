# dictionary (unordered, changeable and indexed)
dic={"a":"apple","d":"dog"}
print(dic)
print(dic["a"])

dic["a"]="ant"
print(dic["a"])

# in & not in
print("a" in dic)

#delete
del dic["a"]
print(dic)

# dictionary for variable {x:x**2 for x in [List]}
dic1={x:x**2 for x in [4,5,9,10]}
print(dic1)