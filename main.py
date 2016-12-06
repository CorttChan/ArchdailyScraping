#! python3
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve

#输入Archdaily项目网址
url = input('请输入archdaily项目网址:')
usr_url = 'http://' + url

#临时测试网址
#usr_url = 'http://www.archdaily.com/796230/lobby-renovation-for-the-bank-of-slovenia-sadar-plus-vuga'
soup = BeautifulSoup(urlopen(usr_url).read(),'lxml')

#项目介绍描述文字抓取部分
#main_article = soup.article
#print (main_article)


#抓取项目所有图片缩略图片地址
pic_gallery = soup.findAll('a',class_="gallery-thumbs-link")
#ul_attrs = pic_gallery.attrs

#for link in pic_gallery:
    #pic_link = link.img['data-src']
    #print (type(pic_link))


#使用正则表达式替换缩略图片地址为原始分辨率图片地址


#按项目名称文件夹储层原始分辨率图片

# 定义显示下载文件进度函数
# 参考：http://www.aichengxu.com/view/4955140
def Schedule(a,b,c):
  per = 100.0*a*b/c
  if per > 100:
    pen = 100
  print ('%.2f%%' % per)

# 定义创建项目文件夹目录函数
# 参考：http://www.qttc.net/201209207.html
def mkdir(path):
    import os

    # 去除首位空格
     #path = path.strip()
    # 去除尾部 \ 符号
     #path = path.retrip('\\')

    # 判断路径是否存在
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

# 定义要创建的目录
# mkpath
# mkdir(mkpath)

project_name = soup.find('h1',{"class":"afd-title-big afd-title-big--bmargin-small afd-relativeposition"}).get_text()

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
#print (project_name)

downloadDir = 'C:\\Users\\CORTTCHAN\\Pictures\\Archdaily\\'
project_Dir = downloadDir + project_name
#print (project_Dir)

#调用自定义函数'mkdir'创建项目文件夹 
mkdir(project_Dir)

# 参考：http://www.cnblogs.com/mhxy13867806343/p/4153475.html
n = 0
for download in pic_gallery:
  n += 1
  pic_name = str(n)+'.jpg'
  pic_link = download.img['data-src'].replace('thumb_jpg','large_jpg')
  print (pic_link)
  filepath = os.path.join(project_Dir,pic_name)
  #print (filepath)
  urlretrieve (pic_link,filepath,Schedule)






#print (pic_gallery[0].img['data-src'])
#print (len(pic_gallery))

#for link in pic_gallery:
#    pic_link = link.get('data-src')
#    print (pic_link)
