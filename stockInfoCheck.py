
'''
Created on 2020/1/31

StockInfoCheck by Python 3.8.1

@author: Meng

'''

import requests

def tradeInfo():

    link = 'http://qt.gtimg.cn/q=' + stockCode
    content=requests.get(link).text
    list = content.split('~')
    
    infoData = (list[1] ,
                list[2] ,
                list[3] ,
                list[31] ,
                list[32] ,
                list[36] ,
                list[37] ,
                list[38] ,
                list[43] ,
                list[39])

    infoType = ('股票名称：' ,
                '股票代码：' ,
                '当前价格/元：' ,
                '当前涨跌/元：' ,
                '当前涨跌/%：' ,
                '成交量/手：' ,
                '成交额/万：' ,
                '换手率/%：' ,
                '振幅/%：' ,
                '市盈率：')

    for num in range(len(infoType)):
        print(infoType[num] + infoData[num])
        
def moneyFlow():

    link = 'http://qt.gtimg.cn/q=ff_' + stockCode
    content=requests.get(link).text
    list = content.split('~')

    flowType = ('主力流入/万：' ,
                '主力流出/万：' ,
                '主力净流入/万：' ,
                '主力净流入占比/%：' ,
                '散户流入/万：' ,
                '散户流出/万：' ,
                '散户净流入/万：' ,
                '散户净流入占比/%：')

    for num in range(len(flowType)):
        print(flowType[num] + list[num+1])
                
def codeCheck(stockCode):

    if len(stockCode) == 4:
        stockCode = 'sz00' + stockCode
    elif int(stockCode) >= 600000:
        stockCode = 'sh' + stockCode
    else:stockCode = 'sz' + stockCode
    return(stockCode)

print('欢迎查询股票信息！')
print('请输入股票代码：')

stockCode = input()

stockCode = codeCheck(stockCode)
tradeInfo()
moneyFlow()
