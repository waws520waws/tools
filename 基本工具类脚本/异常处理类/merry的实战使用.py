#!user/bin/env python3
# -*- coding: UTF-8 -*-

"""
tools项目
@Time : 2021/1/29 17:33
@File : merry的实战使用.py
@Software: PyCharm
@author: 王伟 A21036

         merry的异常处理实战功能。
"""
import requests
from merry import Merry
from requests import ConnectTimeout

merry = Merry()
merry.logger.disabled = True
catch = merry._try

class BaseClass(object):

    @staticmethod
    @merry._except(ZeroDivisionError)
    def process_zero_division_error(e):
        print('zero_division_error', e)

    @staticmethod
    @merry._except(FileNotFoundError)
    def process_file_not_found_error(e):
        print('file_not_found_error', e)

    @staticmethod
    @merry._except(Exception)
    def process_exception(e):
        print('exception', type(e), e)

    @staticmethod
    @merry._except(ConnectTimeout)
    def process_connect_timeout(e):
        print('connect_timeout', e)

class Calculator(BaseClass):

    @catch
    def process(self, num1, num2, file):
        result = num1 / num2
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(result))

class Fetcher(BaseClass):

    @catch
    def process(self, url):
        response = requests.get(url, timeout=1)
        if response.status_code == 200:
            print(response.text)

if __name__ == '__main__':
    c = Calculator()
    c.process(1, 0, 'result.txt')

    f = Fetcher()
    f.process('http://notfound.com')
