import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.error import (
    HTTPError,
    URLError,
    ContentTooShortError
    )

url = 'http://www.archdaily.cn/cn/800402/su-li-shi-bei-mei-zong-bu-da-lou-goettsch-partners'

html = urlopen(url)
bsobj = BeautifulSoup(html.read(),'lxml')


# //获取项目名称：
project_name = bsobj.find('h1',{"class":"afd-title-big afd-title-big--bmargin-small afd-relativeposition"}).get_text()
# 去除项目名称中的特殊字符
  # 去除首位空格
project_name = project_name.strip()
  # 去除特殊字符
  # 参考：http://www.runoob.com/python/att-string-translate.html
#from string import maketrans
intab = ' /+'
outtab = '___'
trantab = project_name.maketrans(intab,outtab)
project_name = project_name.translate(trantab)
print(project_name)


# //定义显示下载文件进度函数
# 参考：http://www.aichengxu.com/view/4955140
def Schedule(a,b,c):
  per = 100.0*a*b/c
  if per > 100:
    pen = 100
  print ('%.2f%%' % per)


# //定义创建项目文件夹目录函数
# 参考：http://www.qttc.net/201209207.html
def mkdir(path):
    import os
    # 存在    True
    # 不存在  False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print (path+'目录创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+'目录已存在')
        return False

# 创建项目下载文件夹
downloadDir = r'C:\Users\CORTTCHAN\Pictures\Archdaily\\'
project_Dir = downloadDir + project_name
print(project_Dir)
#调用自定义函数'mkdir'创建项目文件夹
mkdir(project_Dir)

# // 项目图片下载
# 参考：http://www.cnblogs.com/mhxy13867806343/p/4153475.html



pic_gallery = bsobj.findAll('a',class_="gallery-thumbs-link")
n = 0
for download in pic_gallery:
  n += 1
  pic_name = str(n)+'.jpg'
  pic_link = download.img['data-src'].replace('thumb_jpg','large_jpg')
  print (pic_link)
  filepath = os.path.join(project_Dir,pic_name)
  #print (filepath)
  urlretrieve (pic_link,filepath,Schedule)

def imgdownload(url):
    try:
        urlretrieve(url,filepath,Schedule())
    except