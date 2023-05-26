#!/usr/bin/env python3

import socket

s = socket.socket()
s.connect(("10.10.10.1", 8888))

s.sendall("Leewack was here\n".encode())
s.close()
