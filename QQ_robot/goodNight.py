from PIL import Image, ImageDraw, ImageFont
from savePath import get_FilePath
import time 
from SendMessage import sendMessage
from Configure_Info import configure
import requests
import random

class goodNightClass():
	# def __init__(self,messageArr):
	# 	self.time= '123' #时间
	# 	self.messageArr = messageArr # 晚安式队列
	# 	self.goodNightKey = "#是一个长一点的晚安式呢#"
	def __init__(self):
		self.messageArr = [] # 晚安式队列
		self.time= '' #时间
		self.goodNightKey = '' #晚安式 关键词
		self.save = False    #是否保存晚安式
		self.group_id = ""
		self.keyWord = "晚安式指令介绍\n\
1.开启指令\n\
	晚安式#题目#开启\n\
	启动晚安式并记录题目的消息\n\
2.截止指令\n\
	晚安式#截止\n\
	停止记录晚安式消息\n\
3.出图指令\n\
	晚安式#出图\n\
	输出一张晚安式图\n\
4.清空指令\n\
	晚安式#清空\n\
	清空记录内容\n\
5.删除指令\n\
	晚安式#name#删除\n\
6.帮助指令\n\
	晚安式#help\n\
	指令介绍"


	#启动晚安式记录
	def start_saveMeeage(self,goodNightKey):
		self.time =  time.strftime("%Y-%m-%d" ,  time.localtime())
		self.save = True
		self.messageArr = []
		self.goodNightKey = goodNightKey
		self.create_goodNightOtherMessage("启动记录晚安式{}".format(self.goodNightKey))
	#停止晚安式记录
	def stop_saveMessage(self):
		self.save = False
		self.create_goodNightOtherMessage("已停止记录")

	#清空晚安式 并关闭
	def remove_allMessage(self):
		self.create_goodNightOtherMessage("记录已清空")
		self.time = ''
		self.messageArr = []
		self.goodNightKey = ''
		self.group_id = ""
		

	#前缀为 "晚安式"
	#判断是否指令 
	def judge_goodNightMessageWithMessage(self,messageDic):
		group_id = messageDic["sender"]["group"]["id"]
		sende_id = messageDic["sender"]["id"]
		messageChain = messageDic["messageChain"]
		# if send_id != 443142362:
		# 	return
		#处理消息
		self.group_id = group_id
		for item in messageChain:
			if item["type"] == "Plain":
				text = item["text"]
				sub_arr = text.split('#')
				if len(sub_arr)== 3 and sub_arr[0] == "晚安式":
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
						imagePath  = self.drow_goodNightImage()
						self.create_goodNightImageMessage(imagePath)
						print("晚安式#出图")
						return True
					if sub_arr[1] == "清空":
						self.remove_allMessage()
						print("晚安式#清空")
						return True
					if sub_arr[1] == "help":
						self.create_goodNightOtherMessage(self.keyWord)
						print("晚安式#help")
						return True
				elif text.startswith(self.goodNightKey):
					self.add_goodNightMessageWithMessage(messageDic)
					print("晚安式#增加数据")
					return True
		return False
				
		
	#添加消息到晚安式队列
	def add_goodNightMessageWithMessage(self,messageDic):
		print("-----------------------")
		if self.save == True:
			sender = messageDic["sender"]
			qqID = sender["id"]
			del_Index = 99999
			#删除旧数据
			for index in range(len(self.messageArr)):
				oldItem = self.messageArr[index]
				if oldItem["id"] == qqID:
					del_Index = index
					break
			if del_Index < len(self.messageArr):
				self.messageArr.pop(del_Index)
			else:
				goodNightClass.downLoad_headImage(qqID)
			#添加新数据
			item = {}
			item["id"] = qqID
			item["name"] = sender["memberName"]
			messageChain = messageDic["messageChain"]
			for cell in messageChain:
				if cell["type"] == "Plain":
					text = cell["text"]
					item["text"] = text
					break
			self.messageArr.append(item)
			print("晚安式 {} 添加成功".format(item["name"]))

				
	#清除某条数据
	def remove_MessageWithName(self,name):
		print("-----------------------")
		del_index = 99999
		for index in range(len(self.messageArr)):
			oldItem = self.messageArr[index]
			if oldItem["name"] == name:
				del_Index = index
				break
		if del_Index < len(self.messageArr):
			self.messageArr.pop(del_Index)
		print("晚安式 {} 删除成功".format(name))


	
	#绘制晚安式
	def drow_goodNightImage(self):
		print("-----------------------")
		print(self.messageArr)
		#计算高度
		fontPath = get_FilePath.get_sourePath("Hiragino Sans GB.ttc")
		sum_Height = 0
		for item in self.messageArr:
			label = ImgText(item["text"],750)
			labelImg = label.draw_text()
			width,height = labelImg.size #获取图片大小
			sum_Height += 118 + height + 63

		#随机一个头图
		weiboList = get_FilePath.get_weiboPathList()
		rand = random.randint(0,len(weiboList)-1)
		weiboPath = get_FilePath.get_weiboImagePath(weiboList[rand])
		photo = Image.open(weiboPath)
		w, h = photo.size
		newH = int(1080 / w * h)
		photo =photo.resize((1080, newH),Image.ANTIALIAS)
		

		#画背景图
		sum_Height += newH #头图高度
		sum_Height += 150 #底图高度
		goodNight_Img = Image.new('RGBA', (1080, sum_Height), "#FFFFFF")
		goodNight_draw = ImageDraw.Draw(goodNight_Img)
		#画上头图
		photoBox = (0,0,1080,newH) #左上右下
		goodNight_Img.paste(photo, photoBox)
		
		

		#画上晚安式
		titlePath = get_FilePath.get_sourePath("Hiragino Sans GB.ttc")
		titleFont = ImageFont.truetype(titlePath, 60,index=2) #定义文字字体及字号，这里用你自己电	脑本地的字体
		titleSize = goodNight_draw.multiline_textsize(self.goodNightKey, titleFont)
		#画个半透明图
		
		box_image =  Image.new('RGBA', (titleSize[0]+100, titleSize[1]+40), (255,255,255,128))
		box_box = (int((1080-titleSize[0])/2-50), newH - 120 ,int((1080-titleSize[0])/2-50)+titleSize[0]+100, int(newH - 120+titleSize[1]+40))
		goodNight_Img.paste(box_image, box_box,box_image)
		titleBox = ((1080-titleSize[0])/2, newH -105 )
		goodNight_draw.text(titleBox, self.goodNightKey, font=titleFont, fill='#FFFF80',align="center") #文字写入图片


		#中间部分
		nextY = newH
		index = 0
		for item in self.messageArr:
			#名字
			nameFont = ImageFont.truetype(fontPath, 35,index=2)
			goodNight_draw.text((270, nextY+54),item["name"] , fill=("#24253D"), font=nameFont)
			#文本
			label = ImgText(item["text"],750)
			text_img = label.draw_text()
			width,height = text_img.size #获取图]片大小
			box = (270, nextY + 118, 270+width,nextY + 118 + height )#左上右下x,y,y+height,x_width
			goodNight_Img.paste(text_img, box)
			#头像
			head_image_path = get_FilePath.judge_saveGoodNightPath("{}.png".format(item["id"]))
			head_image = Image.open(head_image_path)
			if len(head_image_path) == 0:
				head_image = Image.new('RGBA', (156, 156), (255, 255, 0, 1))
			head_image =head_image.resize((156, 156),Image.ANTIALIAS)
			w, h = head_image.size
			alpha_layer = Image.new('L', (w, w), 0)
			draw = ImageDraw.Draw(alpha_layer)
			draw.ellipse((0, 0, w, w), fill=255)
			goodNight_Img.paste(head_image, (57, nextY + 25), alpha_layer)
			#画线
			nextY += 118 + height + 63
			goodNight_draw.line((57, nextY,1080 - 57 * 2,nextY), fill="#E0E0E1", width=2)
			index = index + 1
		#底图
		footPath = get_FilePath.get_sourePath("Hiragino Sans GB.ttc")
		footFont = ImageFont.truetype(footPath, 60,index=2) #定义文字字体及字号，这里用你自己电	脑本地的字体
		footSize = goodNight_draw.multiline_textsize("- 李梓应援会 -", footFont)
		pos = ((1080-footSize[0])/2, nextY + 45 )
		goodNight_draw.text(pos, "- 李梓应援会 -", font=footFont, fill='#333333',align="center") #文字写入图片
		#保存文件
		imge_name = self.time + ".png"
		imagePath = get_FilePath.get_saveGoodNightPath(imge_name)
		goodNight_Img.save(imagePath) #保存图片
		return imagePath
	
	@staticmethod
	def downLoad_headImage(qqID):
		# http://q1.qlogo.cn/g?b=qq&nk=443142362&s=640 
		url = "http://q1.qlogo.cn/g?b=qq&nk={}&s=640".format(qqID)
		try:
			r = requests.get(url)
			imagePath = get_FilePath.get_saveGoodNightPath("{}.png".format(qqID))
			with open(imagePath,'wb') as f:
				f.write(r.content) 
			print("头像下载成功")	
		except:
			print("头像下载失败")
			imge =  Image.new('RGBA', (156, 156), "#FFFF00")
			imagePath = get_FilePath.get_saveGoodNightPath("{}.png".format(qqID))
			imge.save(imagePath,quality=50) #保存图片
	#发送图片消息
	def create_goodNightImageMessage(self,imagePath):

		json = sendMessage.upload_image(imagePath,"group")
		if json and json["url"]:
			message_json = {
				"sessionKey": configure.session,
				"target": self.group_id,
				"messageChain":[{ "type": "Image", "url":json["url"] }]
			}
			sendMessage.send_groupMsg(message_json)

	#发送其他消息
	def create_goodNightOtherMessage(self,message):
		message_json = {
			"sessionKey": configure.session,
			"target": self.group_id,
			"messageChain":[{ "type": "Plain", "text":message }]
		}
		sendMessage.send_groupMsg(message_json)
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

