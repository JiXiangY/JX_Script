# -*- coding: UTF-8 -*-
import time
import threading
from Configure_Info import configure
from GetMessage import getMessage
from SendMessage import sendMessage
from Verification import verify
from receiveMessage import receiveMessage


def main():
	#初始化配置文件
	configure()
	#获取参数 验证
	verify.verify_session()
	#创建接收
	receive = receiveMessage()
	receive.run()


if __name__ == "__main__":
	main()