import os


#Data文件夹生成文件夹 并返回路径
def save_folder(folder_name):
    path = os.getcwd()
    print('path = ' + path)
    folder_Path = path+"/Data/"+folder_name
    have_book = os.path.exists(folder_Path)
    if have_book == False:
        os.mkdir(folder_Path)
    return folder_Path

#获取图片保存路径
def get_saveImagePath(imageName):
    folder_Path = save_folder("Image")
    return folder_Path + "/" + imageName

#获取资源文件路径
def get_sourePath(file_name):
    path = os.getcwd()
    # print('path = ' + path)
    file_Path = path+"/Resource/"+file_name
    return file_Path

# print(get_sourePath("JiChou.jpg"))
