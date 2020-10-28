import requests,time,random,json,re,os,sys
from Configure_Info import configure


##-------------------------------------获取消息-----------------------------------###
# 获取Bot收到的消息和事件
# 使用此方法获取bot接收到的最老消息和最老各类事件(会从MiraiApiHttp消息记录中删除)
def get_fetchMessage():
    configure()
    url ="http://" + configure.host+ ":"+ configure.port + "/fetchMessage?sessionKey="+ configure.session + "&count=10"
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    msg_arr = []
    if response_json['code'] == "3":
        print("session已失效,重新验证")
        return
    if response_json['code'] == "0":
        msg_arr = response_json["data"]
        return msg_arr
    if response_json['code'] == "1":
        print("错误的auth key")
        return
    return 

# 使用此方法获取bot接收到的最新消息和最新各类事件(会从MiraiApiHttp消息记录中删除)
def get_fetchLatestMessage():
    configure()
    url ="http://" + configure.host+ ":"+ configure.port + "/fetchLatestMessage?sessionKey="+ configure.session + "&count=10"
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    msg_arr = []
    if response_json['code'] == "3":
        print("session已失效,重新验证")
        return
    if response_json['code'] == "0":
        msg_arr = response_json["data"]
        return msg_arr
    if response_json['code'] == "1":
        print("错误的auth key")
        return
    return 



# 使用此方法获取bot接收到的最老消息和最老各类事件(不会从MiraiApiHttp消息记录中删除)
def peekLatestMessage():
    configure()
    url ="http://" + configure.host+ ":"+ configure.port + "/peekMessage?sessionKey="+ configure.session + "&count=10"
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    msg_arr = []
    if response_json['code'] == "3":
        print("session已失效,重新验证")
        return
    if response_json['code'] == "0":
        msg_arr = response_json["data"]
        return msg_arr
    if response_json['code'] == "1":
        print("错误的auth key")
        return
    return 


# 使用此方法获取bot接收到的最新消息和最新各类事件(不会从MiraiApiHttp消息记录中删除)
def get_peekMessage():
    configure()
    url ="http://" + configure.host+ ":"+ configure.port + "/peekLatestMessage?sessionKey="+ configure.session + "&count=10"
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    msg_arr = []
    if response_json['code'] == "3":
        print("session已失效,重新验证")
        return
    if response_json['code'] == "0":
        msg_arr = response_json["data"]
        return msg_arr
    if response_json['code'] == "1":
        print("错误的auth key")
        return
    return 