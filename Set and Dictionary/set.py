# set (unordered and unindexed)
s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 # s1 and s2
s4=s1|s2 # s1  or s2
s5=s1-s2 # Complement : s1 - (s1 & s2)
s6=s1^s2 # inverse of intersection

print("s1=",s1)
print("s2=",s2)
print("s3=",s3)
print("s4=",s4)
print("s5=",s5)
print("s6=",s6)

# set(string)
s=set("Hello")
print(s)


# in & not in
print("3 is in s1 ,",3 in s1)
print("7 is in s4 ,",7 in s4)
print("3 is not in s1 ,",3 not in s1)
print("7 is not in s3 ,",7 not in s3)
print("H is in s ,","H" in s)
print("A is in s ,","A" in s)