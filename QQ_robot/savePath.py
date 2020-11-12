import os

class get_FilePath():
	#Data文件夹生成文件夹 并返回路径
	@staticmethod
	def save_folder(folder_name):
		path = os.getcwd()
		print('path = ' + path)
		folder_Path = path+"/Data/"+folder_name
		have_book = os.path.exists(folder_Path)
		if have_book == False:
			os.mkdir(folder_Path)
		return folder_Path
	
	#获取图片保存路径
	@staticmethod
	def get_saveImagePath(imageName):
		folder_Path = get_FilePath.save_folder("Image")
		return folder_Path + "/" + imageName
	
	#获取资源文件路径
	@staticmethod
	def get_sourePath(file_name):
		path = os.getcwd()
		# print('path = ' + path)
		file_Path = path+"/Resource/"+file_name
		return file_Path	

	#获取微博图片文件路径
	@staticmethod
	def get_weiboPathList():
		path = os.getcwd()
		file_Path = path+"/weibo"
		file_list = os.listdir(file_Path)
		return file_list	
		#获取微博图片路径
	@staticmethod
	def get_weiboImagePath(imageName):
		path = os.getcwd()
		file_Path = path+"/weibo/" + imageName
		return file_Path	


	@staticmethod
	def get_imagePathList():
		folder_Path = get_FilePath.save_folder("Image")
		image_list = os.listdir(folder_Path)
		return image_list

	@staticmethod
	def get_goodNightPathList():
		folder_Path = get_FilePath.save_folder("GoodNight")
		image_list = os.listdir(folder_Path)
		return image_list
		#获取图片保存路径

	#判断晚安式图像是否存在 存在就返回路径 不存在返回空
	@staticmethod
	def judge_saveGoodNightPath(imageName):
		folder_Path = get_FilePath.save_folder("GoodNight")
		Path = folder_Path + "/" + imageName
		if os.path.exists(Path):
			return Path
		else:
			return ""

	#根据文件名返回路径 创建文件需要 所以不能返回空
	@staticmethod
	def get_saveGoodNightPath(imageName):
		folder_Path = get_FilePath.save_folder("GoodNight")
		Path = folder_Path + "/" + imageName
		return Path
# print(get_sourePath("JiChou.jpg"))


