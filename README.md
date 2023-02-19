# Overview

The purpose of this project was to learn how client and server work on the networking level. I’m interested in backend development, so I wanted to learn how the communication between client and server works.

This program has a server side and a client side. The server side holds pictures that can be requested by the client. When the client program us running it asks the user which picture, they want to. Once the user chooses what picture they want to a message will be sent to the server and the server will send back the image accordingly.

To run the program, you can clone this repository and open two different terminals.

On te first terminal run:
```
python server.py
```

You should expect an output like this:
```
socket binded to 40674
socket is listening
```
Now you server is up and running, waiting for connections.

On the second terminal run:
```
python client.py
```
You should expect an output like this:
```
What picture do you want? 
1. Car
2. House
3. Dog
Number of choice: 
```
Now your client is running. After choosing one of the option the server will send you one of the pictures. If you choose one option that doesn't exist it will also send you a picture of not found.

The link bellow is a demo video of the program running.

[Networking Demo Video](https://www.youtube.com/watch?v=DAZPlj2IXug)

# Network Communication

The architecture used here was client/server.

The program was written in Python using the socket library. The communication protocol used is TCP/IP. The server ip address is 127.0.0.1 and the port being used is 40674.

The client program convert the string input by the user in bytes and send to the server. The server reads the message and using PIL library converts the pictures in bytes and send it back to the client. The client using PIL library also converts the bytes in image again.

# Development Environment

The program was developed in VS Code and was written in Python. Socket and PIL library were used for networking connection and image processing respectively.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [PIL Tutorial - Geeks For Geeks](https://www.geeksforgeeks.org/python-pillow-tutorial/)
* [Socket Tutorial - Geeks For Geeks](https://www.geeksforgeeks.org/socket-programming-python/)

# Future Work

* Creating a database for the server to store the pictures.
