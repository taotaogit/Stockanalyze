import datetime
import time
import urllib.request
import os
import json
import sys

def ToGB(str ):
        return str.encode('gb2312')

def main ():
    #encoding=utf-8
    
    file3 = 'D:\project\jd price\study\stock.txt'
    fh = open('D:\project\jd price\study\stock.txt')
    print(fh.readline())
    print(fh.readline())
    a=json.dumps(fh.readline(),ensure_ascii=False,separators=(',', ': '))
    print (a[6])
 
main()



