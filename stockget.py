import datetime
import time
import urllib.request
import os  # this is "open" lib

debug=False

class Utility:
    def ToGB(str):
        if(debug): print(str)
        return str.decode('gb2312')

class StockInfo:
    """get stock information"""
    ##
    def GetStockStrByNum(num):
        f= urllib.request.urlopen('http://hq.sinajs.cn/list='+ str(num))
        if(debug) : print(f.geturl())
        if(debug) : print(f.info())
        return f.readline()
        f.close()    
                
    def ParseResultStr(resultstr):
        if(debug) : print(resultstr)
        slist=resultstr.split(',')
        name=slist[0][-4:]
        yesterdayendprice=slist[2]
        todaystartprice=slist[1]
        nowprice=slist[3]
        upgraderate=(float(nowprice)-float(yesterdayendprice))/float(yesterdayendprice)
        upgraderate= upgraderate * 100
        dateandtime=slist[30] + ' ' + slist[31]        
        print('*******************************')
        print('name is :',name)
        print('yesterday end price is :', yesterdayendprice)
        print('today start price is :', todaystartprice)
        print('now price is :', nowprice)
        print('upgrade rate is :', upgraderate,'%')
        print('date and time is :', dateandtime)
        print('*******************************')


        
        
    def GetStockInfo(num):
        str=StockInfo.GetStockStrByNum(num)
        strGB=Utility.ToGB(str)
        return strGB


def compare_time(start_t,end_t):

    s_time = time.mktime(time.strptime(start_t,'%Y%m%d%X')) # get the seconds for specify date

    e_time = time.mktime(time.strptime(end_t,'%Y%m%d%X'))
    if (s_time < e_time):
        return(0)
    else:
        return int(s_time-e_time)


class Mwrinter:
    def __init__(self, count,filepath):
        self.spc = ' '
        self.maxcolumn = count
        self.pointer = 0
        self.file = open(filepath,'a')
    def __dlt__(self):
        self.file.close()
    def wtit(self, x, z):
#######  x is for data to be printed ####
#######  Y is for format to be printed ####
#######  x is for wether line break ####
        #### want to print appendix way, use the keys word end=''####

        if z == 0:
            self.file.writelines(x)
        else:
          # self.file.writelines("\n")
            self.file.writelines(x)
    


def Main():
    count = 0
    file3 = 'D:\project\jd price\study\stock.txt'
    a = "2016081104:05:00"
    b = time.strftime('%Y%m%d%X', time.localtime())
    c = compare_time(a, b)
    print(c)
    print(" time to sleep is "   )
    time.sleep(c)
    p = Mwrinter(300,file3)
    p.wtit(time.strftime("%Y/%m/%d %X", time.localtime()),1)
    p.wtit("\n",1)   
    count = 0
    while (count < 2):
        print ( time.strftime("%Y/%m/%d %X", time.localtime()))
        count = count + 1
        time.sleep(0.5)
        stocks = ['sh600868', 'sz002448']
        
        for stock in stocks:
            p.wtit(StockInfo.GetStockInfo(stock),1)

    p.wtit(time.strftime("%Y/%m/%d %X", time.localtime()),1)     
    del(p)
    
Main()
print(time.time() )
print (time.localtime( time.time() ))
print (time.asctime( time.localtime(time.time()) ))

print ( time.strftime("%Y/%m/%d %X", time.localtime()))

