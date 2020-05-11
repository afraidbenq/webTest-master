from Tools.decorator import Log
from Tools.driver import ChromeDriver
from Tools.logger import Logger
from config import Config
from .base import Base, Location


class Login(object):
    logger = Logger().logger
    driver = None
    username = Location("用户名输入框", "input[type=text]")
    passwd = Location("密码输入框", "input[type=password]")
    submit = Location("登录按钮", "button[type=submit]")
    img = Location("后台管理系统果壳logo", '//*[@id="root"]/div/section/header/div[1]/div/span[1]/img', "XPATH")

    def __init__(self):
        # 启动driver
        try:
            self.driver = ChromeDriver()
            self.driver.maximize_window()
            self.driver.get(Config.url)
            self.driver.set_page_load_timeout(Config.TIMEOUT)
            self.driver.set_script_timeout(10)
        except Exception as e:
            Log.error("driver初始化失败....\n系统信息: {} \n浏览器类型: {}\n详细信息: {}".format(
                Config.system, Config.BROWSER, str(e)))
            if self.driver:
                self.driver.quit()
            raise Exception(e)

    def login(self):
        # 屏蔽登录部分
        self.driver.send(self.username, Config.USER)
        self.driver.send(self.passwd, Config.PWD)
        self.driver.click(self.submit)
        assert self.driver.exists(self.img), "登录失败, 未找到大后台左上角logo"
        assert self.driver.title == "GOOCKR CHARGING", \
            "打开GOOCKR CHARGING失败, 浏览器title不为'GOOCKR CHARGING'，可能未进入GOOCKR CHARGING首页"
        return self.driver
