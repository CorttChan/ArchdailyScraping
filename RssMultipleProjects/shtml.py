#!python3
#-*- coding：utf-8 -*-
# __author__ = 'CorttChan<cortt.me@gmail.com>'

import urllib.request
import socket
from colorama import Fore,init
from bs4 import BeautifulSoup
from urllib.error import (HTTPError,URLError)

# 定义获取项目网页函数'GetHTML'
def GetHTML(url):
    init(autoreset=True)
    print('\n' + '--------------------项目网页解析中……')
    # 添加'User-Agent'
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
    # 读取项目网页
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    try:
        html = opener.open(url)
        Project_bs = BeautifulSoup(html.read(), 'lxml')
        html.close()
    except (HTTPError,URLError) as e:
        print(Fore.RED + '--------------------网页未找到，请检查网络是否通畅，网址是否正确')
    except socket.timeout as e:
        print(Fore.RED + '--------------------网络连接超时，请稍后重试')
    else:
        return Project_bs
