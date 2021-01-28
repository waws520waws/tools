#!user/bin/env python3
# -*- coding: UTF-8 -*-

"""
tools项目-爬虫相关脚本
@Time : 2021/1/28 10:12
@File : requests_bs4.py
@Software: PyCharm
@author: 王伟 A21036

         requests_bs4的代码功能。
        说明：
        1、最常用的下载和解析的脚本
        2、requests
        3、bs4
"""
import requests
from bs4 import BeautifulSoup
headers =  {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            'Connection': 'close'
        }

url = ""
html = requests.get(url,headers = headers).text
soup = BeautifulSoup(html,"lxml")

# 集合形式的tags
a_list = soup.select("a")
for a in a_list:
    pass

# 单个tag
title = soup.select("title")[0]

# 取出text
text = soup.select("title")[0].get_text()

# 取出属性
href = soup.select("title")[0].get("href")

# 下面接处理方式

