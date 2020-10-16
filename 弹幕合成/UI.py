#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time, datetime 
import threading
from tkinter import messagebox
import tkinter as tk          # 导入 Tkinter 库
import tkinter.filedialog
# 创建窗体
from tkinter import ttk
from DanMuHandle import danMu_handel
import os
import subprocess

window = tk.Tk()
window.title('弹幕视频合成(吉祥)')
window.geometry('500x300')
house_label = tk.Label(window, text='视频文件')
house_label.place(x=0, y=0, height=40, width=100)


video_name = ""
xml_name = "/Users/yujixiang/Downloads/20191205_223856.xml"
#视频文件选择
def open_video():
    filenames = tkinter.filedialog.askopenfilenames()
    if len(filenames) != 0:
        string_filename =""
        for i in range(0,len(filenames)):
            string_filename += str(filenames[i])
        videoLabel.config(text = string_filename)
        global video_name
        video_name = string_filename
        print(string_filename)
    else:
        videoLabel.config(text = "未选择视频文件")

videoLabel = tk.Label(window,text = '未选择视频文件')
videoLabel.place(x=10, y=40, height=30, width=300)
videobtn = tk.Button(window,text="视频选择",command=open_video)
videobtn.place(x=350, y=40, height=30, width=100)

#XML文件选择
def open_xml():
    filenames = tkinter.filedialog.askopenfilenames()
    if len(filenames) != 0:
        string_filename =""
        for i in range(0,len(filenames)):
            string_filename += str(filenames[i])
        xmlLabel.config(text = string_filename)
        global xml_name
        xml_name = string_filename
        print(string_filename)
    else:
        videoLabel.config(text = "未选择XML文件")


xmlLabel = tk.Label(window,text = '未选择XML文件')
xmlLabel.place(x=10, y=80, height=30, width=300)
xmlbtn = tk.Button(window,text="xml选择",command=open_xml)
xmlbtn.place(x=350, y=80, height=30, width=100)


def start_handle():
    if os.path.exists(video_name) == False:
        tkinter.messagebox.showwarning('警告','视频文件错误')
        # return
    if os.path.exists(xml_name) == False:
        tkinter.messagebox.showwarning('警告','xml文件错误')
        return
    ass_name = danMu_handel(xml_name)
    time.sleep(1)
    if os.path.exists(ass_name) == False:
        tkinter.messagebox.showwarning('警告','ass文件错误')
        return
    try:
        # ffmpeg -i test.mp4 -vf subtitles=2.ass -vcodec libx264 out2.mp4
        command = "ffmpeg -i {} -vf subtitles={} -vcodec libx264 out.mp4".format(video_name,ass_name)
        cmd(command)
    except:
        tkinter.messagebox.showwarning('警告','ass文件错误')

def cmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    subp.wait(2)
    while subp.poll != 0:
        subp.communicate()    
    if subp.poll() == 0:
        print(subp.communicate()[1])
    else:
        print("失败") 


starbtn = tk.Button(window,text= "开始",command=start_handle)
starbtn.place(x=200, y=120, height=30, width=100)



window.mainloop()                 # 进入消息循环