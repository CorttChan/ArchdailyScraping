#!python3
#-*- coding：utf-8 -*-
# __author__ = 'CorttChan<cortt.me@gmail.com>'

import urllib.request
import time
from colorama import Fore,init

import arss
import shtml
import deltmp
import auright
import Dimgs

# 版本声明
auright.pright()

init(autoreset=True)
# 初始化待爬取项目url
raw_url = []

# 获取rss更新
rssurl = arss.getrsspros()
# 读取已爬取项目url
f = open('proceurl.txt',encoding='utf-8')
original_rss = f.readlines()
f.close()
pro_rss = []
for i in original_rss:
    pro_rss.append(i.rstrip('\n'))
# 检查更新的rss是否已下载过，如果没有就添加到待爬取列表中
for i in rssurl:
    if i not in pro_rss:
        raw_url.append(i)

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
    print('--------------------开始创建项目文件夹:')
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print('\n' + '--------------------项目文件夹创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print('\n' + '--------------------项目文件夹已创建')
        return False

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

def main(raw_url):
    print('\n'+Fore.GREEN+'--------------------待下载项目数： **' + str(len(raw_url)) + '**')
    # 初始化计数器
    n = 1
    for i in raw_url:
        # url = str(i)
        print('\n'*2+Fore.GREEN+'--------------------开始下载第：**' + str(n) + '** 个项目')
        # 导入待下载url列表
        html_bs = shtml.GetHTML(i)
        path = Gettitl(html_bs)
        imgs = Geturls(html_bs)
        # 调用自定义函数'mkdir'创建项目文件夹
        mkdir(path)
        # 保存下载列表到本地
        saveurls(imgs, path)
        # 开始下载项目原图
        Dimgs.Download(imgs, path)
        print('\n'+Fore.YELLOW+r'_ _ _ _ _ _ _ _ _ _ _ _ _ _ 分 _ _ _(:з」∠)_ _ _ 割 _ _ _(:з」∠)_ _ _君 _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
        n += 1
        # 将完成下载的项目url添加入procerul.txt文件归档
        f = open('proceurl.txt', 'a', encoding='utf-8')
        f.write('\n' + i)
        f.close()
    print('\n'+Fore.GREEN+'--------------------所有项目已完成下载')
    # 清理临时缓存
    print('\n'+Fore.GREEN+'--------------------开始清理临时缓存……')
    time.sleep(1)
    deltmp.DeleteTmp()

    print('\n' + Fore.RED + '--------------------程序即将退出……')
    for i in range(3):
        time.sleep(1)
        print(Fore.RED + '--------------------' + str(4 - i) + '***')
    exit()



if __name__ == '__main__':
    main(raw_url)