# -*- coding: utf-8 -*-
import requests
# import json
# 消去https请求的不安全warning
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import urllib
import hashlib
import time
import xlwt
import datetime
import re
from bs4 import BeautifulSoup  # 导入bs4库


# -------------------------------82311 113746
# init


req_header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'UM_distinctid=174d8f5f426177-001fcfc28f6f07-31687304-1fa400-174d8f5f4278a5; bcolor=; font=; size=; fontcolor=; width=; PPad_id_PP=3; CNZZDATA1262370505=957035894-1601363578-https%253A%252F%252Fwww.baidu.com%252F%7C1601368979',
    'Host': 'www.xsbiquge.com',
    'If-Modified-Since': ' Wed, 16 Sep 2020 04:08:39 GMT',
    'If-None-Match': 'W/"5f618fc7-1facd"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
}

item_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    ,'Accept-Encoding': 'gzip, deflate, br'
    ,'Accept-Language': 'zh-CN,zh;q=0.9'
    ,'Cache-Control': 'max-age=0'
    ,'Connection': 'keep-alive'
    ,'Cookie': 'UM_distinctid=174d8f5f426177-001fcfc28f6f07-31687304-1fa400-174d8f5f4278a5; bcolor=; font=; size=; fontcolor=; width=; CNZZDATA1262370505=957035894-1601363578-https%253A%252F%252Fwww.baidu.com%252F%7C1602487016; PPad_id_PP=1'
    ,'Host': 'www.xsbiquge.com'
    ,'If-Modified-Since': 'Mon, 30 Dec 2019 11:23:48 GMT'
    ,'If-None-Match': 'W/"5e09de44-3b1b"'
    ,'Sec-Fetch-Dest': 'document'
    ,'Sec-Fetch-Mode': 'navigate'
    ,'Sec-Fetch-Site': 'none'
    ,'Sec-Fetch-User': '?1'
    ,'Upgrade-Insecure-Requests': '1'
    ,'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}



txtID = ''  # 小说id
title = ''  # 小说名字
txtDic = {}
txt_list = []
fileName = ''
prefix_url = 'https://www.xsbiquge.com/' 
section_ct = 0
def getRankings(txtID):
    url = prefix_url + str(txtID)
    print(url)
    global req_header
    response = requests.get(url, params=req_header)
    print('encode ' + response.encoding)
    response.encoding = "gzip"
    print(response)
    soups = BeautifulSoup(response.text, 'lxml')  # html.parser是解析器，也可是lxml

    global txtDic
    txtDic['title'] = soups.select('#wrapper .box_con #maininfo #info h1')[0].text
    global title 
    title = txtDic['title']
    print(txtDic['title'])
    txtDic['author'] = soups.select('#wrapper .box_con #maininfo #info p')
    # 获取小说最近更新时间
    txtDic['update'] = txtDic['author'][2].text
    # 获取最近更新章节名称
    txtDic['lately'] = txtDic['author'][3].text
    # 获取小说作者
    txtDic['author'] = txtDic['author'][0].text
    # 获取小说简介
    txtDic['intro'] = soups.select('#wrapper .box_con #maininfo #intro')[
                                   0].text.strip()
    # 获取小说所有章节信息
    print(txtDic)
    global txt_list 
    txt_list = soups.select('#wrapper .box_con #list dl dd a')
    # print(txt_list)
    print('\n-------------------\n')
    # print(section_list)
    global section_ct 
    section_ct = len(txt_list)
    # 获取小说第一章页面地址
    first_page = txt_list[0]['href']
    print("小说章节页数："+str(section_ct))
    print("第一章地址寻找成功：" + first_page)
    # 打开小说文件写入小说相关信息
    global fileName 
    fileName = txtDic['title'] + '.txt'
    fo = open(fileName, "ab+")
    fo.write((txtDic['title']+"\r\n").encode('UTF-8'))
    fo.write((txtDic['author'] + "\r\n").encode('UTF-8'))
    fo.write((txtDic['update'] + "\r\n").encode('UTF-8'))
    fo.write((txtDic['lately'] + "\r\n").encode('UTF-8'))
    fo.write(("*******简介*******\r\n").encode('UTF-8'))
    fo.write(("\t"+txtDic['intro'] + "\r\n").encode('UTF-8'))
    fo.write(("\n\n------------\r\n\n").encode('UTF-8'))
    fo.close()
    down_text()
    

def write_data_to_txt(data):
    result2txt = str(data)          # data是前面运行出的数据，先将其转为字符串才能写入
    textName = str(fileName) + '.txt'
    with open(textName, 'a') as file_handle:   # .txt可以不自己新建,代码会自动新建
        file_handle.write(result2txt)     # 写入
        file_handle.write('\n')           # 有时放在循环里面需要自动转行，不然会覆盖上一条数据


def down_text():
    i = 0
    print(section_ct)
    while i < section_ct:
        try:
            section_num = txt_list[i]
            section_url = prefix_url + section_num['href']
            # 请求当前章节页面
            response = requests.get(section_url, params=item_header)
            # 新笔趣阁的编码格式为gbk
            response.encoding = 'gzip'
                # soup转换
            soup = BeautifulSoup(response.text, "html.parser")
                # 获取章节名称
            section_name = soup.select('#wrapper .content_read .box_con .bookname h1')[0]
            section_text = soup.select('#wrapper .content_read .box_con #content')[0]
            for ss in section_text.select("script"):  # 删除无用项
                ss.decompose()
            # 获取章节文本
            section_text = re.sub('\s+', '\r\n\t', section_text.text).strip('\r\n')#替换字符串 不太明白
            fo = open(fileName, "ab+")
            fo.write(("\n\n------------\r\n\n").encode('UTF-8'))
            # 以二进制写入章节题目
            fo.write(('\r'+section_name.text+'\r\n\n\n').encode('UTF-8'))
            
             # 以二进制写入章节内容
            fo.write((section_text).encode('UTF-8'))
            print(txtDic['title']+' 章节：'+section_name.text+'     已下载')
            # print(section_text.text.encode('UTF-8'))
            time.sleep(1)
            if i % 30 == 0:
                time.sleep(9)
            i += 1
        except:
            print("编号：" + "小说名：《"+txtDic['title']+"》 章节下载失败，正在重新下载。")
    fo.close()
    print("小说名：《"+txtDic['title']+"》 下载完成")


txtID = '15_15338'
getRankings(txtID)

