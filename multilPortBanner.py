#! /usr/bin/python3
import socket

ports=[21,22,25,3306]  #21(ftp) , 22(ssh) , 25(smtp) , 3306(mysql)

# 0 to 4 b/c we have 4 ports in list
for i in range(0,4):

  s=socket.socket()
  ports=ports[i]

print("this is the banner for the port:")

print(ports)

s.connect( ('192.168.19.1',ports) )

answer=s.recv(1024)

print(answer)

s.close()
