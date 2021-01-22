import socket

serverName = 'alba.local'
port = 12000
print("Server: " + serverName)
print("Port: " + str(port))

global soketi
def funct():
    while 1:
        try:
            soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soketi.connect((serverName, port))
            break
        except socket.error as error:
            print("Couldn't connect.")
            return


    name = str(soketi.recv(1024), "utf-8")
    you = input("Write your name: ")
    soketi.sendall(str.encode(you))
    while 1:
        answer = str(soketi.recv(1024), "utf-8")
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
                soketi.sendall(str.encode(data))
                print("You ended the conversation")
                break
            lines += data + "\n"
            data = input("You: ")

        if len(str.encode(lines)) > 0:
            print("Typing...")
            soketi.sendall(str.encode(lines))
    return

funct()