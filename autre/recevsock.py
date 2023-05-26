#!/usr/bin/env python3
import socket

s = socket.socket()
s.bind(("0.0.0.0",8888))
s.listen()
conn, addr = s.accept()

print("Connection from", addr)
content = conn.recv(1024).decode()
print(content)