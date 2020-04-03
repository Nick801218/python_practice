#
import urllib.request as req
def getdata(url):


    request=req.Request(url, headers={
        "Cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"

    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    #
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")

    with open("title_goss.txt","w",encoding="utf-8") as file:
        file.write("")

    with open("title_goss.txt","a",encoding="utf-8") as file:
        for title in titles:
            if title.a != None:
                file.write(title.a.string+"\n")
    nextlink=root.find("a", string="‹ 上頁")
    return nextlink["href"]


pageurl="https://www.ptt.cc/bbs/Gossiping/index.html"
for i in range(0,3):
    pageurl="https://www.ptt.cc"+getdata(pageurl)
