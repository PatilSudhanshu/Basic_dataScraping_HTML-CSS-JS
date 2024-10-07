import requests as rq 

from bs4  import BeautifulSoup

BUrl = 'https://books.toscrape.com/'

BHeader = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}



def startHtml(BUrl = None, BHeader=None):
    if BUrl:
        BResp = rq.get(url=BUrl, headers= BHeader)

        bSoup = BeautifulSoup(BResp.content, "html.parser")

        return bSoup
    else:
        return 'please send correct url'