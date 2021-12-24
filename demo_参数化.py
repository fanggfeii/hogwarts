# @author:  fangfei
# @time  :  2021/12/24/0024  17:04
# @file  :  demo_参数化.py
# @desc  : 
import pytest


@pytest.mark.parametrize('key, result', [
    ['appium', 200],
    ['selenium', 300],
    ['requests', 400],
    ['docker', 500]
], ids=[1, 2, 3, 4])
def test_interface(key, result):
    url = f"http://www.baidu.com/{key}"
    print(url, result)
