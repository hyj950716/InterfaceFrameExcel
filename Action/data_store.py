# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/2 13:54
@Auth ： 胡英俊(请叫我英俊)
@File ：data_store.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
from config.public_data import RELY_DATA


class RelyDataStore(object):
    def __int__(self):
        pass

    @classmethod
    def do(cls, storePoint, apiName, caseId, request_source={}, response_source={}):

        ds = {"request": request_source, "response": response_source}
        for key, value in storePoint.items():
            print("存储接口[%s]的第%s条case的依赖%s数据" % (apiName, caseId, key))
            for i in value:
                if i in ds[key]:
                    # 如果在，取出对应的值，然后放入全量变量中存储
                    if apiName not in RELY_DATA[key]:
                        RELY_DATA[key] = {apiName: {str(caseId): {i: ds.get(key).get(i)}}}
                    elif str(caseId) not in RELY_DATA[key][apiName]:
                        RELY_DATA[key][apiName][str(caseId)] = {i: ds.get(key).get(i)}
                    else:
                        RELY_DATA[key][apiName][str(caseId)][i] = ds.get(key).get(i)
                else:
                    print("接口[%s]请求参数中不存在字段%s" % (apiName, i))

        # for key, value in storePoint.items():
        #     if key == "request":
        #         # 说明存储的数据来自请求参数request_source
        #         print("存储接口[%s]的第%s条case的依赖数据"%(apiName, caseId))
        #         for i in value:
        #             if i in request_source:
        #                 # 如果在，取出对应的值，然后放入全量变量中存储
        #                 if apiName not  in RELY_DATA["request"]:
        #                     RELY_DATA["request"] = {apiName:{caseId:{i:request_source.get(i)}}}
        #                 else:
        #                     if caseId not in RELY_DATA["request"][apiName]:
        #                         RELY_DATA["request"][apiName] = {caseId:{i:request_source.get(i)}}
        #                     else:
        #                          RELY_DATA["request"][apiName][caseId][i] = request_source.get(i)
        #             else:
        #                 print("接口[%s]请求参数种不存在字段%s"%(apiName, i))
        #     elif key == "response":
        #         # 说明存储的数据来源响应body的response_source中
        #         print("存储接口[%s]的第%s条case的响应数据"%(apiName, caseId))
        #         for j in value:
        #             if j in response_source:
        #                 # 如果在，取出对应的值，然后放入全量变量中存储
        #                 if apiName not  in RELY_DATA["response"]:
        #                     RELY_DATA["response"] = {apiName:{caseId:{j:response_source.get(j)}}}
        #                 else:
        #                     if caseId not in RELY_DATA["response"][apiName]:
        #                         RELY_DATA["response"][apiName] = {caseId:{j:response_source.get(j)}}
        #                     else:
        #                          RELY_DATA["response"][apiName][caseId][j] = response_source.get(j)
        #             else:
        #                 print("接口[%s]请求参数种不存在字段%s"%(apiName, j))

if __name__ == "__main__":
    request = {"username": "hxf0001","password":"hxf950716","email":"hxf@qq.com"}
    store_point = {"request": ["username", "password"], "response": ["userid"]}
    response = {"userid": 12, "code": "00"}
    RelyDataStore.do(store_point, "register", 1, request, response)
    print(RELY_DATA)