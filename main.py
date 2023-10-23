import requests
import json
import os
import hashlib

def test():
    print("register------")
    data = json.dumps({"username":"hxf001","password":"hxf950716","email":"hxf@qq.com"})
    param = {"username":"hxf001","password":"hxf950716","email":"hxf@qq.com"}
    try:
        r = requests.post("http://124.223.167.147:8080/register/",data=data)
    except Exception as e:
        print(e)
