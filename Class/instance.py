class point:
    def __init__(self,a,b):
        self.x=a
        self.y=b
# Object 1
p1=point(3,4)
print(p1.x,p1.y)
# Object 2
p2=point(5,6)
print(p2.x,p2.y)


class FULLNAME:
    def __init__(self,first,last):
        self.f=first
        self.l=last

name1=FULLNAME("Nick","Wu")
print(name1.f,name1.l)
name2=FULLNAME("Jeremy","Lin")
print(name2.f,name2.l)

