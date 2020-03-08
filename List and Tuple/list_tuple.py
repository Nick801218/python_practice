#List (ordered and changeable)
#       0  1  2  3  4
#       ↓  ↓  ↓  ↓  ↓
grades=[39,98,77,63,2]
data=[[3,4,5],[7,8,9]]
print(grades)
print(grades[3])
grades[0]=55
print(grades)
print(grades[1:4])# start at index 1 (included) and end at index 4 (not included)
grades[1:4]=[0,0,0]
print(grades)
grades=grades+[12,45,8]
print(grades)
grades.insert(5,11)# inserts the specified value at the specified position
print(grades)
print(len(grades))
print(data[0][2])
#Tuple (ordered and unchangeable)
#       0  1  2  3  4
#       ↓  ↓  ↓  ↓  ↓
grades=(39,98,77,63,2)
data=((3,4,5),(7,8,9))
grades[3]=10 #error