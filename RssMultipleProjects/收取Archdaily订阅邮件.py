import imapclient
imapObj = imapclient.IMAPClient('mail.cortt.me', ssl=False)
imapObj.login('archdaily_rss@cortt.me','Rss@123456')
imapObj.select_folder('INBOX',readonly=True)
UIDs = imapObj.search('UNSEEN')
print(UIDs)
rawMessage = imapObj.fetch(UIDs,['BODY[]'])
#import pprint
#pprint.pprint(rawMessage)

import imaplib
imaplib._MAXLINE = 1000000

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[3][b'BODY[]'])

from bs4 import BeautifulSoup

# 获取订阅邮件正文并解析为bs4对象/
if message.html_part != None:
    html_str = message.html_part.get_payload().decode(message.html_part.charset)
    bsObj = BeautifulSoup(html_str, 'lxml')

# 提取项目链接URL
url_ori = bsObj.find_all('tbody')
print(url_ori[-2])


# 利用正则表达式提取项目url
#import re
