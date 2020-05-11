from .base import Base, Location
from Tools.web_tool import Tools
import time
from Tools.win32Key import KeyboardKeys
from Tools.win32Model import Clipboard
import random


class Agent(Base):
    yhgl = Location("用户管理", '//*[@id="root"]/div/section/section/aside/div/ul/li[3]/div/span/span', "XPATH")
    dls = Location("代理商", '//*[@id="userManagement$Menu"]/li[1]/a', "XPATH")
    cjdls = Location("创建代理商", '//*[@id="layout-container"]/div/div[1]/div/div[2]/div[1]/div[1]/button[1]', "XPATH")
    plsc = Location("批量删除", '//*[@id="layout-container"]/div/div/div/div[2]/div[1]/div[1]/button[2]', "XPATH")
    plszzssj = Location("批量设置直属上级", '//*[@id="layout-container"]/div/div/div/div[2]/div[1]/div[1]/button[3]',
                        "XPATH")
    plszjslx = Location("批量设置角色类型", '//*[@id="layout-container"]/div/div/div/div[2]/div[1]/div[1]/button[4]',
                        "XPATH")
    szdlssy = Location("设置代理商收益", '//*[@id="layout-container"]/div/div/div/div[2]/div[1]/div[1]/button[5]',
                       "XPATH")
    cx = Location("查询", '//*[@id="layout-container"]/div/div/div/div[2]/div[1]/div[2]/button[1]', "XPATH")
    czsytj = Location("重置所有条件", '//*[@id="layout-container"]/div/div/div/div[2]/div[1]/div[2]/button[2]', "XPATH")
    zdylb = Location("自定义列表", '//*[@id="layout-container"]/div/div/div/div[2]/div[1]/div[2]/div/button', "XPATH")
    qx = Location("全选",
                  '//*[@id="layout-container"]/div/div/div/div[2]/div[2]/div/div/div/div/div/table/thead/tr/th[1]/span/div/span[1]/div/label/span',
                  "XPATH")
    dlssx = Location("代理商筛选",
                     '//*[@id="layout-container"]/div/div/div/div[2]/div[2]/div/div/div/div/div/table/thead/tr/th[2]/i',
                     "XPATH")

    qsrssnr1 = Location('请输入搜索内容', "input.ant-input")
    queding = Location('确定', "button.ant-btn ant-btn-primary")

    uploadpic = Location("上传图片按钮", '//*[@id="base64ImgInput"]/span[2]/div/span/button', "XPATH")

    tupian = Location('图片', "div.ant-modal-body>div>div:nth-child(1)>img")

    cjtpqr = Location('裁剪图片确认', "div.ant-modal-footer>div>button.ant-btn.ant-btn-primary")

    path = "C:\\Users\\32918\\Desktop\\20000494.png"
    xzzssj = Location('选择直属上级',
                      '//*[@id="layout-container"]/div/div[2]/div/div/div[2]/div[3]/div[1]/div/form/div[2]/div[2]/div/span/span/button',
                      'XPATH')
    dlsmcsx = Location('代理商名称筛选',
                       '//*[@id="layout-container"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[1]/table/thead/tr/th[2]/i',
                       'XPATH')
    qsrssnr = Location('请输入搜索内容',
                       '//*[@id="layout-container"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/input',
                       "XPATH")
    qd = Location('确定',
                  '//*[@id="layout-container"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/button[2]',
                  "XPATH")
    dx = Location('点选代理商',
                  '//*[@id="layout-container"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[2]/table/tbody/tr/td[1]/span/label/span',
                  'XPATH')
    dj = Location('点选角色类',
                  '//*[@id="layout-container"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span',
                  'XPATH')
    bangding = Location('绑定', '//*[@id="layout-container"]/div/div[2]/div[1]/div[2]/div[3]/div/button[1]', 'XPATH')
    zhikong = Location('置空', '//*[@id="layout-container"]/div/div[2]/div[1]/div[2]/div[3]/div/button[2]', 'XPATH')
    quxiao = Location('取消', '//*[@id="layout-container"]/div/div[2]/div[1]/div[2]/div[3]/div/button[3]', "XPATH")
    xzjslx = Location('选择角色类型',
                      '//*[@id="layout-container"]/div/div[2]/div/div/div[2]/div[3]/div[1]/div/form/div[3]/div[2]/div/span/span/button',
                      "XPATH")
    dlsmc = Location('代理商名称', 'input[id=name]')
    dlslxr = Location('代理商联系人', 'input#contacts')
    dlsdh = Location('代理商电话', 'input#phone')
    bzxx = Location('备注信息', 'textarea#remarks')
    xyb = Location('下一步',
                   '//*[@id="layout-container"]/div/div[2]/div/div/div[2]/div[3]/div[1]/div/form/div[8]/div/div/span/button[1]',
                   "XPATH")
    fh = Location('返回',
                  '//*[@id="layout-container"]/div/div[2]/div/div/div[2]/div[3]/div[1]/div/form/div[8]/div/div/span/button[2]',
                  "XPATH")
    szdq = Location('所在地区', '//*[@id="area"]', "XPATH")
    zgdl = Location('中国大陆', 'div#53725134-5936-41ab-f76f-726a65f0fe66>ul>li.ant-select-dropdown-menu-item')
    szgj = Location('所在国家', '//*[@id="country"]', "XPATH")
    zg = Location('中国', '//*[@id="country"]/div/div/div[2]', 'XPATH')
    szss = Location('所在省市', '//*[@id="province"]', 'XPATH')
    beijing = Location('北京市', '//*[@id="province"]/div/div/div[2]', "XPATH")
    szcs = Location('所在城市', '//*[@id="city"]', 'XPATH')
    dcq = Location('东城区', '//*[@id="city"]/div/div/div[2]', "XPATH")
    szqx = Location('所在区县', '//*[@id="district"]', 'XPATH')
    jddz = Location('街道地址', '//*[@id="address"]', "XPATH")
    syb = Location('上一步',
                   '//*[@id="layout-container"]/div/div[2]/div/div/div[2]/div[3]/div[2]/div/form/div[6]/div/div/span/button[1]',
                   "XPATH")
    wzxxxyb = Location('下一步',
                       '//*[@id="layout-container"]/div/div[2]/div/div/div[2]/div[3]/div[2]/div/form/div[6]/div/div/span/button[2]',
                       "XPATH")
    wzxxfh = Location('返回',
                      '//*[@id="layout-container"]/div/div[2]/div/div/div[2]/div[3]/div[2]/div/form/div[6]/div/div/span/button[3]',
                      'XPATH')
    dlm = Location('登录名', '//*[@id="loginName"]', "XPATH")
    mima = Location('登录密码', '//*[@id="password"]', "XPATH")
    qrmm = Location('确认密码', '//*[@id="confirm"]', "XPATH")
    dlxxsyb = Location('上一步',
                       '//*[@id="layout-container"]/div/div[2]/div/div/div[2]/div[3]/div[3]/div/form/div[4]/div/div/span/button[1]',
                       "XPATH")
    cjdlsbtn = Location('创建代理商',
                        '//*[@id="layout-container"]/div/div[2]/div/div/div[2]/div[3]/div[3]/div/form/div[4]/div/div/span/button[2]',
                        "XPATH")
    dlxxfh = Location('返回',
                      '//*[@id="layout-container"]/div/div[2]/div/div/div[2]/div[3]/div[3]/div/form/div[4]/div/div/span/button[3]',
                      "XPATH")

    def opendls(self):
        self.driver.click(self.yhgl)
        self.driver.click(self.dls)

    def upload(self, path):
        Clipboard.setText(path)
        time.sleep(1)
        KeyboardKeys.twoKeys('ctrl', 'v')
        KeyboardKeys.oneKey('enter')  # 模拟回车

    def click_dls(self):

        self.driver.click(self.yhgl)
        while True:
            time.sleep(2)
            if self.driver.exists(self.dls):
                self.driver.click(self.dls)
                break
            else:
                self.driver.click(self.yhgl)

    def create_dls(self):
        self.driver.click(self.cjdls)
        self.driver.click(self.uploadpic)
        self.upload(self.path)
        time.sleep(2)
        print(self.driver.bounds(self.tupian))
        self.driver.click(self.cjtpqr)
        self.driver.click(self.xzzssj)
        self.driver.click(self.dlsmcsx)
        self.driver.send(self.qsrssnr, '广州')
        self.driver.click(self.qd)
        self.driver.click(self.dx)
        self.driver.click(self.zhikong)
        self.driver.click(self.dx)
        self.driver.click(self.bangding)
        self.driver.click(self.xzjslx)
        self.driver.click(self.dj)
        self.driver.click(self.zhikong)
        self.driver.click(self.dj)
        self.driver.click(self.bangding)
        self.driver.send(self.dlsmc, '测试创建代理商')
        self.driver.send(self.dlslxr, '卢俊杰')
        self.driver.send(self.dlsdh, '13823417742')
        self.driver.send(self.bzxx, '备注')
        self.driver.click(self.xyb)
        self.driver.click(self.szdq)
        KeyboardKeys.oneKey('down')
        KeyboardKeys.oneKey('enter')
        self.driver.click(self.szgj)
        KeyboardKeys.oneKey('enter')
        self.driver.click(self.szss)
        KeyboardKeys.oneKey('enter')
        self.driver.click(self.szcs)
        KeyboardKeys.oneKey('enter')
        self.driver.click(self.szqx)
        KeyboardKeys.oneKey('enter')
        self.driver.send(self.jddz, '街道地址')
        self.driver.click(self.wzxxxyb)
        self.driver.send(self.dlm, ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 6)))
        self.driver.send(self.mima, '123456')
        self.driver.send(self.qrmm, '123456')
        self.driver.click(self.cjdlsbtn)
        time.sleep(10)

    def check_dls(self):
        self.driver.click(self.dlssx)
        Clipboard.setText('测试创建代理商')
        KeyboardKeys.twoKeys('ctrl', 'v')
        self.driver.click(self.cx)
        result = '测试创建代理商'
        time.sleep(3)
        return result

    def test(self):
        pass
