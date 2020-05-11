from TestSuite.base_case import BaseCase
from Tools.decorator import screenshot
from Page.agent import Agent
import unittest

class Case50(BaseCase):

    retry = 0

    @screenshot
    def test(self):
        """测试创建代理商"""
        Agent(self.driver).click_dls()
        Agent(self.driver).create_dls()
        result = Agent(self.driver).check_dls()
        self.assertEqual("测试创建代理商", result, "创建代理商失败!  获取返回结果与预期不符")
