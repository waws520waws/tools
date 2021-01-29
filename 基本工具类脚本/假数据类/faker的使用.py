#!user/bin/env python3
# -*- coding: UTF-8 -*-

"""
tools项目
@Time : 2021/1/29 17:40
@File : faker的使用.py
@Software: PyCharm
@author: 王伟 A21036

         faker的使用。
        说明：
        1、制作假数据
        2、支持的语言(默认英文)
            简体中文：zh_CN
            繁体中文：zh_TW
            美国英文：en_US
            英国英文：en_GB
            德文：de_DE
            日文：ja_JP
            韩文：ko_KR
            法文：fr_FR
        参考blog:https://mp.weixin.qq.com/s/iLjr95uqgTclxYfWWNxrAA
"""

"""
安装
pip3 install faker
"""

from faker import Faker

faker = Faker()
print('name:', faker.name())
print('address:', faker.address())
print('text:', faker.text())

faker1 = Faker("zh_CN")
print('name:', faker1.name())
print('address:', faker1.address())
print('text:', faker1.text())

"""
常见方法的汇总：
Address
Color
Company
Credit Card
Date Time
File
Geo
Internet
Job
Lorem：于生成一些假文字数据，包括句子、自然段、长文本、关键词等，另外可以传入不同的参数来控制生成的长度
Misc：用于生成生成一些混淆数据，比如密码、sha1、sha256、md5 等加密后的内容
Person：用于生成和人名相关的数据，包括姓氏、名字、全名、英文名等内容，还能区分男女名字
User-Agent：用于生成和浏览器 User-Agent 相关的内容，可以定制各种浏览器，还可以传入版本信息来控制生成的内容
"""