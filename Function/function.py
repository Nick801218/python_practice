# define functions
def multiply():
    print(3*4)

def multiply2(n1,n2):
    print(n1*n2)

def add(n1,n2): # Let a function return a value
    print(n1+n2)
    return 0

def add2(n1,n2):
    return n1+n2

def sum(n1,n2): # n1+(n1+1)+(n1+2)+.....+n2
    sum=0
    for n in range(n1,n2+1):
        sum+=n
    print(sum)

# call functions
multiply()

multiply2(5,6)

value=add(3,4)
print(value)

value2=add2(3,4)*add2(1,2) # (3+4)*(1+2)
print(value2)

sum(5,30)
sum(1,10)
