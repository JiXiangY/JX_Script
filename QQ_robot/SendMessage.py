import requests,json
from Configure_Info import configure
from requests_toolbelt import MultipartEncoder

class sendMessage():

	#发送群聊消息
	@staticmethod
	def send_groupMsg(message):
		header = {"Content-Type": "application/json"}
		url ="http://" + configure.host+ ":"+ configure.port + "/sendGroupMessage"
		body = message
		# print(url)
		response = requests.post(url,json=body,headers = header)
		response_json = response.json()
		# print(response_json)
		if response_json["code"] != 0:
			print(response_json)
			print("消息发送失败")
	
	#好友消息
	@staticmethod
	def send_friendMessage(message):
		header = {"Content-Type": "application/json"}
		url ="http://" + configure.host+ ":"+ configure.port + "/sendFriendMessage"
		body = message
		# print(url)
		response = requests.post(url,json=body,headers = header)
		response_json = response.json()
		# print(response_json)
		if response_json["code"] != 0:
			print(response_json)
			print("消息发送失败")
	
	#临时消息
	@staticmethod
	def send_tempMessage(message):
		header = {"Content-Type": "application/json"}
		url ="http://" + configure.host+ ":"+ configure.port + "/sendTempMessage"
		body = message
		# print(url)
		response = requests.post(url,json=body,headers = header)
		response_json = response.json()
		# print(response_json)
		if response_json["code"] != 0:
			print(response_json)
			print("消息发送失败")
	
	
	
	#上传照片
	# 使用此方法上传图片文件至服务器并返回ImageId
	# sessionKey	String	false	YourSession	已经激活的Session
	# type	String	false	"friend "	"friend" 或 "group" 或 "temp"
	# img	File	false	-	图片文件
	# 返回 图片json 
	# {
	# imageId": "/1010892170-163329470-7788980469032B425A3365C876FBBBC1",
	# "url": "http://c2cpicdw.qpic.cn/offpic_new/1010892170//1010892170-163329470-7788980469032B425A3365C876FBBBC1/0?term=2",
	# "path": "C:\\Users\\Administrator\\Desktop\\mirai_3\\.\\data\\MiraiApiHttp\\images\\1.jpg"
	# }
	@staticmethod
	def upload_image(img_path,type):
		header = {"Content-Type":"multipart/form-data"}
		url ="http://" + configure.host+ ":"+ configure.port + "/uploadImage"
		img = open(img_path, "rb")# 以2进制方式打开图片
		imageType = "image/jpeg"
		img_name =  "temp.jpg"
		if img_path.endswith('.png'):
			imageType =  "image/png"
			img_name =  "temp.png"
		body = MultipartEncoder({
		"sessionKey":configure.session,
		"img":(img_name,img,imageType),
		"type":type
		})
		#🌿🌿🌿🌿🌿🌿🌿🌿请求头 太尼玛恶心了 这里卡了好几个小时 标记一下 🌿🌿🌿🌿🌿🌿🌿🌿🌿
		header['Content-Type'] = body.content_type
		response = requests.post(url,data = body,headers = header)
		response_json = response.json()
		print(response_json)
		img.close()
		if response_json and len(response_json["url"]) > 0:
			return response_json
	
	
	@staticmethod
	def upload_imageData(img,type):
		header = {"Content-Type":"multipart/form-data"}
		url ="http://" + configure.host+ ":"+ configure.port + "/uploadImage"
		body = MultipartEncoder({
			"sessionKey":configure.session,
			"img":("temp.png",img,"image/png"),
			"type":type
		})
		header['Content-Type'] = body.content_type
		response = requests.post(url,data = body,headers = header)
		response_json = response.json()
		print(response_json)
		img.close()
		if len(response_json["url"]) > 0:
			return response_json

	# upload_image("/Users/yujixiang/Desktop/","300.jpg","group")
	#上传语音
	# 使用此方法上传图片文件至服务器并返回ImageId
	# sessionKey	String	false	YourSession	已经激活的Session
	# type	String	false	group
	# voice	File	false	-	图片文件
	# 返回 音频json 
	# {
	#	 "voiceId": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.amr", //语音的VoiceId
	#	 "url": "xxxxxxxxxxxxxxxxxxxx",
	#	 "path": "xxxxxxxxxx"
	# }
	@staticmethod
	def upload_voice(voice_path,voice_name):
		header = {"Content-Type":"multipart/form-data"}
		url ="http://" + configure.host+ ":"+ configure.port + "/uploadVoice"
		voice = open(voice_path + voice_name, "rb")# 以2进制方式打开图片
		body = MultipartEncoder({
		"sessionKey":configure.session,
		"voice":(voice_name,voice,"audio/amr"),
		"type":"group"
		})
		#🌿🌿🌿🌿🌿🌿🌿🌿请求头 太尼玛恶心了 这里卡了好几个小时 标记一下 🌿🌿🌿🌿🌿🌿🌿🌿🌿
		header['Content-Type'] = body.content_type
		response = requests.post(url,data = body,headers = header)
		response_json = response.json()
		print(response_json)
		voice.close()
		if response_json["url"]:
			return response_json
	
	# upload_voice("/Users/yujixiang/Desktop/","temp.Amr")
				