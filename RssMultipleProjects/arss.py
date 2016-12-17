#!python3
#-*- coding：utf-8 -*-
# __author__ = 'CorttChan<cortt.me@gmail.com>'


import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import (HTTPError,URLError)


# Archdaily_Rss_Url
#Rss = 'http://feeds.feedburner.com/Archdaily'

def getrsspros(url='http://feeds.feedburner.com/Archdaily'):
    # 初始话RSS项目url列表
    pro_rss = []
    # 添加'User-Agent'
    headers = ('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
    # 读取项目网页
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    try:
        html = opener.open(url)
    except (HTTPError,URLError) as e:
        print('--------------------网络连接错误： %s' % e)
        print('网页未找到，请检查网络是否通畅，网址是否正确')
    except Exception as e:
        print('--------------------网络连接错误： %s' % e)
    else:
        # 解析项目网址
        bsObj = BeautifulSoup(html.read(), 'lxml')
        Proj_url = bsObj.findAll('guid')
        # print(len(Proj_url))
        for i in Proj_url:
            # print(i.get_text())
            pro_rss.append(i.get_text())
    return pro_rss

if __name__ == '__main__':
    getrsspros()

# print(getrsspros())
