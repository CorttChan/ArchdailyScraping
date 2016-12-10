#!python3
# coding:utf-8

# __author__ = 'CorttChan<cortt.me@gmail.com>'

import urllib.request
import time
import socket
import wget
from bs4 import BeautifulSoup
from urllib.error import (HTTPError,URLError)

# 输入Archdaily项目网址
project_url = input('请输入Archdaily项目网址:')

# 定义获取项目网页函数'GetHTML'
def GetHTML(url):
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
        print('网页未找到，请检查网络是否通畅，网址是否正确')
    except socket.timeout as e:
        print('网络连接超时，请稍后重试')
    else:
        return Project_bs


# 定义获取原始图片地址函数'Geturls'
def Geturls(html_bs):
    pic_gallery = html_bs.findAll('a', class_="gallery-thumbs-link")
    pics_original_url = []
    # 解析项目原图url
    for i in pic_gallery:
        pics_original_url.append(i.img['data-src'].replace('thumb_jpg', 'large_jpg'))
    # 原图url修改
    pics_url = []
    for i in pics_original_url:
        pics_url.append(i.split('?')[0])
    # 返回项目原图url列表
    return pics_url


# 定义创建项目文件夹目录函数
def mkdir(path):
    import os
    print('--------------------创建项目文件夹:')
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path + '\n' + '--------------------项目文件夹创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + '目录已存在')
        return False

# 定义获取项目标题函数'Gettitl'
def Gettitl(html_bs):
    # 定义要创建的目录
    project_name = html_bs.find('h1',{"class": "afd-title-big afd-title-big--bmargin-small afd-relativeposition"}).get_text()
    # 去除项目名称中的特殊字符
    # 去除首位空格
    project_name = project_name.strip()
    # 去除特殊字符
    intab = ' /+'
    outtab = '___'
    trantab = project_name.maketrans(intab, outtab)
    project_name = project_name.translate(trantab)
    downloadDir = '.\\Archdaily\\'
    project_Dir = downloadDir + project_name
    return project_Dir


def Download_imgs(url,path):
    print('--------------------项目原图总数: ' + str(len(url)) + ' 张')
    # 设置全局超时时间
    socket.setdefaulttimeout(50)
    # 初始循环计数器
    loop = 1
    # 初始化计数器
    index = 1
    # 初始图片数量
    pics_num = len(url)
    # 初始化下载错误链接url
    # failurl = []
    # 初始化已完成连接url
    sucurl = []
    while True:
        for i in url:
            if i not in sucurl:
                try:
                    print('\n' + '开始下载第 __' + str(loop) + '_' + str(index) + '__ 张图片：')
                    file = wget.download(i, path)
                except socket.timeout as e:
                    print('\n' + '--------------------网络连接错误： %s' % e)
                    print('--------------------图片下载错误，稍后自动重试')
                    index += 1
                    # failurl.append(i)
                except Exception as e:
                    print('\n' + '--------------------网络连接错误： %s' % e)
                    print('--------------------图片下载错误，稍后自动重试')
                    index += 1
                    # failurl.append(i)
                else:
                    index += 1
                    sucurl.append(i)
                    # print(file + '\n' + '下载完毕')
                time.sleep(1)
            else:
                continue
        loop += 1
        if len(sucurl) == pics_num:
            break
    print('\n' * 2 + '--------------------项目原图下载完毕')


# 脚本运行
print('\n'*3 + '--------------------项目网页解析中……')
html_bs = GetHTML(project_url)
path = Gettitl(html_bs)
imgs = Geturls(html_bs)
# 调用自定义函数'mkdir'创建项目文件夹
mkdir(path)
# 保存下载列表到本地
print('--------------------保存图片地址列表到url_list.txt文件')
txtpath = path + '\\' + 'url_list.txt'
txtfile = open(txtpath,'w')
txtfile.write('项目原图总数 ' + str(len(imgs)) + r' 张：' + '\n')
for i in imgs:
    txtfile.write(i+'\n')
txtfile.close()
# 开始下载项目原图
Download_imgs(imgs,path)