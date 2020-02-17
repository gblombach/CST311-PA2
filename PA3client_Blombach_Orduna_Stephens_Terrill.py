# Programming Assignment #3
# Blombach, Chicas-Terrill, Orduna, Stephens
# TCPChatClient.py
# February 18, 2020

from socket import *
from threading import Thread

# variables
serverName = 'localhost'
serverPort = 12021
messageSize = 1024
encoding ='utf8'

def receiveMessage():
    while True:
        try:
            message = clientSocket.recv(messageSize)
            print(message.decode())
        except Exception as e:
            print(e)
            break

def sendMessage(event=None):
    clientSocket.send(bytes(message,encoding))
    if message == 'bye':
        clientSocket.close

def onClose(event=None):
    message ='bye'
    sendMessage()
               

if __name__ == '__main__':

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    receiveThread = Thread(target=receiveMessage)
    receiveThread.start()
    
    while True:
        message = input('')
        sendMessage()
        
    #clientSocket.close()
    
