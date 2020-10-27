import requests,json
from Configure_Info import configure

#获取session
def post_auth():
    configure()
    header = {"Content-Type": "application/json"}
    url ="http://" + configure.host+ ":"+ configure.port + "/auth"
    body = {"authKey":configure.authKey}
    # print(url)
    response = requests.post(url,json=body,headers = header)
    response_json = response.json()
    # print(response_json)
    if response_json["code"] != "0":
        print(response_json)
    return response_json["session"]

#认证session 和 qq
def post_verify(session):
    configure()
    header = {"Content-Type": "application/json"}
    url ="http://" + configure.host+ ":"+ configure.port + "/verify"
    body = {"sessionKey":session,"qq":configure.qq}
    # print(url)
    response = requests.post(url,json=body,headers = header)
    response_json = response.json()
    print(response_json)
    if response_json["code"] != "0":
        print("检验成功")

#重新获取session 并认证
def verify_session():
    session = post_auth()
    confi = configure()
    confi.upDataSession(session)
    post_verify(session)
