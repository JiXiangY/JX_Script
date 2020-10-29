# -*- coding: UTF-8 -*-
import json
import os,sys

class configure():
    host = ""
    port = ""
    session = ""
    authKey = ""
    qq = ""
    receiveTime = 5
    done = False
    jiChou = False
    def __init__(self):
        if configure.done == True:
            return

        try:
            data = open("configure.json","r+")
            json_str = data.read()
            print(json_str)
            info_json = json.loads(json_str)
            configure.host = info_json["host"]
            configure.port = info_json["port"]
            configure.session = info_json["session"]
            configure.authKey = info_json["authKey"]
            configure.qq = info_json["qq"]
            configure.receiveTime = info_json["receiveTime"]
            configure.done = True
            configure.jiChou = info_json["jiChou"]
        except:
            print("configure_json错误")
        

    def upDataSession(self,session):
        configure.session = session