# 导入selenium
from selenium import webdriver
import time
# 从Config文件夹导入GetConfigData.py
from Config import GetConfigData
from Log import WriteLog

# 函数：登录功能
def LogIn(logPath,configdata):
    '''
    登录功能
    :return:登录句柄
    '''
    # 打开浏览器
    browser = webdriver.Firefox()
    # 放大窗口
    # browser.fullscreen_window()
    # 打开测试网址
    browser.get(configdata['WebUrl'])
    # 写日志
    WriteLog.WriteLog(logPath,"打开测试网址："+configdata['WebUrl'])
    # 等待
    browser.implicitly_wait(int(configdata['WaitTime']))
    # 输入用户名和密码登录
    username = browser.find_element_by_id('loginUser')
    password = browser.find_element_by_id('password')
    logbutton = browser.find_element_by_id('loginBtn')
    username.send_keys(configdata['UserAccount'])
    password.send_keys(configdata['Password'])
    logbutton.click()
    # 写日志
    WriteLog.WriteLog(logPath,"登录成功！账号信息："+configdata['UserAccount']+' '+configdata['Password'])
    # 等待
    browser.implicitly_wait(int(configdata['WaitTime']))
    # 选择医院登录
    hospital_id = 'button[cid="' + configdata['Hospital'] + '"]'
    # print(hospital_id)
    hospital = browser.find_element_by_css_selector(hospital_id)
    hospital.click()
    # 等待
    browser.implicitly_wait(int(configdata['WaitTime']))
    # 写日志
    WriteLog.WriteLog(logPath,"进入组织："+configdata['Hospital'])
    # 打开导航展示
    daohang = browser.find_element_by_css_selector('span[id="navbar-switch"]')
    daohang_class = daohang.get_attribute("class")
    # print(daohang_class)
    if daohang_class != "ivu-switch ivu-switch-checked ivu-switch-small":
        daohang.click()
    return browser
# 函数：退出登录
def LogOut(browser):
    '''
    退出登录
    :param hosptail:
    :return:
    '''
    #  等待10秒
    time.sleep(10)
    # 退出
    ele = browser.find_element_by_xpath('//div[@id="headerBarWrap"]/div[3]/div[1]/span[3]')
    ele.click()
    browser.implicitly_wait(30)
    ele = browser.find_element_by_link_text('退出')
    ele.click()
    browser.implicitly_wait(30)
    # 确定退出
    ele = browser.find_element_by_xpath('//div[@id="popConfirm"]/div/div[2]/button[2]')
    ele.click()
    return browser
# 测试函数功能
# 获取配置文件数据
# configdata = GetConfigData.GetConfigData('../Config/Config.txt')
# 打开浏览器
# b = LogIn(configdata)
# hospital = LogOut(b)
