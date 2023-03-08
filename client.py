import socket

host = "170.0.0.1"
port = 8080

connected = True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    while connected:
        i = input("Enter message to send, \"d\" to disconnect: ")
        if str(i) == "d":
            connected = False
        else:
            s.sendall(str(i).encode("UTF-8"))
            data = s.recv(1024)
            print("server replied: ", data.decode("UTF-8"))
