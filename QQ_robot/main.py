# -*- coding: UTF-8 -*-
import time
import threading
from Configure_Info import configure
from GetMessage import *
from SendMessage import *
from Verification import *

def main():
    configure()
    verify_session()
    upload_image("/Users/yujixiang/Desktop/","002Po4pSly1gjk0idcodbj60s71030x002.jpg","friend")
    # p = threading.Thread(target = absd, args = (3,))
    # p.start()


if __name__ == "__main__":
    main()