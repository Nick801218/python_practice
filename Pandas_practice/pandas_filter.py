import pandas as pd

data=pd.Series([10, 39, 68])
condition=[True, False, True]
print(data[condition])
condition=data>18
print(data[condition])