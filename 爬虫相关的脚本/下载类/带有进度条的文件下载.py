#!user/bin/env python3
# -*- coding: UTF-8 -*-

"""
tools项目--下载类
@Time : 2021/1/28 10:34
@File : 带有进度条的文件下载.py
@Software: PyCharm
@author: 王伟 A21036

         下载文件带有进度条功能。
        说明：
        1、tqdm 进度条的使用方式
"""

import requests
import os
from tqdm import tqdm
from loguru import logger

def down_pdf_with_tqdm(url,dst):
    """
    下载文件,带有进度条的方式
    :param url: pdf的下载的url地址
    :param dst: 下载文件的路径，到下载的文件名：C:\Users\a21036\Desktop\tools\爬虫相关的脚本\下载类\荣威iMAX8用户手册-2020.12.10.pdf
    :return: 返回文件是否下载完成
    """
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        'Connection': 'close'
    }
    response = requests.get(url, headers=headers, stream="TRUE")
    file_size = int(response.headers['content-length'])
    if os.path.exists(dst):
        first_byte = os.path.getsize(dst)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size

    header = {"Range": f"bytes={first_byte}-{file_size}"}

    pbar = tqdm(total=file_size, initial=first_byte, unit='B', unit_scale=True, desc=dst)
    req = requests.get(url, headers=header, stream=True)
    with open(dst, 'ab') as f:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                pbar.update(1024)
    pbar.close()
    logger.info(url + " 文件已经下载完成")
    return True


if __name__ == '__main__':
    url = "https://sanbaobeian.dpac.org.cn/uploads/AttachmentData/荣威iMAX8用户手册-2020.12.10.pdf"
    dst = url.split("/")[-1]
    down_pdf_with_tqdm(url,dst)