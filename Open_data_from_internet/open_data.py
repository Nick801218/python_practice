# Connet to the internet

# import urllib.request as request

# src="https://www.ncu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") # get source code from ncu website (HTML ,CSS or JS)
# print(data)


import urllib.request as request
import json

src="https://data.taipei/api/getDatasetInfo/downloadResource?id=b60ae44f-2c0e-4b9f-b76c-914db5213c78&rid=e1e768f0-4351-4371-acc4-53a26f9894d7"
with request.urlopen(src) as response:
    data=json.load(response)
#print(data)
ilist=data['PW000a']['dimension']['項目']['category']['index']

# Retrieve data you want
with open("area.txt","w",encoding="utf-8") as file:
    for area in ilist:
        file.write(area+"\n")
