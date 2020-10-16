# -*- coding: utf-8 -*-
import json
import xmltodict
import math
import random

def xml_Json(xmlstr):
    #parse是的xml解析器
    xmlparse = xmltodict.parse(xmlstr)
    #json库dumps()是将dict转化成json格式，loads()是将json转化成dict格式。
    #dumps()方法的ident=1，格式化json
    # jsonstr = json.dumps(xmlparse,indent=1)
    # print(jsonstr)
    i = xmlparse['i']
    d = i['d']
    return d

def open_file(fileName):
    fo = open(fileName, "r")
    xml = fo.read()
    return xml

def write_file(danMu_list,oldFileName):

    fileName = oldFileName[:-4] + ".ass"
    fo = open(fileName, "ab+")
    fo.write(('[Script Info]'+"\r\n").encode('UTF-8'))
    fo.write(('[Title: bilibili ASS 弹幕在线转换'+"\r\n").encode('UTF-8'))
    fo.write(('Original Script:{}\r\n'.format(oldFileName)).encode('UTF-8'))
    fo.write(('ScriptType: v4.00+\r\n').encode('UTF-8'))
    fo.write(('Collisions: Normal\r\n').encode('UTF-8'))
    fo.write(('PlayResX: 560\r\n').encode('UTF-8'))
    fo.write(('PlayResY: 420\r\n').encode('UTF-8'))
    fo.write(('Timer: 10.0000\r\n').encode('UTF-8'))
    fo.write(('\r\n').encode('UTF-8'))
    fo.write(('[V4+ Styles]\r\n').encode('UTF-8'))
    fo.write(('Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\r\n').encode('UTF-8'))
    fo.write(('Style: Fix,Microsoft YaHei,25,&H66FFFFFF,&H66FFFFFF,&H66000000,&H66000000,1,0,0,0,100,100,0,0,1,2,0,2,20,20,2,0\r\n').encode('UTF-8'))
    fo.write(('Style: R2L,Microsoft YaHei,25,&H66FFFFFF,&H66FFFFFF,&H66000000,&H66000000,1,0,0,0,100,100,0,0,1,2,0,2,20,20,2,0\r\n').encode('UTF-8'))
    fo.write(('\r\n').encode('UTF-8'))
    fo.write(('[Events]\r\n').encode('UTF-8'))
    fo.write(('Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\r\n').encode('UTF-8'))
    lasttime = 0
    lastY = 25
    for index in range(len(danMu_list)):

        old_item = danMu_List[index]
        old_style = old_item["@p"]
        old_text = old_item["#text"]
        styleList = old_style.split(',')
        time = float(styleList[0])
        #时间转换
        startTime = time_handle(time)
        entTime = time_handle(time+10)
        x1 = random.randint(560,950)
        x2 = random.randint(-300,-100)
        Y = 0
        maxY = 75
        if int(styleList[8]) == 1:
            maxY = 420
        if(time - lasttime > 5):
            Y = 25
            lastY = 25
        else:
            Y = lastY + 25
            if(Y > maxY):
                Y = 25
                lastY = 25
            else:
                lastY = Y
        lasttime = time
        new_item = "Dialogue: 0,"+startTime+","+entTime+",R2L,,20,20,2,,{"+"\move({},{},{},{})".format(x1,Y,x2,Y)+'}'+old_text
        fo.write((new_item+"\r\n").encode('UTF-8'))
        print(new_item)
    fo.close()
    print("完成")


def time_handle(time):
    hour = 0
    min = 0
    s = 0
    hourStr = ''
    minStr = ''
    sStr = ''
    if(time>3600):
        hour = math.floor(time/3600)
        time = time - 3600 * hour
        if hour > 10:
            hourStr = str(hour)
        else:
            hourStr = "0" + str(hourStr)
    else:
        hourStr = "00"

    if(time > 60):
        min = math.floor(time/60)
        s = time - min * 60
        sStr = str(round(s,2))
        if min >= 10:
            minStr = str(min)
        else:
            minStr = "0" + str(min)
    else:
        minStr = "00"
        sStr = str(round(time,2))
    return hourStr + ":" + minStr + ":" + sStr


fileName = "20191205_223856.xml"
xml = open_file(fileName)
danMu_List = xml_Json(xml)
write_file(danMu_List,fileName)