""""""""""""""""""""""""""""""""""

新浪股票查询接口(1)
本系列目录：-文摘-
1. 新浪的股票查询接口：讲解了该接口的数据结构；
2. 新浪的股票查询接口（使用篇）：用一个简单的例子演示该接口的使用;
3. 实时股票信息查询：一个高级的例子，能够自动刷新股票信息，实现了实时更新；
以大秦铁路（股票代码：601006）为例，如果要获取它的最新行情，只需访问新浪的股票数据接口：http://hq.sinajs.cn/list=sh601006
这个url会返回一串文本，例如：

var hq_str_sh601006=“大 秦铁路, 27.55, 27.25, 26.91, 27.55, 26.20, 26.91, 26.92, 22114263, 589824680, 4695, 26.91, 57590, 26.90, 14700, 26.89, 14300, 26.88, 15100, 26.87, 3100, 26.92, 8900, 26.93, 14230, 26.94, 25150, 26.95, 15220, 26.96, 2008-01-11, 15:05:32“;

这个接口对于JavaScript程序非常方便，通常的使用方式为，静态或动态地在页面中插入：

<script type=“text/javascript“ src=“http://hq.sinajs.cn/list=sh601006“ charset=“gb2312“></script>

这样一来，你就可以在JS中用变量名“hq_str_sh601006”访问大秦铁路的行情数据了。下一篇文章用JavaScript代码演示了具体使用方法。

这个字符串由许多数据拼接在一起，不同含义的数据用逗号隔开了，按照程序员的思路，顺序号从0开始。
0：”大秦铁路”，股票名字；
1：”27.55″，今日开盘价；
2：”27.25″，昨日收盘价；
3：”26.91″，当前价格；
4：”27.55″，今日最高价；
5：”26.20″，今日最低价；
6：”26.91″，竞买价，即“买一”报价；
7：”26.92″，竞卖价，即“卖一”报价；
8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
10：”4695″，“买一”申请4695股，即47手；
11：”26.91″，“买一”报价；
12：”57590″，“买二”
13：”26.90″，“买二”
14：”14700″，“买三”
15：”26.89″，“买三”
16：”14300″，“买四”
17：”26.88″，“买四”
18：”15100″，“买五”
19：”26.87″，“买五”
20：”3100″，“卖一”申报3100股，即31手；
21：”26.92″，“卖一”报价
(22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况”
30：”2008-01-11″，日期；
31：”15:05:32″，时间；

如果你要同时查询多个股票，那么在URL最后加上一个逗号，再加上股票代码就可以了；比如你要一次查询大秦铁路（601006）和大同煤业（601001）的行情，就这样使用URL：
http://hq.sinajs.cn/list=sh601003,sh601001
返回的数据为：

var hq_str_sh601003=“柳 钢股份, 18.91, 18.80, 18.81, 19.10, 18.51, 18.80, 18.81, 5125000, 96017794, 9115, 18.80, 5100, 18.79, 12000, 18.78, 1800, 18.77, 2600, 18.76, 1500, 18.81, 25283, 18.82, 4470, 18.84, 3400, 18.85, 1600, 18.86, 2008-01-11, 15:05:32“;
var hq_str_sh601001=“大 同煤业, 40.00, 40.06, 39.81, 40.60, 39.13, 39.82, 39.83, 8117292, 324759633, 50, 39.82, 300, 39.81, 22809, 39.80, 1500, 39.79, 2600, 39.78, 600, 39.83, 10600, 39.85, 2100, 39.87, 2390, 39.88, 1000, 39.89, 2008-01-11, 15:05:32“;
但如果你要查询大盘指数，情况会有不同，比如查询上证综合指数（000001），使用如下URL：
http://hq.sinajs.cn/list=s_sh000001
返回的数据为：

var hq_str_s_sh000001=“上证指数,5484.677,28.136,0.52,877247,15587495“;

数据含义分别为：指数名称，当前点数，当前价格，涨跌率，成交量（手），成交额（万元）；

查询深圳成指的URL为：
http://hq.sinajs.cn/list=s_sz399001
数据构成方式与上证综合指数的数据相同。

最后说一下，新浪并没有明确提供这个查询API，所以他可以在不通知任何人的情况下，改变这种查询方式的接口和实现。

**************************************
rU 或 Ua 以读方式打开, 同时提供通用换行符支持 (PEP 278)
w     以写方式打开，
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb     以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+    以二进制读写模式打开 (参见 r+ )
wb+    以二进制读写模式打开 (参见 w+ )
ab+    以二进制读写模式打开 (参见 a+ )

"""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""
 在python中，使用unicode类型作为编码的基础类型。即

     decode              encode

str ---------> unicode --------->str

u = u'中文' #显示指定unicode类型对象u
str = u.encode('gb2312') #以gb2312编码对unicode对像进行编码
str1 = u.encode('gbk') #以gbk编码对unicode对像进行编码
str2 = u.encode('utf-8') #以utf-8编码对unicode对像进行编码
u1 = str.decode('gb2312')#以gb2312编码对字符串str进行解码，以获取unicode
u2 = str.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型


""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""


