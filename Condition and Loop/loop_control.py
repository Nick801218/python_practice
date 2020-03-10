# break
n=0
while n<5:
    if n==3:
        break
    print("n inside while loop:",n)
    n+=1

print("n outside while loop:",n)

# continue
m=0
for x in range(5):
    if x%2==0:
        continue
    print(x)
    m+=1

print("The number of odd numbers between 0 and 4 = ",m)


# else
sum=0
for i in range(1,11):
    sum=sum+i
else:
    print(sum)

# Exercise: Find the square of an integer

# Answer 1 :
inte=int(input("Input a integer :"))
s=inte**0.5
if s-int(s)==0:
    print("The square of input integer =",s)
else:
    print("The square of input integer is not an integer")

# Answer 2 (must use break and else):

inte2=int(input("Input a integer :"))
for s2 in range(inte2+1):
    if s2*s2==inte2:
        print("The square of input integer :",s2)
        break
else:
    print("The square of input integer is not an integer")

