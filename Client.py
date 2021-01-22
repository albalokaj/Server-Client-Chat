import socket

serverName = 'alba.local'
port = 12000
print("Server: " + serverName)
print("Port: " + str(port))

global sock
def funct():
    while 1:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((serverName, port))
            break
        except socket.error as error:
            print("Couldn't connect.")
            return


    name = str(sock.recv(1024), "utf-8")
    you = input("Write your name: ")
    sock.sendall(str.encode(you))
    while 1:
        answer = str(sock.recv(1024), "utf-8")
        if answer == "quit":
            print(name + " ended the conversation")
            break
        print(name + ": " + answer)

        data = input("You: ")
        lines = ""
        while 1:
            if data == "over":
                break
            if data == "quit":
                sock.sendall(str.encode(data))
                print("You ended the conversation")
                break
            lines += data + "\n"
            data = input("You: ")

        if len(str.encode(lines)) > 0:
            print("Typing...")
            sock.sendall(str.encode(lines))
    return

funct()
