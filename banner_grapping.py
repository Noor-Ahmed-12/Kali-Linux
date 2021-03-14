#!/usr/bin/python3
import socket

#A 'socket()' provides a way for two computer nodes to communicate with each other. 
#Usually, one is a server and one is a client.

s=socket.socket();

#We then use the connect() method from the socket module 
#to make a network connection to a particular IP and port.
s.connect( ("192.168.19.1",22) );

#Here, we use the receive method recv to read 1024 bytes of data from the socket 
#and store them in a variable named answer ; these 1024 bytes will contain the banner information.

answer=s.recv(1024)

#then we print that information into screen
print(answer)

#and close the connection
s.close()


