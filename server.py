import socket
import io
from PIL import Image

s = socket.socket()

port = 40674

s.bind(('',port))
print("socket binded to %s" %(port))

s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from ', addr)
    
    data = c.recv(1073741824)

    message = data.decode()

    if message == "1":
        img = Image.open('Pictures/car.jpg')
    elif message == "2":
        img = Image.open('Pictures/house.jpg')
    elif message == "3":
        img = Image.open('Pictures/dog.jpg')
    else:
        img = Image.open('Pictures/notfound.jpg')
        
    buf = io.BytesIO()
    img.save(buf,format='JPEG')
    byte_im = buf.getvalue()

    c.sendall(byte_im)
    
    c.close()
