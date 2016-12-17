#!python3
#-*- coding：utf-8 -*-
# __author__ = 'CorttChan<cortt.me@gmail.com>'


import os
from colorama import Fore,init

init(autoreset=True)
def DeleteTmp():
    for n in os.listdir():
        if n.endswith('.tmp'):
            os.unlink(n)
    print(Fore.GREEN+'--------------------临时缓存清理完毕')

if __name__ == '__main__':
    DeleteTmp()