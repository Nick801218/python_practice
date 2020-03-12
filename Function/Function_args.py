# Function with default parameter value
def power(base,exp=0):
    print(base**exp)

power(3,2)
power(4) # If we call the function without argument, it uses the default value

#
def devide(n1,n2):
    print(n1/n2)

devide(4,2)
devide(n2=4,n1=2)

# If the number of arguments is unknown, add a * before the parameter name:
def avg(*value): # value : tuple
    sum=0
    for numbers in value:
        sum+=numbers
    print(sum/len(value))

avg(8,7)
avg(9,8.8,7,-2)




