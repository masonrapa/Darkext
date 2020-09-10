from threading import Thread
from lib import fore, cls
from time import strftime
import socket
import sys
cls()
try:porto = sys.argv[1]
except: porto = input("[Set A Port] >> ")
try: address = sys.argv[2]
except: address = input("[IP:PORT] >> ")
cls()
def thread():
	while True:
		soc = socket.socket()
		host_name = "0.0.0.0"
		ip = socket.gethostbyname(host_name)
		port = int(porto)
		soc.bind((host_name, port))
		soc.listen(1)
		connection, addr = soc.accept()
		while True:
			message = connection.recv(1024)
			message = message.decode()
			if message != "":
				print (fore(244,30,30,strftime("%d/%m %H:%M:%S >> ")+message).go+fore(30,240,60,"").go)
				break

Thread(target = thread).start()
ip = str(address.split(":")[0])
port= int(address.split(":")[1])
while True:
	msg = input(fore(30,240,60,"").go)
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.connect((ip,port))
	s.send(msg.encode())
