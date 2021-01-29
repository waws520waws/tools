#!user/bin/env python3
# -*- coding: UTF-8 -*-

"""
Tools项目
@Time : 2021/1/29 17:04
@File : md5加密算法.py
@Software: PyCharm
@author: 王伟 A21036

         md5的加密功能。
        说明：
        1、md5的加密
        参考的blog:https://blog.csdn.net/geerniya/article/details/77531626
"""

"""
import hashlib         #导入hashlib模块

md = hashlib.md5()     #获取一个md5加密算法对象
md.update('how to use md5 in hashlib?'.encode('utf-8'))                   #制定需要加密的字符串
print(md.hexdigest())  #获取加密后的16进制字符串,一共32位
"""


# 例程
import hashlib

db = {}

#计算密码的md5值
def get_md5(s):
    md = hashlib.md5()
    md.update(s.encode('utf-8'))
    return md.hexdigest()

#注册新的用户
def register(username,password):
    db[username] = get_md5(password + username + 'SSC')

#验证用户登录
def login(username,password):
    if not username in db:
        print('User is not exist!')
        return
    if db[username] == get_md5(password + username + 'SSC'):
        print('Login sucessfully')
    else:
        print('Incorrect password')

#主程序
if __name__ == '__main__':
    user1 = 'xiaoming'
    psw1 = '123456'
    register(user1,psw1)  #注册新用户
    login(user1,psw1)     #登录成功
    login(user1,psw1+' ')  #密码错误，登录失败
    login(user1+' ',psw1)  #用户名错误，登录失败