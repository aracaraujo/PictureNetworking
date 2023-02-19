import socket
from io import BytesIO
from PIL import Image
import os

controller = True

while controller:
    # Creating socket that will connect client to server.
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    os.system("clear")
    print("What picture do you want? ")
    print("1. Car")
    print("2. House")
    print("3. Dog")
    print("4. Forest")
    print("5. Mountain")
    print("6. Ocean")
    user_input = input("Number of choice: ")

    # Converting user input to bytes so it can be sent through the network.
    message = bytes(user_input,'utf-8')

    # Assigning a port.
    port = 40674

    # Connecting socket to server.
    s.connect(('127.0.0.1', port))

    s.sendall(message)

    # Receving picture back from the server.
    data = s.recv(1073741824)

    # Converting picture bytes in the real picture again.
    stream = BytesIO(data)
    image = Image.open(stream).convert("RGBA")
    stream.close()
    image.show()

    # Ask user if they wants more picture.
    control_input = input("Do you want to see another picture?(y/n) ")

    if control_input.lower() == "n":
        controller = False
    
    s.close()