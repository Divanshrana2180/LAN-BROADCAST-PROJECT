import socket

BROADCAST_IP = "255.255.255.255"
PORT = 5000

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print("LAN Broadcast Sender Started")

while True:
    message = input("Enter Message: ")
    sender.sendto(message.encode(), (BROADCAST_IP, PORT))
