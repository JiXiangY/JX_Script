from PIL import Image, ImageDraw, ImageFont
from savePath import get_FilePath
import time 
from SendMessage import sendMessage
from Configure_Info import configure


class goodNightClass():

	def __init__(self):
		self.time= '' #时间
		self.goodNightKey = '' #晚安式 关键词
		self.messageArr = [] # 晚安式队列
		self.save = False    #是否保存晚安式
		self.keyWord = [
			#晚安式指令介绍
			"开启",
			"截止",
			"出图",
			"清空",
			"删除"
		]

	#启动晚安式记录
	def start_saveMeeage(self,goodNightKey):
		self.time =  time.strftime("%Y-%m-%d" ,  time.localtime())
		self.save = True
		self.messageArr = []
		self.goodNightKey = goodNightKey

	#停止晚安式记录
	def stop_saveMessage(self):
		self.save = False
	
	#清空晚安式 并关闭
	def remove_allMessage(self):
		self.time = ''
		self.messageArr = []
		self.goodNightKey = ''

	#清除某条数据
	def remove_MessageWithName(self,name):
		print("remove_MessageWithName")
	#前缀为 "晚安式"
	#判断是否指令 

	def judge_goodNightMessageWithMessage(self,messageDic):
		group_id = messageDic["sender"]["group"]["id"]
		sende_id = messageDic["sender"]["id"]
		messageChain = messageDic["messageChain"]
		#处理消息
		for item in messageChain:
			if item["type"] == "Plain":
				text = item["text"]
				sub_arr = text.split('#')
				if len(sub_arr == 3):
					if sub_arr[2] == "开启":
						self.start_saveMeeage("#{}#".format(sub_arr[1]))
						print("晚安式#{}#开启".format(sub_arr[1]))
						return True
					if sub_arr[2] == "删除":
						self.remove_MessageWithName(sub_arr[1])
						print("晚安式#{}#删除".format(sub_arr[1]))
						return True
				elif len(sub_arr) == 2:
					if sub_arr[1] == "截止":
						self.stop_saveMessage()
						print("晚安式#截止")
						return True
					if sub_arr[1] == "出图":
						self.drow_goodNightImage()
						print("晚安式#出图")
						return True
					if sub_arr[2] == "清空":
						self.remove_allMessage()
						print("晚安式#清空")
						return True
				elif text.startswith(self.goodNightKey):
					self.add_goodNightMessageWithMessage(messageDic)
					print("晚安式#增加数据")
					return True
		return False
				
		
	#添加消息到晚安式队列
	def add_goodNightMessageWithMessage(self,messageDic):
		print("add_goodNightMessageWithMessage")
	
	#绘制晚安式
	def drow_goodNightImage(self):
		print("drow_goodNightImage")




#---------------------------下面是资料
#http://q1.qlogo.cn/g?b=qq&nk=443142362&s=640 QQ头像接口



# {
# "type": "GroupMessage",
# "messageChain":[
# {
# "type": "Source",
# "id": 15595,
# "time": 1605088073
# },
# {
# "type": "Plain",
# "text": "晚安式记录#晚安式#"
# }
# ],
# "sender":{"id": 443142362, "memberName": "吉祥小哥哥", "permission": "OWNER", "group":{"id": 628045903,…}
# }