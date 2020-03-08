# condition
# a==b : Equals
# a!=b : Not equals
# a<b  : Less than
# a<=b : Less than or equal to
# a>b  : Greater than
# a>=b : Greater than or equal to

# x=input("Please enter a number :") # The number you enter is a string
# x=float(x) # Convert a string to an integer

# if x>=100:
#     print("x is greater than or equal to 100")
# elif x>50:
#     print("x is greater than 50 and Less than 100 ")
# else:
#     print("x is less than or equal to 50")


# Operator

x=float(input("Please enter a number :"))
y=float(input("Please enter a number :"))
op=input("Please slect an operator (+,-,*,/) : ")

if op=="+":
    print("x+y=",x+y)
elif op=="-":
    print("x-y=",x-y)
elif op=="*":
    print("x*y=",x*y)
elif op=="/":
    print("x/y=",x/y)
else:
    print("Operator is not supported")
