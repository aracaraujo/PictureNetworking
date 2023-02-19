import socket
from io import BytesIO
from PIL import Image

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("What picture do you want? ")
print("1. Car")
print("2. House")
print("3. Dog")
user_input = input("Number of choice: ")

message = bytes(user_input,'utf-8')

port = 40674

s.connect(('127.0.0.1', port))

s.sendall(message)

data = s.recv(1073741824)

stream = BytesIO(data)
image = Image.open(stream).convert("RGBA")
stream.close()
image.show()

s.close()