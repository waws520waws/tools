#!user/bin/env python3
# -*- coding: UTF-8 -*-

"""
tools项目
@Time : 2021/1/29 17:28
@File : merry的使用.py
@Software: PyCharm
@author: 王伟 A21036

         merry类的使用功能。
        说明：
        1、更加优雅的异常处理的方法
        参考的blog：https://cuiqingcai.com/9134.html
"""
"""
安装
pip3 install merry
"""

from merry import Merry

merry = Merry()
merry.logger.disabled = True

# 异常的监听 _try
@merry._try
def process(num1, num2, file):
    result = num1 / num2
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(result))

# 在merry中定义异常的处理方式
@merry._except(ZeroDivisionError)
def process_zero_division_error(e):
    print('zero_division_error', e)

@merry._except(FileNotFoundError)
def process_file_not_found_error(e):
    print('file_not_found_error', e)

@merry._except(Exception)
def process_exception(e):
    print('exception', type(e), e)



"""
这里的异常将异常捕获和异常的处理分成了两个部分，脱离了同一个环境，这样变量的传递通过g
它使用了 merry.g 这个对象来存储上下文的变量，在 主逻辑方法里面要把想要传递的参数赋值进去，在异常处理的方法里面再用 merry.g 取出来
@merry._try
def app_logic():
    db = open_database()
    merry.g.database = db  # save it in the error context just in case
    # do database stuff here

@merry._except(Exception)
def catch_all():
    db = getattr(merry.g, 'database', None)
    if db is not None and is_database_open(db):
        close_database(db)
    print('Unexpected error, quitting')
    sys.exit(1)
"""

if __name__ == '__main__':
    process(1, 2, 'result/result.txt')
    process(1, 0, 'result.txt')
    process(1, 2, 'result.txt')
    process(1, [1], 'result.txt')


