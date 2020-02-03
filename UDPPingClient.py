from socket import *
import time
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for ping in range(10):
    try:
        message = f"This is Ping {ping} {time.ctime()}"
        t = time.time()
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())
        print(time.time() - t)
    except timeout as e:
        print(e)
clientSocket.close()
