# Programming Assignment #3
# Blombach, Chicas-Terrill, Orduna, Stephens
# TCPChatServer.py
# February 18, 2020

from socket import *
from threading import Thread
import collections

# variables
serverName = ''
serverPort = 12021
messageSize = 1024
clients = collections.OrderedDict()
encoding = 'utf8'
checkPoint = False
order =['X', 'Y']


# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))


# function for accepting connections to the server
def accept_connection():
    while True:
        client, client_address = serverSocket.accept()
        print('%s:%s has connected' % client_address)
        client.send(bytes('Connected to chat server. Enter your name and press enter.',encoding))
        Thread(target=client_chat, args=(client,client_address)).start()


# function for receiving messages from clients
def client_chat(client, client_address):
    name = client.recv(messageSize).decode()
    # store sockets in tuple
    clients[client] = name
    client.send(bytes('You are connected to chat. Type "bye" to quit.',encoding))
    message = 'System: %s has joined chat.' % name
    # send chat connection information to all clients
    broadcast(bytes(message,encoding))

    while True:
        global checkPoint
        message = client.recv(messageSize)
        if message != bytes('bye', encoding):
            # check who sent the message first
            # only when two people have been connected to the system
            if checkPoint == False and len(clients) == 2:
                checkPoint = True
                status_message = '*** ' + order[list(clients.values()).index(name)] + ': ' +\
                    name + ' received before ' + order[(list(clients.values()).index(name) + 1) % len(clients)] +\
                    ': ' + list(clients.values())[ (list(clients.values()).index(name) + 1) % len(clients)] + ' ***'
                # send status message to all clients
                broadcast(bytes(status_message,encoding))

            broadcast(message, name + ': ')
  
        else:
            client.send(bytes('System: Bye, ' + name,encoding))
            broadcast(bytes('System: %s has left chat.' % name,encoding))
            # close connection
            client.close()
            print('%s:%s has disconnected' % client_address)
            # remove client socket from list
            del clients[client]
            break


# function to broadcast messages to all connected clients
def broadcast(message,prefix=''):

    # send message to all clients
    for sockets in clients:
        sockets.send(bytes(prefix, encoding) + message)

    # send message to server too
    print((bytes(prefix, encoding) + message).decode())


# main function that establishes socket listener        
def main():

    serverSocket.listen(1)
    print('waiting for connections')
    new_thread = Thread(target=accept_connection)
    new_thread.start()
    new_thread.join()
    
    # close the connection
    serverSocket.close()


if __name__ == '__main__':
    main()

