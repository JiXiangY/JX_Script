import socket

def connecthost(ip,port):
    sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk1.settimeout(5)
    try:
        sk1.connect((ip,port))
        return "端口开启"
    except Exception as e:
        return "端口关闭"
    sk1.close()
ret = connecthost('121.37.129.113',7890)
print(ret)