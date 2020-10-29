import requests,json
from Configure_Info import configure


class verify():
	#获取session
	@staticmethod
	def post_auth():
		header = {"Content-Type": "application/json"}
		url ="http://" + configure.host+ ":"+ configure.port + "/auth"
		body = {"authKey":configure.authKey}
		# print(url)
		response = requests.post(url,json=body,headers = header)
		response_json = response.json()
		# print(response_json)
		if response_json["code"] != 0:
			print(response_json)
		return response_json["session"]
	
	#认证session 和 qq
	@staticmethod
	def post_verify(session):

		header = {"Content-Type": "application/json"}
		url ="http://" + configure.host+ ":"+ configure.port + "/verify"
		body = {"sessionKey":session,"qq":configure.qq}
		# print(url)
		response = requests.post(url,json=body,headers = header)
		response_json = response.json()
		print(response_json)
		if response_json["code"] != 0:
			print("检验成功")
	
	#重新获取session 并认证
	@staticmethod
	def verify_session():
		session = verify.post_auth()
		confi = configure()
		confi.upDataSession(session)
		verify.post_verify(session)
	
