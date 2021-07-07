# -*- coding: utf-8 -*-
# username: huangqun

import allure
import pytest
import logging
import yaml

# from python_code.calc import Calulator
# @pytest.fixture(scope='class')  # fixture放进conftest.py统一配置
# def Replay_calc():
#     print("开始计算")
#     calc = Calulator()
#     yield calc
#     print("计算结束")


with open("./datas/calcdata.yml", encoding='utf-8') as f:
    add = yaml.safe_load(f)['add']
    add_datas = add['adddata']
    add_node_ids = add['addnodeid']
    add_fail_datas = add['addfaildata']
    add_fail_ids = add['addfailid']
with open("./datas/calcdata.yml", encoding='utf-8') as g:
    div = yaml.safe_load(g)['div']
    div_datas = div['divdata']
    div_node_ids = div['divnodeid']
    div_fail_datas = div['divfaildata']
    div_fail_ids = div['divfailid']

logging.basicConfig(level=logging.INFO)
plog = logging.getLogger(name='log1.log')
TEST_CASE_LINK = 'https://gitee.com/huangqun1535/test_huangqun.git'


class TestCalc:

    @allure.testcase(TEST_CASE_LINK, 'gitee上传用例地址')
    @allure.title("加法运算")
    @allure.feature("计算器加法运算：主功能测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('a, b, expect', add_datas, ids=add_node_ids)
    def test_add(self, a, b, expect, Replay_calc):
        # 实例化计算器类
        # calc = Calulator()
        # 调用add方法
        result = Replay_calc.add(a, b)
        # 避免python底层计算丢位
        if isinstance(result, float):
            result = round(result, 6)
        print(result)
        # 判断结果，断言
        assert result == expect
        plog.info("加法运算------{0:^8}+{1:^8}={2:^8}------测试用例".format(a, b, expect))

    @allure.testcase(TEST_CASE_LINK, 'gitee上传用例地址')
    @allure.title("加法运算")
    @allure.story("计算器加法运算：不规范输入值测试")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('a, b, expect', add_fail_datas, ids=add_fail_ids)
    def test_add_fail(self, a, b, expect, Replay_calc):
        with pytest.raises(TypeError):
            Replay_calc.add(a, b)
        plog.info("加法运算------{0:^8}+{1:^8}={2:^8}------异常场景测试用例".format(a, b, expect))

    @allure.testcase(TEST_CASE_LINK, 'gitee上传用例地址')
    @allure.title("除法运算")
    @allure.feature("计算器除法运算：主功能测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('a, b, expect', div_datas, ids=div_node_ids)
    def test_div(self, a, b, expect, Replay_calc):
        # 调用div方法
        result = Replay_calc.div(a, b)
        # 避免python底层计算丢位
        if isinstance(result, float):
            result = round(result, 6)
        print(result)
        # 判断结果，断言
        assert result == expect
        plog.info("除法运算------{0:^8}+{1:^8}={2:^8}------测试用例".format(a, b, expect))

    @allure.testcase(TEST_CASE_LINK, 'gitee上传用例地址')
    @allure.title("除法运算")
    @allure.story("计算器除法运算：不规范输入值测试")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('a, b, expect', div_fail_datas, ids=div_fail_ids)
    def test_div_fail(self, a, b, expect, Replay_calc):
        if b != 0:
            with pytest.raises(TypeError):
                Replay_calc.div(a, b)
        else:
            with pytest.raises(ZeroDivisionError):
                Replay_calc.div(a, b)
        plog.info("除法运算------{0:^8}+{1:^8}={2:^8}------异常场景测试用例".format(a, b, expect))

    @allure.title("测试报告图片")
    def test_link_photo(self):
        allure.attach.file('./photos/计算器加法除法测试报告.jpg', name='计算器加法除法测试报告', attachment_type=allure.attachment_type.JPG)


if __name__ == '__main__':
    pytest.main()
# 按重要等级执行3+示例：pytest test_calc.py --allure-severities normal,critical
