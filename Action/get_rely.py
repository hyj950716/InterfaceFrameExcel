# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/2 10:23
@Auth ： 胡英俊(请叫我英俊)
@File ：get_rely.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
from config.public_data import RELY_DATA
from utils.md5_encrypt import md5_encrypt

class GetRely(object):
    def __init__(self):
        pass

    @classmethod
    def get(cls, relyData, dataSource):
        data = dataSource.copy()
        for key, value in relyData.items():
            # 说明被依赖的数据应该去RELY_DATA的request中获取
            for k, v in value.items():
                interfaceName, case_id = v.split("->")
                val = RELY_DATA[key][interfaceName][case_id][k]
                if k == "password":
                    val = md5_encrypt(val)
                    if k in data:
                        data[k] = val
                else:
                    if k in data:
                        data[k] = val

        return data

if __name__ == "__main__":
    s = {"username": "", "password": "", "userid": 0}
    rely = {"request": {"username": "register->1", "password": "register->1"}, "response": {"userid": "register->1"}}
    print(GetRely.get(rely, s))