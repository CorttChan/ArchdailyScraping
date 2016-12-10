import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
import urllib.request,time,socket
from urllib.error import (
    HTTPError,
    URLError,
    ContentTooShortError
    )

new_html = open('test.html','r',encoding='utf-8')

# 获取需要下载的原始图片URL
bsobj = BeautifulSoup(new_html.read(),'lxml')
pic_gallery = bsobj.findAll('a',class_="gallery-thumbs-link")
url = []
for i in pic_gallery:
    url.append(i.img['data-src'].replace('thumb_jpg','large_jpg'))
    #print(i.img['data-src'], end='\n')


# 定义图片下载函数
print(len(url))
def get_1(url):
    index = 0
    socket.setdefaulttimeout(30)
    for i in url:
        print('正在下载第 '+str(index)+' 个图片')
        try:
            urlretrieve(i, str(index)+'.jpg')
            url.remove(i)
        except (HTTPError,URLError) as e:
            print('图片下载错误，稍后自动重试')
        index += 1
    return url


def get_2(url,n=0):
    # 设置全局超时时间
    timeout = 100
    socket.setdefaulttimeout(timeout)
    # 设置休眠时间
    sleep_download_time = 10
    # 初始化计数器
    index = 1
    # 添加'User-Agent'
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    user_headers = {'Connection':'keep-alive',
                    'Host':'images.adsttc.com',
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding':'gzip, deflate, sdch',
                    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
        }
    url_fail = []
    for i in url:
        req = urllib.request.Request(url=i, headers=user_headers)

        try:
            time.sleep(sleep_download_time)
            imgurl = urlopen(req)
            jpgpic = imgurl.read()
            imgurl.close()
        except (HTTPError, URLError) as e:
            print('错误代码： %s' % e)
            print('图片下载错误，稍后自动重试')
            index += 1
            url_fail.append(i)
        except socket.timeout as e:
            print('错误代码： %s' % e)
            print('图片下载错误，稍后自动重试')
            index += 1
            url_fail.append(i)
        else:
            imgfile = open('pic_' + str(n)+ '_' +str(index) + '.jpg', 'wb')
            print('Downloading: ' + 'pic' + str(index) + '.jpg')
            imgfile.write(jpgpic)
            imgfile.close()
            index += 1
    print('Total pics: '+str(index))
    print('下载失败链接数量： ' + str(len(url_fail)))


# get_1(url)

# 初始化循环计数器
#n = 0
#while len(url) != 0:
#    get_2(url,n)
#    n += 1
#    print('第： '+ str(n) + ' 次循环下载')

get_2(url)
print(len(url))
new_html.close()
print('文件读取完毕')