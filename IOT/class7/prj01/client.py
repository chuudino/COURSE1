import socket

client_socket = socket.socket()
client_socket.connect(("localhost", 5438))
print("Connected to server at localhost:5438")

while True:
    msg = input("Enter message to send to server (type 'exit' to quit): ")
    client_socket.send(msg.encode("utf-8"))

    if msg.lower() == "exit":
        print("Exiting client.")
        reply = client_socket.recv(1024).decode("utf-8")
        print(f"Received from server: {reply}")
        break
    else:
        reply = client_socket.recv(1024).decode("utf-8")
        print(f"Received from server: {reply}")
