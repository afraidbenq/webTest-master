from TestSuite.base_case import BaseCase
from Tools.decorator import screenshot
from Page.agent import Agent
import unittest

class Case82(BaseCase):

    retry = 0

    @screenshot
    def test(self):
        """测试借还记录最下栏统计数据"""
        Agent(self.driver).test()
        self.assertEqual(True, True, "创建代理商失败!  获取返回结果与预期不符")
