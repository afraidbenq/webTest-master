from .base import Base, Location
from Tools.web_tool import Tools
import time


class Index(Base):
    loginbtn = Location("登陆按钮", 'button[type=submit]')
    # menu = Location("大后台左侧菜单", ".menuItem")
    # seperate = Location("展开菜单的按钮", '//*[@id="root"]/div/section/header/div[1]/i', "XPATH")
    admin = Location("系统管理员", '//*[@id="root"]/div/section/header/div[2]/span[2]', "XPATH")
    logout = Location("退出登录", '[class=ant-dropdown-menu-item]')

    seperate = Location("展开菜单的按钮", 'i.anticon.anticon-menu-fold.trigger')
    sjtj = Location("数据统计", '//*[@id="layout-container"]/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]', "XPATH")
    dyfx = Location("数据统计", '//*[@id="layout-container"]/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]', "XPATH")
    cabimg = Location("地域分析内机柜图标",
                      '//*[@id="layout-container"]/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div[27]/div/div/div/img',
                      "XPATH")

    def touch_menu(self):
        time.sleep(3)
        self.driver.click(self.admin)
        time.sleep(3)
        self.driver.click(self.logout)
        time.sleep(3)
        # self.driver.click(self.seperate)
        # time.sleep(3)
        # self.driver.click(self.seperate)
        # time.sleep(3)
        # self.driver.click(self.dyfx)

    def check(self):
        time.sleep(3)
        self.driver.move(self.loginbtn)
        r = self.driver.exists(self.loginbtn)
        return r
    # search = Location("搜索按钮", "#sb_form_go")
    # search_input = Location("搜索内容输入框", "#sb_form_q")

    # def search_dragonball_super(self):
    #     self.driver.send(self.search_input, "龙珠超")
    #     self.driver.click(self.search)

    # def close_menu(self):
    #     if self.driver.exists(self.seperate):
    #         self.driver.click(self.seperate)
    #
    # def select_menu(self, menu):
    #     menu_list = Tools.trans_menu(menu)
    #     self.close_menu()                   # 需要先关闭菜单, 但是需要等待菜单折叠起来
    #     for n in menu_list:
    #         self.driver.click_text(self.menu, n)
