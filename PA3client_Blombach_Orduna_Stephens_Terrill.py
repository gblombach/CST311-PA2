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
encoding = 'utf8'


def receive_message():
    while True:
        try:
            message = clientSocket.recv(messageSize)
            print(message.decode())
        except Exception as e:
            print(e)
            break


def send_message(event=None):
    clientSocket.send(bytes(message,encoding))
    if message == 'bye':
        clientSocket.close


def on_close(event=None):
    message = 'bye'
    send_message()
               

if __name__ == '__main__':

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    receiveThread = Thread(target=receive_message)
    receiveThread.start()
    
    while True:
        message = input('')
        send_message()
        
    # clientSocket.close()
