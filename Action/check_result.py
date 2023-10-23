# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/2 16:32
@Auth ： 胡英俊(请叫我英俊)
@File ：check_result.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
import re


class CheckResult(object):
    def __init__(self):
        pass

    @classmethod
    def check(self, responseObj, checkPoint):
        errorkey = {}
        {"code": "00", "userid": {"type": "N"}, "id": {"value": "^\d+$"}}
        for key, value in checkPoint.items():
            if isinstance(value, str):
                # 说明是等值校验
                if responseObj.get(key, "") !=value:
                    errorkey[key] = {"expect":value, "realy":responseObj.get(key, "")}
            elif isinstance(value, dict):
                # 说明需要通过正则或者时数据类型校验
                sourceData = responseObj.get(key, "")
                if "value" in value:
                    regStr = value["value"]
                    rg = re.match(regStr, "%s"% sourceData)
                    if not rg:
                        errorkey[key] =  {"expect":value, "realy":responseObj.get(key, "")}
                elif "type" in value:
                    # 说明是校验数据类型
                    typeS = value["type"]
                    if typeS == "N":
                        # 整型
                        if not isinstance(sourceData, int):
                            errorkey[key] =  {"expect":value, "realy":responseObj.get(key, "")}
                        elif typeS == "S":
                            # 字符串类型
                            pass
        return errorkey


if __name__ == "__main__":
    r = {"code": "01", "userid": 12, "id": "12sd"}  # check
    c = {"code": "00", "userid": {"type": "N"}, "id": {"value": "^\d+$"}}
    print(CheckResult.check(r,c))