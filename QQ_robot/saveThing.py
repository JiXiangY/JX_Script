import os

def save(path):
    # 判断目录是否存在
    if not os.path.exists(os.path.split(path)[0]):
        # 目录不存在创建，makedirs可以创建多级目录
        os.makedirs(os.path.split(path)[0])
    try:
        # 保存数据到文件
        with open(path, 'wb') as f:
            f.write(html.encode('utf8'))
        print('保存成功')
    except Exception as e:
        print('保存失败', e)

def save_folder(folder_name):
    path = os.getcwd()
    print('path = ' + path)
    dataPath = path+"/Data/"+folder_name
    have_book = os.path.exists(dataPath)
    if have_book == False:
        os.mkdir(dataPath)

def get_saveImagePath():
    path = os.getcwd()
    save_folder("Image")

get_saveImagePath()

# path = path + "/" + "123"
# try:
#     print("1")
#     # r = requests.get(imageUrl)
#     # #保存图片
#     # with open('{}/{}.jpg'.format(path,imageName),'wb') as f:
#     #     f.write(r.content) 
#     # 
# except:
#     print("1")
#     # print("已下载图片 {} 失败 重新下载".format(imageName))