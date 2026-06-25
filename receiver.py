import socket

HOST = ""
PORT = 5000

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind((HOST, PORT))

print("Receiver started...")
print("Waiting for messages...\n")

while True:
    data, address = receiver.recvfrom(1024)

    print("\n======================")
    print("Received from:", address[0])
    print("Message:", data.decode())
    print("======================")
