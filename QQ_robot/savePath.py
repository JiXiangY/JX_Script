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

	@staticmethod
	def get_imagePathList():
		folder_Path = get_FilePath.save_folder("Image")
		image_list = os.listdir(folder_Path)
		return image_list

# print(get_sourePath("JiChou.jpg"))


