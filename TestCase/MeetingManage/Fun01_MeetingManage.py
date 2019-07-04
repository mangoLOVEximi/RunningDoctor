from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

# 找到当前文件Fun01_MeetingManage.py的路径
current_directory = os.path.abspath(os.path.dirname('Fun01_MeetingManage.py'))
print('current_directory:' + current_directory)
# 找到项目的根文件路径
parent_path = os.path.split(current_directory)[0]
root_path = os.path.split(parent_path)[0]
print('root_path:' + root_path)
# 把根目录追加为执行时的环境变量
sys.path.append(root_path)

from Config.GetConfigData import *
from Log.WriteLog import *
from Util.LogSystem import *

# 打开浏览器登录
def OpenBrowser(configdata):
    '''
    打开浏览器，登录成功
    :return:
    '''
    browser = LogIn('../../Log/',configdata)
    return browser

def LoadUrl(browser):
    '''
    打开功能网页
    :return:
    '''
    # 打开会议预定功能
    ele = browser.find_element_by_css_selector('li[data-appid="59dca0bf61bf3438ea035dbf"]')
    ele.click()
    # 切换到会议管理框架
    # iframe = browser.find_element_by_id('iframeExport')
    # browser.switch_to.frame(iframe)
    # 打开会议室管理子菜单页面
    ele = browser.find_element_by_xpath('/html/body/div[6]/div[8]/div[19]/div/div/div/div[1]/div[2]/ul/li[6]')
    ele.click()
    return browser

def FindElement():
    '''
    定位元素
    :return:
    '''

def SendVals(vals):
    '''
    构造发送参数
    :return:
    '''
    # 获取当天日期
    currentData = time.strftime('%Y-%m-%d', time.localtime())
    # 构造参数
    vals = vals + currentData
    return vals

def CheckResult():
    '''
    检查结果
    :return:
    '''

