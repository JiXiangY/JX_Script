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

# -------------------------------82311 113746
# init
allDataArr = [] #单个项目的数组
maxPage = 0
setPro_id = ''
fileName = ''

def getRankings(pro_id, page_index):
    url = 'http://mapi.modian.com/v45/product/comment_list?json_type=1&moxi_post_id=' + str(moxi_post_id) +'&page_index=' + str(page_index) + '&page_rows=10&pro_id='+str(pro_id)

    print(url)
    response = requests.get(url).json()
    # print(response)
    if int(response['status']) == 0:
        dataArr = response['data']
        if len(dataArr) == 0:
            return
        for dic in dataArr:
            if dic['content'].endswith(" 元"):
                dic['content'] = strReplace(dic['content'])
            else:
                dic['content'] = '0'
        # print(dataArr)
        global allDataArr
        for samllDic in dataArr:
            for k in range(0, len(allDataArr)):
                dic = allDataArr[k]
                if int(dic['user_id']) == int(samllDic['user_id']):
                    dic['content'] = str(float(dic['content'])+float(samllDic['content']))
                    break
                if k == len(allDataArr)-1:
                    allDataArr.append(samllDic)
            if len(allDataArr) == 0:
                allDataArr.append(samllDic)

        if page_index < maxPage:
            getRankings(pro_id,page_index+10)


def strReplace(str):
    str2 = ''
    str2 = str.replace('支持了 ','')
    str2 = str2.replace(' 元', '')
    return str2



def write_data_to_excel():

    # 实例化一个Workbook()对象(即excel文件)
    wbk = xlwt.Workbook()
    # 新建一个名为Sheet1的excel sheet。此处的cell_overwrite_ok =True是为了能对同一个单元格重复操作。
    sheet = wbk.add_sheet('Sheet1',cell_overwrite_ok=True)
    # 遍历result中的没个元素。
    for i in range(0,len(allDataArr)):
        sheet.write(i, 0, allDataArr[i]['user_info']['username'])
        sheet.write(i, 1, int(allDataArr[i]['user_id']))
        sheet.write(i, 2, float(allDataArr[i]['content']))
    wbk.save(fileName+'.xls')

# init end

# ---------------------------------

# 填下面的两个东西
# maxPage = int(input('请输入要查询的订单最大数量：')) #最大数量 往多了填就行 添太多慢一点
maxPage = 100000
setPro_id = int(input('请输入要查询的项目号：')) #订单编号 78021

fileName = input('请输入要生成的文件名（不需要后缀）：') #文件名
try:
    url = 'http://mapi.modian.com/v45/refresh/product_info_rt?&client=2&json_type=1&pro_id=' + str(setPro_id)
    response = requests.get(url).json()
    moxi_post_id = response['data']['product_info']['moxi_post_id']
except IOError:
    moxi_post_id = input('错误，请手动输入post_id:') #post_id

getRankings(setPro_id,0)
print(allDataArr)
write_data_to_excel()
