# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/24 16:12
@Auth ： 胡英俊(请叫我英俊)
@File ：public_data.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
import os

# 整个项目的根目录的绝对路径
baseDir = os.path.dirname(os.path.dirname(__file__))

# 获取数据文件的绝对路径
file_path = baseDir + '\\TestData\\inter_test_data.xlsx'

API_apiName = 2
API_requestUrl = 3
API_requestMothod = 4
API_paramsType = 5
API_apiTestCaseFileName = 6
API_active = 7

CASE_requestData = 1
CASE_relyData = 2
CASE_responseCode = 3
CASE_responseData = 4
CASE_dataStore = 5
CASE_checkPoint = 6
CASE_active = 7
CASE_status = 8
CASE_errorInfo = 9

# 存储依赖数据
RELY_DATA = {"request": {"register": {"1": {"username": "zhangsan","password": "zhangsan01"}}}, "response": {"register": {"1": {"userid": 12}}}}


if __name__ == "__main__":
    print(file_path)