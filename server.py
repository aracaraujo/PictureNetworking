import socket
import io
from PIL import Image

# Creating server socket.
s = socket.socket()

# Assigning port.
port = 40674

# Binding server to the port.
s.bind(('',port))
print("socket binded to %s" %(port))

# Server start to listening for connections. It will allow up to 5 connections at a time.
s.listen(5)
print("socket is listening")


while True:
    # Accepting connections.
    c, addr = s.accept()
    print('Got connection from ', addr)
    
    # Receives the message from client.
    data = c.recv(1073741824)

    # Conveting the bytes of the message back to a string.
    message = data.decode()

    # It will check what message the client sent and then send a picture accordintly.
    if message == "1":
        img = Image.open('Pictures/car.jpg')
    elif message == "2":
        img = Image.open('Pictures/house.jpg')
    elif message == "3":
        img = Image.open('Pictures/dog.jpg')
    elif message == "4":
        img = Image.open('Pictures/forest.jpg')
    elif message == "5":
        img = Image.open('Pictures/mountain.jpg')
    elif message == "6":
        img = Image.open('Pictures/ocean.jpg')
    else:
        img = Image.open('Pictures/notfound.jpg')
        
    # Conveting the picture in bytes so it can be sent through the network.
    buf = io.BytesIO()
    img.save(buf,format='JPEG')
    byte_im = buf.getvalue()

    c.sendall(byte_im)
    
    c.close()