class ImgText:
	fontPath = get_FilePath.get_sourePath("Hiragino Sans GB.ttc")
	font = ImageFont.truetype(fontPath,30,index=1)
 
	def __init__(self, text,width):
		# 预设宽度 可以修改成你需要的图片宽度
		self.width = width
		# 文本
		self.text = text
		# 段落 , 行数, 行高
		self.duanluo,self.note_height, self.line_height = self.split_text()

	def get_duanluo(self, text):
		txt = Image.new('RGBA', (self.width , 1000), "#FFFFFF")
		draw = ImageDraw.Draw(txt)
		duanluo = ""   # 所有文字的段落
		sum_width = 0  # 宽度总和
		line_count = 1 # 几行
		line_height = 0# 行高
		for char in text:
			width, height = draw.textsize(char, ImgText.font)
			sum_width += width
			if sum_width > self.width: # 超过预设宽度就修改段落 以及当前行数
				line_count += 1
				sum_width = width
				duanluo += '\n'
			duanluo += char
			line_height = max(height, line_height)
		if not duanluo.endswith('\n'):
			duanluo += '\n'
		return duanluo, line_height, line_count	

	def split_text(self):
		# 按规定宽度分组
		max_line_height = 0
		total_lines = 0
		allText = []
		for text in self.text.split('\n'):
			duanluo, line_height, line_count = self.get_duanluo(text)
			max_line_height = max(line_height, max_line_height)
			total_lines += line_count
			allText.append((duanluo, line_count))
		line_height = max_line_height
		total_height = total_lines * line_height
		return allText, total_height, line_height

	def draw_text(self):

		note_img = Image.new('RGBA', (self.width+100, self.note_height), "#FFFFFF")
		draw = ImageDraw.Draw(note_img)
		# 左上角开始
		x, y = 0, 0
		for duanluo, line_count in self.duanluo:
			draw.text((x, y), duanluo, fill=(96,97,111), font=ImgText.font,spacing = 5)
			y += self.line_height * line_count
		return note_img
		# imagePath = get_FilePath.get_saveImagePath("test.png")
		# note_img.save(imagePath) #保存图片


