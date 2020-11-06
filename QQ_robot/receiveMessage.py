import sched
import time
from datetime import datetime
from GetMessage import getMessage
import threading
from Configure_Info import configure
from Verification import verify
from drowImage import drowEmoji
class receiveMessage():
	def __init__(self):
		self.timePool = configure.receiveTime
		
	
	def run(self):
		timer = threading.Timer(self.timePool, self.time_Pool)
		timer.start()


	def time_Pool(self):
		# print(threading.current_thread())
		try:
			message_Arr = getMessage.get_fetchLatestMessage()
			if message_Arr == 3:
				verify.verify_session()#如果失效 重新验证
			
			if message_Arr and len(message_Arr) > 0 :
				print(message_Arr)
				for dic in message_Arr:
					self.handle_message(dic)
		except:
			print("消息处理错误")


		timer = threading.Timer(self.timePool, self.time_Pool)
		timer.start()

#------------------------消息处理 ---------------------------
	def handle_message(self,messageDic):
		#群聊消息
		if messageDic["type"] == "GroupMessage":
			group_id = messageDic["sender"]["group"]["id"]
			sende_id = messageDic["sender"]["id"]
			messageChain = messageDic["messageChain"]
			#处理消息
			for item in messageChain:
				if item["type"] == "Plain":
					text = item["text"]
					#记仇插件
					if self.JiChou_handel(text,sende_id,group_id,"group") == True:
						break



		
		#好友消息
		if messageDic["type"] == "FriendMessage":
			sende_id = messageDic["sender"]["id"]
			messageChain = messageDic["messageChain"]
			#处理消息
			for item in messageDic:
				print("好友消息")


#-----------------------------具体功能处理-----------------------------------------
	#处理记仇插件
	def JiChou_handel(self,text,sende_id,send_to,send_type):
		#判断是否启用插件
		if configure.jiChou == True:
			sub_arr = text.split('#')
			if sub_arr and len(sub_arr) == 2 and sub_arr[0] == "记仇" and len(sub_arr[1]) > 0:
				def jichou_worker(name,send_to,send_type):
					try:
						if sende_id != 443142362: #暂时自己使用
							drowEmoji.create_JiChouOtherMessage(name,send_to,send_type)
						else:
							drowEmoji.create_JiChouMessage(name,send_to,send_type)
						# drowEmoji.create_JiChouMessage(name,send_to,send_type)
					except:
						print("记仇失败")
				p = threading.Thread(target = jichou_worker, name = "消息发送",args=(sub_arr[1],send_to,send_type))
				p.start()
				return True
			if sub_arr and len(sub_arr) == 2 and sub_arr[0] == "羡慕" and len(sub_arr[1]) > 0:
				def xianmu_worker(name,send_to,send_type):
					try:
						if sende_id != 443142362: #暂时自己使用
							drowEmoji.create_JiChouOtherMessage(name,send_to,send_type)
						else:
							drowEmoji.create_XianMuMessage(name,send_to,send_type)
						# drowEmoji.create_XianMuMessage(name,send_to,send_type)
					except:
						print("羡慕失败")
				p = threading.Thread(target = xianmu_worker, name = "消息发送",args=(sub_arr[1],send_to,send_type))
				p.start()
				return True
		return False


