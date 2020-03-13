
import socket
import os
import subprocess

s = socket.socket()
host = '10.6.17.81'
port = 9995

s.connect((host, port))
print("Voila! You are connected to " + host  )

while True:
    data = s.recv(1024)
    
    if len(data) > 0:
        output_str = 'Done!! You are good to go!!'
        s.send(str.encode(output_str))
        data = s.recv(1024) 
        q1 = input(data.decode("utf-8"))
        s.send(str.encode(q1))
        data = s.recv(1024)
        q2 = input(data.decode("utf-8"))
        s.send(str.encode(q2))
        data = s.recv(1024)
        q3 = input(data.decode("utf-8"))
        s.send(str.encode(q3))
        data = s.recv(1024)
        q4 = input(data.decode("utf-8"))
        s.send(str.encode(q4))  
        print(output_str)