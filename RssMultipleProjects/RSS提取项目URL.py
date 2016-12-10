from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import (
    HTTPError,
    URLError,
    )
#html = request.urlopen('http://www.baidu.com')
#bsObj = BeautifulSoup(html.read(),'lxml')

#print(bsObj)
#
def Single_Html(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        print('网页未找到，请检查网络是否通畅，网址是否正确')
    else:
        bsObj = BeautifulSoup(html.read(), 'lxml')
        return bsObj

Rss = Single_Html('http://feeds.feedburner.com/Archdaily')

Proj_url = Rss.findAll('guid')
for url in Proj_url:
    print(url.get_text(),end='\n')

