class point:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    # define object method
    def show(self):
        print(self.x,self.y)

    def dis(self,targetX,targetY):
        return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5


# Object 1
p1=point(3,4)

p1.show() # Call object method

d1=p1.dis(0,0) # Calculate the distance between (0,0) and (3,4)
print(d1)

# Object 2
p2=point(5,6)

p2.show()

d2=p2.dis(0,0) # Calculate the distance between (0,0) and (5,6)
print(d2)

# Create files and read it
class file:
    def __init__(self,name):
        self.name=name
        self.file=None
    def open(self,content):
        self.file=open(self.name, mode="w", encoding="utf-8")
        self.file.write(content)
        self.file.close()
    def read(self):
        self.file=open(self.name, mode="r", encoding="utf-8")
        return self.file.read()

f1=file("data1.txt")
f1.open("hello world")
data1=f1.read()
print(data1)

f2=file("data2.txt")
f2.open("my name is Nick")
data2=f2.read()
print(data2)