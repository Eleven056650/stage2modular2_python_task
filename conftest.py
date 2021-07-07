# -*- coding: utf-8 -*-
# username: huangqun

import pytest
from python_code.calc import Calulator


@pytest.fixture(scope='class')
def Replay_calc():
    print("开始计算")
    calc = Calulator()
    yield calc
    print("计算结束")


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        # item.name 用例名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        print(item.nodeid)
        # item.nodeid 用例路径
        item._nodeid = item.nodeid.encode("utf-8").decode('unicode_escape')
