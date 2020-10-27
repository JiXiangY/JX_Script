import requests,json
from Configure_Info import configure

def send_groupMsg(message):
    configure()
    header = {"Content-Type": "application/json"}
    url ="http://" + configure.host+ ":"+ configure.port + "/sendGroupMessage"
    body = message
    # print(url)
    response = requests.post(url,json=body,headers = header)
    response_json = response.json()
    # print(response_json)
    if response_json["code"] != "0":
        print(response_json)
        print("消息发送失败")

#好友消息
def send_friendMessage(message):
    configure()
    header = {"Content-Type": "application/json"}
    url ="http://" + configure.host+ ":"+ configure.port + "/sendFriendMessage"
    body = message
    # print(url)
    response = requests.post(url,json=body,headers = header)
    response_json = response.json()
    # print(response_json)
    if response_json["code"] != "0":
        print(response_json)
        print("消息发送失败")

#临时消息
def send_tempMessage(message):
    configure()
    header = {"Content-Type": "application/json"}
    url ="http://" + configure.host+ ":"+ configure.port + "/sendTempMessage"
    body = message
    # print(url)
    response = requests.post(url,json=body,headers = header)
    response_json = response.json()
    # print(response_json)
    if response_json["code"] != "0":
        print(response_json)
        print("消息发送失败")



#上传照片
# 使用此方法上传图片文件至服务器并返回ImageId
# sessionKey	String	false	YourSession	已经激活的Session
# type	String	false	"friend "	"friend" 或 "group" 或 "temp"
# img	File	false	-	图片文件
def upload_image(img_path,img_name,type):
    configure()
    header = {"Content-Type": "multipart/form-data"}
    url ="http://" + configure.host+ ":"+ configure.port + "/uploadImage"
    # try:
        
    # except:
        
    with open(img_path + img_name, "rb")as f_abs:# 以2进制方式打开图片
        body = {
        #
        "sessionKey":configure.session,
        "img":(img_name, f_abs, "image/jpeg"),
        # 图片的名称、图片的绝对路径、图片的类型（就是后缀）
        "type":type
        }
        # 上传图片的时候，不使用data和json，用files
        response = requests.post(url=url, files=body,headers = header).json
        response_json = response.json()
        print(response)
        if response_json["code"] != "0":
            print(response_json)
            print("消息发送失败")


upload_image("/Users/yujixiang/Desktop/","002Po4pSly1gjk0idcodbj60s71030x002.jpg","friend")