def MeetingManage_TestCase001(browser):
    '''
    测试用例：添加会议室
    :return:
    '''
    # 添加会议室
    MeetingAdd = browser.find_element_by_css_selector('button[id="add_room_btn"]')
    MeetingAdd.click()
    # 输入会议室信息
    # 会议室名称
    MeetingName_xpath = '/html/body/div[6]/div[8]/div[19]/div/div/div/div[3]/div[2]/div[1]/div/div/input'
    MeetingName = browser.find_element_by_xpath(MeetingName_xpath)
    MeetingName_vals = SendVals('会议室名称')
    MeetingName.send_keys(MeetingName_vals)
    # 会议室类型
    MeetingType_xpath = '/html/body/div[6]/div[8]/div[19]/div/div/div/div[3]/div[2]/div[2]/div/div/input'
    MeetingType = browser.find_element_by_xpath(MeetingType_xpath)
    MeetingType_vals = SendVals('会议室类型')
    MeetingType.send_keys(MeetingType_vals)
    # 会议室人数
    MeetingNum_xpath = '/html/body/div[6]/div[8]/div[19]/div/div/div/div[3]/div[2]/div[3]/div/div/input'
    MeetingNum = browser.find_element_by_xpath(MeetingNum_xpath)
    MeetingNum.send_keys(100)
    # 会议室地址
    MeetingAddr_xpath = '/html/body/div[6]/div[8]/div[19]/div/div/div/div[3]/div[2]/div[4]/div/div/input'
    MeetingAddr = browser.find_element_by_xpath(MeetingAddr_xpath)
    MeetingAddr_vals = SendVals('会议室地址')
    MeetingAddr.send_keys(MeetingAddr_vals)
    # 会议室描述
    MeetingDescribe_xpath = '/html/body/div[6]/div[8]/div[19]/div/div/div/div[3]/div[2]/div[5]/div/div/textarea'
    MeetingDescribe = browser.find_element_by_xpath(MeetingDescribe_xpath)
    MeetingDescribe_vals = SendVals('会议室描述')
    MeetingDescribe.send_keys(MeetingDescribe_vals)
    # 会议室注意事项
    MeetingNotice_xpath = '/html/body/div[6]/div[8]/div[19]/div/div/div/div[3]/div[2]/div[6]/div/div/textarea'
    MeetingNotice = browser.find_element_by_xpath(MeetingNotice_xpath)
    MeetingNotice_vals = SendVals('会议室注意事项')
    MeetingNotice.send_keys(MeetingNotice_vals)
    # 选择会议室管理员
    MeetingManage_xpath = '/html/body/div[6]/div[8]/div[19]/div/div/div/div[3]/div[2]/div[7]/div/div/input'
    MeetingManage = browser.find_element_by_xpath(MeetingManage_xpath)
    browser.execute_script("arguments[0].click();",MeetingManage)
    MeetingManageChoice_xpath = '/html/body/div[34]/div/div/div/div/div[2]/div[1]/div[1]/input'
    MeetingManageChoice = browser.find_element_by_xpath(MeetingManageChoice_xpath)
    MeetingManageChoice.send_keys('唐莉')
    MeetingManageChoice1_xpath = ''
    MeetingManageChoice1 = browser.find_element_by_xpath('//div[@id="chosePersonBoxModal"]/div/div/div[2]/div/div/ul/li[@uid="55cee726e419beae7c8b45f8"]')
    browser.execute_script("arguments[0].click();", MeetingManageChoice1)
    MeetingManageChoice2_xpath = '/html/body/div[34]/div/div/div/div/div[3]/button[2]'
    MeetingManageChoice2 = browser.find_element_by_xpath('//div[@id="chosePersonBoxModal"]/div/div/div[3]/button[2]')
    browser.execute_script("arguments[0].click();", MeetingManageChoice2)
    # 设置打卡地点
    MeetingCardAddr_xpath = '/html/body/div[6]/div[8]/div[19]/div/div/div/div[3]/div[2]/div[8]/div/div/input'
    MeetingCardAddr = browser.find_element_by_xpath(MeetingCardAddr_xpath)
    browser.execute_script("arguments[0].click();", MeetingCardAddr)
    MeetingCardAddr1 =browser.find_element_by_css_selector('input[id="attendAdminSetLocSearch"]')
    MeetingCardAddr1.send_keys('天府新谷10号楼')
    # MeetingCardAddr1.send_keys(Keys.ENTER)
    browser.implicitly_wait(configdata['WaitTime'])
    MeetingCardAddr2_xpath = '/html/body/div[34]/div/div/div/div/div[2]/div[1]/ul/li[1]'
    MeetingCardAddr2 = browser.find_element_by_xpath(MeetingCardAddr2_xpath)
    browser.execute_script("arguments[0].click();", MeetingCardAddr2)
    MeetingCardAddr3 = browser.find_element_by_css_selector('button[id="confirmSelectLoc"]')
    browser.execute_script("arguments[0].click();", MeetingCardAddr3)
    # 设置打开范围
    MeetingCardScope_xpath = '/html/body/div[6]/div[8]/div[19]/div/div/div/div[3]/div[2]/div[9]/div/div/input'
    MeetingCardScope = browser.find_element_by_xpath(MeetingCardScope_xpath)
    MeetingCardScope.send_keys('100')
    # 提交内容
    MeetingSubmit_xpath = '/html/body/div[6]/div[8]/div[19]/div/div/div/div[3]/div[3]/button[2]/span'
    MeetingSubmit = browser.find_element_by_xpath(MeetingSubmit_xpath)
    browser.execute_script("arguments[0].click();", MeetingSubmit)

# -----测试用例运行-----
logContent = '----------会议室预定：会议室管理功能----------'
WriteLog.WriteLog('../../Log/',logContent)
# 获取配置文件数据
WriteLog.WriteLog('../../Log/','读取配置文件')
configdata = GetConfigData.GetConfigData('../../Config/Config.txt')
# 打开浏览器
browser = OpenBrowser(configdata)
WriteLog.WriteLog('../../Log/','打开网址登陆成功')
# 打开功能网页
browser = LoadUrl(browser)
WriteLog.WriteLog('../../Log/','打开会议室管理功能成功')
# 运行测试用例
WriteLog.WriteLog('../../Log/','###MeetingManage_TestCase001：添加会议室')
MeetingManage_TestCase001(browser)
WriteLog.WriteLog('../../Log/','###MeetingManage_TestCase001：添加会议室,运行成功！')
WriteLog.WriteLog('../../Log/','###MeetingManage_TestCase002：编辑会议室')

# 退出
# WriteLog.WriteLog('../../Log','退出登录')
# browser = LogSystem.LogOut(browser)
# 关闭浏览器
# browser.quit()
