#!user/bin/env python3
# -*- coding: UTF-8 -*-

"""
tools项目
@Time : 2021/1/29 10:38
@File : 工程常用的logger的配置.py
@Software: PyCharm
@author: 王伟 A21036

         常见的logger的配置功能。
        说明：
        1、配置文件，滚动日志的大小
"""
# coding=utf-8
import os
import sys
from loguru import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log_file_path = os.path.join(BASE_DIR, 'Log/my.log')
err_log_file_path = os.path.join(BASE_DIR, 'Log/err.log')

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
# logger.add(s)
logger.add(log_file_path, rotation="500 MB", encoding='utf-8')
logger.add(err_log_file_path, rotation="500 MB", encoding='utf-8',level='ERROR')
logger.debug("That's it, beautiful and simple logging!")
logger.debug("中文日志可以不")
logger.error("严重错误")
