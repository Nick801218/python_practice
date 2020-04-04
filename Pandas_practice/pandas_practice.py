import pandas as pd
data=pd.Series([20,10,15])
data=data==20
print(data)
print("========")

data=pd.DataFrame({
    "name":["John","Mary","BOb"],
    "salary":[20000,35678,42457]
})
print(data)
print("========")
print(data["name"])
print("========")
print(data.iloc[0])