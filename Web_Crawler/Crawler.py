#
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"

request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"

})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

#
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="title")
with open("title.txt","w",encoding="utf-8") as file:
    for title in titles:
        if title.a != None:
            file.write(title.a.string+"\n")