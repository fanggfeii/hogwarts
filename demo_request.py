# @author:  fangfei
# @time  :  2021/12/22/0022  14:33
# @file  :  demo_request.py
# @desc  : 
import requests

r = requests.get('http://baidu.com')
# print(r.status_code)
# print(r.raise_for_status())
# print(r.headers)
print(r.headers['date'])
print(r.headers.get('date'))
