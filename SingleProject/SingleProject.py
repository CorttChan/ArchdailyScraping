#!python3
#-*- coding：utf-8 -*-
# __author__ = 'CorttChan<cortt.me@gmail.com>'

import urllib.request
import time
import socket
from colorama import Fore,init
from bs4 import BeautifulSoup
from urllib.error import (HTTPError,URLError)

import deltmp
import auright
import Dimgs


init(autoreset=True)
# 版本声明
auright.pright()

# 定义获取项目网页函数'GetHTML'
def GetHTML(url):
    print('\n' * 2 + '--------------------项目网页解析中……')
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
        url = urllib.request.unquote(i,encoding='utf-8')             # 网址解码
        pics_url.append(url.split('?')[0])
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
    intab = '/\:*?"<>|'
    outtab = '---------'
    trantab = project_name.maketrans(intab, outtab)
    project_name = project_name.translate(trantab)
    downloadDir = '.\\Archdaily\\'
    project_Dir = downloadDir + project_name
    return project_Dir

# 定义图片url保存函数
def saveurls(list,path):
    # 保存下载列表到本地
    print('--------------------保存图片地址列表到url_list.txt文件')
    txtpath = path + '\\' + 'url_list.txt'
    txtfile = open(txtpath, 'w', encoding='utf-8')
    txtfile.write('项目原图总数 ' + str(len(list)) + r' 张：' + '\n')
    for i in list:
        txtfile.write(i + '\n')
    txtfile.close()

# 脚本运行
def main():
    while True:
        # 输入Archdaily项目网址
        project_url = input('--------------------请输入Archdaily项目网址:')
        # 检查网址合法性
        while 'www.archdaily.com' not in project_url:
            project_url= input('\n' + '--------------------网址错误，请重新输入正确网址：')

        html_bs = GetHTML(project_url)
        path = Gettitl(html_bs)
        imgs = Geturls(html_bs)
        # 调用自定义函数'mkdir'创建项目文件夹
        mkdir(path)
        # 保存下载列表到本地
        saveurls(imgs, path)
        # 开始下载项目原图
        Dimgs.Download(imgs, path)
        print('--------------------清理临时缓存中……')
        time.sleep(1)
        deltmp.DeleteTmp()

        #判断是否继续下载其他项目
        keepgoing = input('\n' + '--------------------继续下载其他项目? (-Y/N-): ')
        if keepgoing == 'Y' or keepgoing == 'y':
            continue
        else:
            print('\n' + Fore.RED + '--------------------程序即将退出……')
            for i in range(3):
                time.sleep(1)
                print(Fore.RED + '--------------------' + str(4-i))
            exit()

if __name__ == '__main__':
    main()
