# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/24 16:21
@Auth ： 胡英俊(请叫我英俊)
@File ：interface_auto_test.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
'''
第一步：解析excel，获取到需要执行的api相关数据
第二步：通过api获取到需要执行的case相关数据
第三步：发送接口请求，并获取到响应body
第四步：做结果校验
第五步：写测试结果，统计本次自动化测试结果
'''

from utils.ParseExcel import ParseExcel
from config.public_data import *
from Action.get_rely import GetRely
from utils.HttpClient import *
from Action.data_store import *
from Action.check_result import *
from Action.write_test_result import *


def main():
    parseE = ParseExcel()
    parseE.loadWorkBook(file_path)
    sheetObj = parseE.getSheetByName("API")
    activeList = parseE.getColumn(sheetObj, API_active)

    for idx, cell in enumerate(activeList[1:], 2):
        if cell.value == "y": # 说明当前行所在的api需要执行自动化测试

            # --------- 第一步 ------------
            # 获取需要执行的接口所在行的行对象
            rowObj = parseE.getRow(sheetObj, idx)
            # print(rowObj)
            apiName = rowObj[API_apiName - 1].value
            requestUrl = rowObj[API_requestUrl - 1].value
            requestMethod = rowObj[API_requestMothod - 1].value
            paramsType = rowObj[API_paramsType - 1].value
            apiTestCaseFileName = rowObj[API_apiTestCaseFileName - 1].value
            # print(apiName, " ", requestUrl, " ", requestMethod, " ", paramsType, " ", apiTestCaseFileName)

            # --------- 第二步 ------------
            # 下一步读用例sheet表，获取api执行时需要的数据
            caseSheetObj = parseE.getSheetByName(apiTestCaseFileName)
            caseActiveObj = parseE.getColumn(caseSheetObj, CASE_active)
            print(caseActiveObj)
            for c_idx, c_cell in enumerate(caseActiveObj[1:], 2):
                print(c_idx, " ", c_cell.value)
                if c_cell.value == "y":
                    # 说明此case需要被执行
                    caseRowObj = parseE.getRow(caseSheetObj, c_idx)
                    requestData = caseRowObj[CASE_requestData -1].value
                    relyData = caseRowObj[CASE_relyData -1].value
                    responseCode = caseRowObj[CASE_responseCode - 1].value
                    dataStore = caseRowObj[CASE_dataStore - 1].value
                    checkPoint = caseRowObj[CASE_checkPoint -1].value
                    print(requestData, " ", relyData, " ",responseCode, " ",dataStore, " ",checkPoint)


                # --------第三步-----
                if relyData:
                    print("进行第%s接口第%s条case的依赖数据处理"%(idx - 1, c_idx - 1))
                    relyData = eval("%s" % relyData)
                    requestData = GetRely.get(relyData, eval("%s" % requestData))
                    print(requestData)

                # ----- 第四步：发送接口请求，并获取到响应的body---------
                hc = HttpClient()
                response = hc.request(requestMethod, requestUrl, paramsType, "%s" % requestData)

                # -----第五步：做依赖数据的存储-----------------
                if response.status_code == int(responseCode):
                    responseData = response.json()
                    if dataStore:
                        RelyDataStore.do(eval(dataStore), apiName, c_idx-1, eval(requestData), responseData)

                    print(RELY_DATA)
                    # ---------第六步：做结果校验----------------
                    errorkey = CheckResult.check(responseData, eval(checkPoint) if checkPoint else {})
                    write_result(parseE,caseSheetObj, responseData, errorkey, c_idx)
                else:
                    print("接口%s的第%s条用例响应失败，status_code = %s "% (apiName, c_idx - 1, response.status_code))
        else:
            print("第%s个接口本次不需要执行" % idx)

if __name__ == "__main__":
    main()


