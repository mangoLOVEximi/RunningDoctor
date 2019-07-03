# 导入selenium
from selenium import webdriver
import time

# 函数：写日志
def WriteLog(logPath,logContent):
    '''
    写日志
    :return:
    '''
    # 获取当天日期
    currentData = time.strftime('%Y-%m-%d',time.localtime())
    # print(currentData)
    # 日志名称
    logtitle = 'Log_' + currentData + '.txt'
    # print(logtitle)
    # 打开文件
    file = open(logPath + logtitle,'a+')
    # 获取当前时间
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    # 写入日志时间
    file.write(currentTime)
    file.write(" ")
    #写入日志内容
    file.write(logContent)
    file.write("\n")
    # 关闭文件
    file.close()



# 测试函数
