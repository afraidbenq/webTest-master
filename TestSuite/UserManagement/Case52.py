from TestSuite.base_case import BaseCase
from Tools.decorator import screenshot
from Page.agent import Agent
import unittest

class Case52(BaseCase):

    retry = 0

    @screenshot
    def test(self):
        """测试代理商批量设置直属上级"""
        Agent(self.driver).test()
        self.assertEqual(True, True, "创建代理商失败!  获取返回结果与预期不符")
