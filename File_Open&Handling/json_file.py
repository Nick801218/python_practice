# Read json
import json
with open("d:\\python\\python_practice\\File_Open&Handling\\config.json",\
         mode="r", encoding="utf-8") as file:
    data=json.load(file) # data is dictionary
print(data)# data is dictionary
print(data["name"])
print(data["version"])
data["name"]="new name" # modify "name" in data "not in config.jason"
print(data)

# Replace the old data by lastest data in config.jason
with open("d:\\python\\python_practice\\File_Open&Handling\\config.json",\
         mode="w", encoding="utf-8") as file:
    json.dump(data,file)