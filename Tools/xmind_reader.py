import re
import xmind
from config import Config
import os
from collections import defaultdict


class Xmind(object):

    def __init__(self, filename):
        # 传入xmind文件
        filepath = os.path.join(Config.xmind, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError("在Xmind目录中未找到文件{}".format(filename))
        self.reader = xmind.load(filepath)

    def get_son(self, node):
        try:
            son = node.getSubTopics()
            # print('getson', son)

            return None if len(son) == 0 else son
        except:

            return None

    def parse(self):
        total = []
        sheets = self.reader.getSheets()  # 获取xmind文件里的画布数量

        for sheet in sheets:  # 逐个画布解析测试用例
            suite = sheet.getTitle()  # 获取画布名称，这将作为TestSuite里的文件夹名称（通常用模块名称代替例如UserManagement）
            root = sheet.getRootTopic()
            case_name = root.getTitle()  # 获取画布内的中心主题名称，这将作为TestSuite里的模块文件夹里的测试用例py文件名称（通常用CaseID代替例如Case50）
            print(case_name)
            rt = dict(times=0, skip=False, name=case_name, suite=suite)  # 测试用例信息记入字典
            for node in root.getSubTopics():  # 获取中心主题下所有子主题（描述、页面、跳过、步骤、重跑次数）
                rt.update(self.get_info(node))  # 获取子主题下信息，并更新/添加到测试用例信息
            total.append(rt)
        # print(total)
        return total

    def get_info(self, node):
        if node.getTitle() == "页面":
            page_list = []
            for page in node.getSubTopics():  # 获取页面下子主题数量，逐个page解析
                mds, vals = [], []
                pg_name = page.getTitle()  # 获取page的页面的标题
                methods = self.get_son(page)  # 获取page下的方法
                # print('methods数', methods)
                if methods is not None:

                    for md in methods:  # 逐个方法解析获取值
                        value = self.get_son(md)  # 获取方法下是否有值

                        vals.append(value[0].getTitle() if value is not None else None)
                        mds.append(md.getTitle())
                page_list.append(dict(page=pg_name, method=mds, value=vals))
                # print(page_list)
            return dict(pages=page_list)
        elif node.getTitle() == "重跑次数":
            for times in node.getSubTopics():
                return dict(times=times.getTitle())
        elif node.getTitle() == "跳过":
            for skip in node.getSubTopics():
                return dict(skip=skip.getTitle())
        elif node.getTitle() == "描述":
            for desc in node.getSubTopics():
                return dict(desc=desc.getTitle())
        elif node.getTitle() == "步骤":
            steps = []
            for step in node.getSubTopics():
                if step.getTitle().startswith("assert"):
                    # 这是断言
                    sub = step.getSubTopics()
                    if len(sub) > 2:
                        expected, act, msg = sub
                        steps.append(dict(
                            action=step.getTitle(),
                            expected=expected.getTitle(),
                            actually=act.getTitle(),
                            msg=msg.getTitle()
                        ))
                    else:
                        act, msg = sub
                        steps.append(dict(
                            action=step.getTitle(),
                            actually=act.getTitle(),
                            msg=act.getTitle()
                        ))
                else:
                    # 获取参数
                    params = []
                    if self.get_son(step) is not None:
                        for par in step.getSubTopics():
                            params.append(par.getTitle())
                    steps.append(dict(action=step.getTitle(),
                                      params=params))
                    # print('steps', steps)
            return dict(steps=steps)

    def parse_to_case(self, case_list):  # 自动写用例
        print(case_list)
        for case in case_list:
            # if case.get("skip") == "True":  # true跳过用例
            #     print('跳过了测试用例')
            #     continue
            suite = case.get("suite")
            suite_dir = os.path.join(Config.suite_dir, suite)
            # 若不存在则创建该目录
            if not os.path.exists(suite_dir):
                os.mkdir(suite_dir)
            case_file = "{}.py".format(case.get("name"))  # 获取用例名生成py文件
            with open(os.path.join(suite_dir, case_file), "w+", encoding="utf-8") as f:  # 写入
                page_info = self.deal_pages(case.get("pages"))
                pages, method = page_info.get("page"), page_info.get("method")
                # print('pages,method', pages, method)
                # import写入
                for head in Config.xmind_head:
                    if not head.endswith("\n"):
                        head += "\n"
                    f.write(head)
                for p in pages:
                    f.write("from Page.{} import {}\n".format(p[0], p[1]))
                f.write("import unittest")
                # 换行
                f.write("\n\n")

                # 编写测试类
                f.write("class {}(BaseCase):\n\n".format(case.get("name")))

                # 重跑次数
                if case.get('times'):
                    f.write("    retry = {}\n\n".format(case.get("times")))
                # 跳过
                if case.get('skip') == 'True':
                    f.write("    @unittest.skip('用例跳过为True')\n\n")

                # 编写装饰器
                f.write("    @screenshot\n")

                # 编写测试类
                f.write("    def test(self):\n")

                # 编写描述
                f.write("        \"\"\"{}\"\"\"\n".format(case.get("desc")))

                # 编写内容
                self.deal_steps(f, case.get("steps"), method)

    def deal_pages(self, pages):
        rt = defaultdict(list)
        for page in pages:
            page_info = page.get("page")
            page_name, page_cls = ".".join(page_info.split(".")[:-1]), page_info.split(".")[-1]
            if page.get('method') and page.get('value'):
                # 有返回值的函数
                for md, val in zip(page.get('method'), page.get('value')):
                    rt['method'].append(dict(method=md, val=val, page=page_cls))
            rt['page'].append((page_name, page_cls))
        # print('rt', rt)
        return rt

    def deal_steps(self, f, steps, method):
        for s in steps:
            sens = "        "
            if s.get("action").startswith("assert"):
                action = s.get("action")
                expected = s.get("expected")
                msg = "\"{}\"".format(s.get("msg"))
                actually = s.get("actually")
                if expected:  # equal等断言
                    arg = re.findall(r"\{(.+)\}", expected)
                    if arg:
                        arg = ["{}={}".format(x, x) for x in arg]
                        expected = "\"{}\".format({})".format(expected, *arg)
                sens = "{}self.{}({}, {}, {})".format(sens, action, expected, actually, msg)
                f.write(sens + "\n")
            else:
                # 判断操作有无返回值
                # print('method', method)
                for m in method:
                    if s.get("action") == m.get('method'):  # 找到该操作
                        returns = m.get('val')
                        if returns is not None:
                            if ";" in returns:
                                returns = ", ".join(["{}".format(x) for x in returns.split(";")])
                            sens = "{}{} = ".format(sens, returns)

                        if s.get("params"):
                            params = ", ".join(["\"{}\"".format(x) for x in s.get("params")])
                            sens = "{}{}(self.driver).{}({})".format(sens, m.get('page'), s.get("action"), params)
                        else:
                            sens = "{}{}(self.driver).{}()".format(sens, m.get('page'), s.get("action"))
                        f.write(sens + "\n")
                        break
