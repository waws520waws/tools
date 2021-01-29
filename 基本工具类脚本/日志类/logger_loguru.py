#!user/bin/env python3
# -*- coding: UTF-8 -*-

"""
tools项目
@Time : 2021/1/29 10:04
@File : logger_loguru.py
@Software: PyCharm
@author: 王伟 A21036

         loguru模块的日志功能。
        说明：
        1、安装
        2、使用
        3、多线程
        参考的博客：https://blog.csdn.net/bailang_zhizun/article/details/107863671
"""
"""
安装
pip\pip3 install loguru
"""


"""
基本使用
from loguru import logger
logger.debug("This's a log message")
"""



"""
# 特别的格式可以使用add 进行添加
import sys
from loguru import logger
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.debug("This's a new log message")
"""



"""
add函数的可以指定的添加的格式，注意sink
sink 可以传入一个 file 对象，例如 sys.stderr 或者 open('file.log', 'w') 都可以。
sink 可以直接传入一个 str 字符串或者 pathlib.Path 对象，其实就是代表文件路径的，如果识别到是这种类型，它会自动创建对应路径的日志文件并将日志输出进去。
sink 可以是一个方法，可以自行定义输出实现。
sink 可以是一个 logging 模块的 Handler，比如 FileHandler、StreamHandler 等等，这样就可以实现自定义 Handler 的配置。
sink 还可以是一个自定义的类，具体的实现规范可以参见官方文档。

def add(
        self,
        sink,
        *,
        level=_defaults.LOGURU_LEVEL,
        format=_defaults.LOGURU_FORMAT,
        filter=_defaults.LOGURU_FILTER,
        colorize=_defaults.LOGURU_COLORIZE,
        serialize=_defaults.LOGURU_SERIALIZE,
        backtrace=_defaults.LOGURU_BACKTRACE,
        diagnose=_defaults.LOGURU_DIAGNOSE,
        enqueue=_defaults.LOGURU_ENQUEUE,
        catch=_defaults.LOGURU_CATCH,
        **kwargs
    ):
    pass
"""



"""
# 创建一个文件并进行使用,日志会同时在文件中和控制台中同时进行输出
from loguru import logger
logger.add("runtime.log")       # 创建了一个文件名为runtime的log文件
logger.debug("This's a log message in file")
"""



"""
默认输出控制台，但是不想输出控制台，可以直接remove,只会输出到指定的文件中
from loguru import logger
logger.remove(handler_id=None)
logger.add("runtime.log")  # 创建了一个文件名为runtime的log文件
logger.debug("This's a log message in file")
"""



"""
日志的命名可以以照当前的时间进行
from loguru import logger
logger.add("runtime_{time}.log")       # 创建了一个文件名为runtime的log文件
logger.debug("This's a log message in file")
"""



"""
滚动的日志文件的配置
1）大小
logger.add("file_1.log", rotation="500 MB")
2）时间：每天中午12：00
logger.add("file_2.log", rotation="12:00")
3）一周一更新
logger.add("file_3.log", rotation="1 week")
"""



"""
指定日志保留时长
logger.add("file_X.log", retention="10 days") 
"""

"""
配置文件压缩格式
logger.add("file_Y.log", compression="zip")

异步写入
logger.add("somefile.log", enqueue=True)  # 异步写入

序列化为json
logger.add("somefile.log", serialize=True)  # 序列化为json
"""



"""
异常捕获@logger.catch 装饰器的方式
from loguru import logger
logger.add("runtime.log",encoding="utf-8") 
@logger.catch
def my_function(x, y, z):
    return 1 / (x + y + z)    # An error? It's caught anyway!
my_function(0, 0, 0)
"""



"""
使用exception的方式捕获异常
from loguru import logger
logger.add("runtime.log") 
def my_function1(x, y, z):
    try:
        return 1 / (x + y + z)
    except ZeroDivisionError:
        logger.exception("What?!")
my_function1(0, 0, 0)
"""



"""
多个文件中在调用logger的时候，只需要在每个文件的开头部分导入logger即可
Asynchronous, Thread-safe, Multiprocess-safe。
由于在 loguru 中有且仅有一个对象：logger。所以loguru是可以在多块module文件中使用的，而且不会出现冲突

# test1.py
from loguru import logger
def func(a, b):
    logger.info("Process func")
    return a / b
def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")


# test2.py
#coding:utf-8
from loguru import logger
import exceptions_catching2_03 as ec3
if __name__=='__main__':
    logger.add("run.log")
    logger.info("Start!")
    ec3.nested(0)
    logger.info("End!")
"""



"""
多线程中的使用
所有添加至logger的sink默认都是线程安全的
#coding:utf-8
from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import sleep, ctime
from loguru import logger
class CleanOutputSet(set):
    def __str__(self):
        return ','.join(x for x in self)
 
lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()
 
def loop(nsec):
    myname = current_thread().name
    logger.info("Startted {}", myname)

    '''
    锁的申请和释放交给with上下文管理器
    '''
    with lock:
        remaining.add(myname)
    sleep(nsec)
 
    logger.info("Completed {} ({} secs)", myname, nsec)
 
    with lock:
        remaining.remove(myname)
        logger.info("Remaining:{}", (remaining or 'NONE'))
 
'''
_main()函数是一个特殊的函数，只有这个模块从命令行直接运行时才会执行该函数（不能被其他模块导入）
'''
def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()
 
'''
这个函数（装饰器的方式）会在python解释器中注册一个退出函数，也就是说，他会在脚本退出之前请求调用这个特殊函数
'''
@register
def _atexit():
    logger.info("All Thread DONE!")
    logger.info("\n===========================================================================\n")
 
if __name__=='__main__':
    logger.add("run.log")
 
    _main()
"""

# coding:utf-8

from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import sleep, ctime

from loguru import logger


class CleanOutputSet(set):
    def __str__(self):
        return ','.join(x for x in self)


lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()


def loop(nsec):
    myname = current_thread().name

    logger.info("Startted {}", myname)

    '''
    锁的申请和释放交给with上下文管理器
    '''
    with lock:
        remaining.add(myname)
    sleep(nsec)

    logger.info("Completed {} ({} secs)", myname, nsec)

    with lock:
        remaining.remove(myname)
        logger.info("Remaining:{}", (remaining or 'NONE'))


'''
_main()函数是一个特殊的函数，只有这个模块从命令行直接运行时才会执行该函数（不能被其他模块导入）
'''


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


'''
这个函数（装饰器的方式）会在python解释器中注册一个退出函数，也就是说，他会在脚本退出之前请求调用这个特殊函数
'''


@register
def _atexit():
    logger.info("All Thread DONE!")
    logger.info("\n===========================================================================\n")


if __name__ == '__main__':
    logger.add("run.log",serialize=True)

    _main()








