#Socket

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_NET = ipv4 SOCK_Stream=port
s.connect((HOST,PORT))

# in KALI
#nc -nvlp 7777  Listening on 7777

