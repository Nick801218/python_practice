# import sys
# print(sys.path)

# Write Files

file=open("d:\\python\\python_practice\\File_Open&Handling\\data.txt", mode="w", encoding="utf-8")
#    open("file path", mode="file handling", encoding="utf-8 for chinese")
file.write("Hello File\nSecond Line\n測試中文")
file.close()

with open("d:\\python\\python_practice\\File_Open&Handling\\data2.txt",\
        mode="w", encoding="utf-8") as file:
    file.write("5\n4\n3")

# Read Files (Calculate the sum of numbers in file)

sum=0
with open("d:\\python\\python_practice\\File_Open&Handling\\data2.txt",\
        mode="r", encoding="utf-8") as file:
    for line in file: # Read the data line by line
        sum+=int(line)
print(sum)
