# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/2 17:22
@Auth ： 胡英俊(请叫我英俊)
@File ：write_test_result.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
from config.public_data import *

def write_result(wbObj, sheetObj, responseData, errorKey, rowNum):
    try:
        # 写响应boby
        wbObj.writeCell(sheet=sheetObj, content="%s" % responseData,
                        rowNo=rowNum, colsNo=CASE_responseData)

        # 写校验结果状态列&错误列信息
        if errorKey:
            wbObj.writeCell(sheet=sheetObj, content="faild",
                            rowNo=rowNum, colsNo=CASE_status)
            wbObj.writeCell(sheet=sheetObj, content="%s" % errorKey,
                            rowNo=rowNum, colsNo=CASE_errorInfo)
        else:
            wbObj.writeCell(sheet=sheetObj, content="pass",
                            rowNo=rowNum, colsNo=CASE_status)
    except Exception as er:
        raise er
