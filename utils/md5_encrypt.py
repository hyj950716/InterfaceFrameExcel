# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/2 11:02
@Auth ： 胡英俊(请叫我英俊)
@File ：md5_encrypt.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
import hashlib

def md5_encrypt(text):
    m5 = hashlib.md5()
    m5.update(text.encode("utf-8"))
    value = m5.hexdigest()
    return value


if __name__ == "__main__":
    print(md5_encrypt("zhangsan01"))