# n = ImgText("就在这时，随着他身心的调和，一个个记忆片段突兀跳出，缓慢呈现于他的脑海之中！\n克莱恩.莫雷蒂，北大陆鲁恩王国阿霍瓦郡廷根市人，霍伊大学历史系刚毕业的学生……\n父亲是皇家陆军上士，牺牲于南大陆的殖民冲突，换来的抚恤金让克莱恩有了进入私立文法学校读书的机会，奠定了他考入大学的基础……",750)
# n.draw_text()

# goodNightClass.downLoad_headImage(443142362)
# messageArr = [{'id': 443142362, 'name': '吉祥小哥哥', 'text': '#名字# 晚安式内容1'},{'id': 443142362, 'name': '吉祥小哥哥', 'text': '貌似没有，只有不小心睡着，醒来准备上班发现手机没充电已经自动关机了,貌似没有，只有不小心睡着，醒来准备上班发现手机没充电已经自动关机了,貌似没有，只有不小心睡着，醒来准备上班发现手机没充电已经自动关机了,貌似没有，只有不小心睡着，醒来准备上班发现手机没充电已经自动关机了'},{'id': 443142362, 'name': '吉祥小哥哥', 'text': '#名字# 晚安式内容3'}]
# good = goodNightClass(messageArr)
# good.drow_goodNightImage()


