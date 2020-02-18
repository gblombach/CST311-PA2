# Programming Assignment #3
# Blombach, Chicas-Terrill, Orduna, Stephens
# TCPChatServer.py
# February 18, 2020

from socket import *
from threading import Thread
import collections
import time

# variables
serverName =''
serverPort = 12021
messageSize = 1024
clients = collections.OrderedDict()
encoding ='utf8'
checkPoint = False
order =['X','Y']

# Create a TCP socket and bind to server port
# Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))

#function for accepting connections to the server   
def acceptConnection():
    while True:
        client, clientAddress = serverSocket.accept()
        print('%s:%s has connected' % clientAddress)
        client.send(bytes('Connected to chat server. Enter your name and press enter.').encode(encoding))
        Thread(target=clientChat, args=(client,clientAddress)).start()
        
#function for receiving messages from clients
def clientChat(client,clientAddress):
    name = client.recv(messageSize).decode()
    #store sockets in tuple
    clients[client] = name
    client.send(bytes('You are connected to chat. Type "bye" to quit.').encode(encoding))
    message = 'System: %s has joined chat.' % name
    #send chat connection information to all clients
    broadcast(bytes(message).encode(encoding))


    while True:
        #instantiate global variable
        global checkPoint
        #get message from client
        message = client.recv(messageSize)
        #if the message is not a disconnect request
        if message !=bytes('bye').encode(encoding):
            #check who sent the message first
            #only when two people have been connected to the system
            if checkPoint == False and len(clients) == 2:
                checkPoint = True
                statusMessage = '*** ' + order[list(clients.values()).index(name)] + ': ' +\
                    name + ' received before ' + order[(list(clients.values()).index(name) + 1) % len(clients)] +\
                    ': ' + list(clients.values())[ (list(clients.values()).index(name) + 1) % len(clients)] + ' ***'
                #send status message to all clients
                broadcast(bytes(statusMessage).encode(encoding))

                
            broadcast(message, name + ': ')

        #else disconnect
        else:
            client.send(bytes('System: Bye, ' + name).encode(encoding))
            broadcast(bytes('System: %s has left chat.' % name).encode(encoding))
            #close connection
            time.sleep(2)
            client.close()
            #log disconnect on server console
            print('%s:%s has disconnected' % clientAddress)
            #remove client socket from ordered list
            del clients[client]
            break

#function to broadcast messages to all connected clients
def broadcast(message,prefix=''):

    #send message to all clients
    for sockets in clients:
        sockets.send(bytes(prefix).encode(encoding)+ message)

    #send message to server too
    print((bytes(prefix).encode(encoding)+ message).decode())

# main function that establishes socket listener        
def Main():

    serverSocket.listen(1)
    print('waiting for connections')
    newThread = Thread(target=acceptConnection)
    newThread.start()
    newThread.join()
    
    #close the connection
    serverSocket.close()

#run main
if __name__ == '__main__':
    Main()             
    
    
        
                    
