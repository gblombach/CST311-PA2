# Programming Assignment #3
# Blombach, Chicas-Terrill, Orduna, Stephens
# TCPChatClient.py
# February 18, 2020

from socket import *
from threading import Thread
import time

# variables
serverName = 'localhost'
serverPort = 12021
messageSize = 1024
encoding ='utf8'

# function to receive messages through client socket
def receiveMessage():
    while True:
        try:
            message = clientSocket.recv(messageSize)
            print(message.decode())
 
        except Exception as e:
            print(e)
            break

# function to send messages via client socket
def sendMessage(event=None):
    clientSocket.send(bytes(message).encode(encoding))


#def onClose(event=None):
    #message ='bye'
    #sendMessage()
               
# run main routine
if __name__ == '__main__':

    #setup client socket to server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    #create thread to receive messages via function
    receiveThread = Thread(target=receiveMessage)
    receiveThread.start()

    #loop keyboard input    
    while True:
        message = raw_input('')
        sendMessage()
        #if client wants to quit, then break loop
        if message == 'bye':
            time.sleep(3)
            break   
    #close connection
    clientSocket.close()
    
