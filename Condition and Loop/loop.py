# While loop

n=1          # 1+2+3+...+10(while loop)
sum=0
while n<=10:
    sum=sum+n
    n+=1
print(sum)


# For loop

for x in [3,5,1]:  # for variable in list:
    print(x)


for y in "Hello":  # for variable in string:
    print(y)


for z in range(5,10):  # for variable in range():
    print(z)


sum2=0                # 1+2+...+10(for loop)
for i in range(1,11):
    sum2=sum2+i
    i+=1
print(sum2)