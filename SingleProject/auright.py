#!python3
#-*- coding：utf-8 -*-
# __author__ = 'CorttChan<cortt.me@gmail.com>'

from colorama import Fore,init

# 版本声明
def pright():
    init(autoreset=True)
    print('\n')
    author_str = (
    '   ****** SingleProject',
    '   ****** Version: 1.1',
    '   ****** Discription: AchdailyPicsDownload',
    '   ****** Author: CorttChan<cortt.me@gmail.com>'
    )
    for n in author_str:
        print(Fore.CYAN + n)
    print('\n')

if __name__ == '__main__':
    pright()

