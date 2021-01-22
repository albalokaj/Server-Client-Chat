import socket
from _thread import *

host = "alba.local"
port = 12000
global soketi

#Socket
try:
    soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print("Error: " + str(error))

#Connect host with port
try:
    soketi.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    soketi.bind((host, port))
    print("Port: " + str(port))
    soketi.listen(10)
    print("Server is ready to receive")
except socket.error as error:
    print("Error: " + str(error))

def thread(connection, address):
    you = input("Write your name: ")
    connection.send(str.encode(you))
    name = str(connection.recv(1024), "utf-8")
    while 1:
        data = input("You: ")
        lines = ""
        while 1:
            if data == "over":
                break
            if data == "quit":
                connection.send(str.encode(data))
                print("You ended the conversation")
                return
            lines += data + "\n"
            data = input("You: ")
        if len(str.encode(lines)) > 0:
            print("Typing...")
            connection.send(str.encode(lines))
            rec = str(connection.recv(1024), "utf-8")
            if rec == "quit":
                print(name + " ended the conversation.")
                break
            print(name + ": " + rec)

    connection.close()
    return

#Lidhja e serverit me klientin
try:
    while 1:
        connection, address = soketi.accept()
        print("Server is connected to the IP address " + str(address[0]) + " and port " + str(address[1]))
        start_new_thread(thread, (connection, address))
except socket.error as error:
    print("Couldn't connect.")


