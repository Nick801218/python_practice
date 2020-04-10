import pandas as pd

data=pd.DataFrame({
    "name":["Nick", "James", "Amy"],
    "salary":[50000, 35000, 60000]
},index=["A","B","C"])
print(data)
print("==============")
print("Numbers of elements:",data.size)
print("Numbers of rows and columns:",data.shape)
print("Data index:",data.index)
print("==============")
print("Get second row data by order:", data.iloc[1], sep="\n")
print("Get second row data by index:", data.loc["B"], sep="\n")
print("==============")
print("Get the column called \"name\":", data["name"], sep="\n")
print("==============")
data["revenue"]=[300000,400000,500000]
data["rank"]=pd.Series([3,2,1],index=["A","B","C"])
data["CP"]=data["revenue"]/data["salary"]
print(data)
