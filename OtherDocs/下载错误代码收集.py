from urllib.request import urlretrieve
from urllib.request import urlopen

url = 'http://s.dgtle.com/portal/201612/03/193835a64qjd5z2wqmammj.jpg?szhdl=imageview/2/w/680'
url_1 = 'http://images.adsttc.com/media/images/5838/1661/e58e/ce93/1c00/0104/large_jpg/PORTADA_H_bg_Mitre_01.jpg?1480070746'
#urlretrieve(url,'2.jpg')

imgurl = urlopen(url_1)
imgfile = open('002.jpg','wb')
imgfile.write(imgurl.read())
imgfile.close()

print('下载测试完毕')