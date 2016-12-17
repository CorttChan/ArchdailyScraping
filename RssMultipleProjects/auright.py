#!python3
#-*- coding：utf-8 -*-
# __author__ = 'CorttChan<cortt.me@gmail.com>'

from colorama import Fore,init

# 版本声明
def pright():
    init(autoreset=True)
    print('\n')
    author_str = (
    '   ****** MultiProject',
    '   ****** Version: 2.0',
    '   ****** Discription: Achdaily_RSS_PicsDownload',
    '   ****** Author: CorttChan <cortt.me@gmail.com>',
    '                  LemonLv <lvjing.me@gmail.com>',
    '   ****** Published: 12/01/2016'
    )
    for n in author_str:
        print(Fore.CYAN + n)
    print('\n')

if __name__ == '__main__':
    pright()

