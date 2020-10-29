
from PIL import Image, ImageDraw, ImageFont
from savePath import get_FilePath
import time 
from SendMessage import sendMessage
from Configure_Info import configure

class JiChou():

	@staticmethod
	def drow_JiChou(name):
		content = "今天\n" + name + "得罪了我\n记下来!" 
		#创建一个空白的图片，大小为300*200，背景为白色
		#image = Image.new(mode="RGB", size=(500,260), color=(255,255,255)) 
		imagePath = get_FilePath.get_sourePath("JiChou.jpg")
		
		image = Image.open(imagePath) #打开一张图片
		draw = ImageDraw.Draw(image)
		width,height = image.size #获取图片大小
		
		#字体
		fontPath = get_FilePath.get_sourePath("Hiragino Sans GB.ttc")
		imageFont = ImageFont.truetype(fontPath, 25,index=1) #定义文字字体及字号，这里用你自己电	脑本地的字体
	
		#下面三行是用来计算文字的位置，用来居中文字内容
		txtSize = draw.multiline_textsize(content, imageFont)
		pos_x = (width - txtSize[0]) / 2 if width > txtSize[0] else 0
		pos = (pos_x, 250)
	
		draw.text(pos, content, font=imageFont, fill='#000000',align="center") #文字写入图片
		location = name + time.strftime(" %Y-%m-%d %H:%M:%S" ,  time.localtime()) + ".png"
		imagePath = get_FilePath.get_saveImagePath(location)
		image.save(imagePath) #保存图片
		return imagePath
	
	
	# {
	#	 "sessionKey": "YourSession",
	#	 "target": 987654321,
	#	 "messageChain": [
	#		 { "type": "Plain", "text": "hello\n" },
	#		 { "type": "Plain", "text": "world" },
	# 	{ "type": "Image", "url": "https://i0.hdslb.com/bfs/album/	67fc4e6b417d9c68ef98ba71d5e79505bbad97a1.png" }
	#	 ]
	# }
	
	@staticmethod
	def create_JiChouMessage(name,send_to,send_type):
		imagePath = JiChou.drow_JiChou(name)
		time.sleep(1)
		json = sendMessage.upload_image(imagePath,send_type)
		if json and json["url"]:
			message_json = {
				"sessionKey": configure.session,
				"target": send_to,
				"messageChain":[{ "type": "Image", "url":json["url"] }]
			}
			sendMessage.send_groupMsg(message_json)


# configure()
# JiChou.create_JiChouMessage("北思","628045903","group")