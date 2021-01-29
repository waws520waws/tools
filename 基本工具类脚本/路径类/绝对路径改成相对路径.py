#!user/bin/env python3
# -*- coding: UTF-8 -*-

"""
tools项目
@Time : 2021/1/29 13:53
@File : 绝对路径改成相对路径.py
@Software: PyCharm
@author: 王伟 A21036

         绝对路径改成相对路径功能。
        说明：
        1、linux平台
"""
def calculate_relative_path(a, b):
    """
    计算相对路径:
        已知两个绝对路径 a 和 b, 求 b 相对于 a 的相对路径.
    注:
        1. a 和 b 来自于同一个盘符
        2. 路径分隔符用正斜杠 "/"
    """
    if a in b:
        out = b.split(a)[-1].lstrip("/").lstrip("\\").replace("\\", "/")
        return out
    a, b = a.split('/'), b.split('/')
    # a = 'D:/M/N/O/P/a.py' --> ['D:', 'M', 'N', 'O', 'P', 'a.py']
    # b = 'D:/M/N/Q/b.py' --> ['D:', 'M', 'N', 'Q', 'b.py']
    intersection = 0  # 交汇点位置
    for index in range(0, min(len(a), len(b))):
        m, n = a[index], b[index]
        if m != n:
            intersection = index  # --> 3
            break

    if intersection == len(a):
        out = f"./{b[-1]}"
    else:
        out = (len(a) - intersection - 1) * '../' + '/'.join(b[intersection:])
    return out


if __name__ == '__main__':
    a = r"/home/xinye/sdk/jdk1.8.0_161/bin"
    b = r"/home/xinye/kkk/www/ee"
    print(calculate_relative_path(a,b))