import socket

target = input("Enter IP (example: 127.0.0.1): ")
port = int(input("Enter port number: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = s.connect_ex((target, port))

if result == 0:
    print("Port is OPEN 🔓")
else:
    print("Port is CLOSED 🔒")

s.close()