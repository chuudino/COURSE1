import socket

HOST = "localhost"
PORT = 5438
server_socket = socket.socket()  # create a socket object
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 允許重複使用地址
server_socket.bind((HOST, PORT))  #
server_socket.listen(2)
print(f"Server listening on {HOST}:{PORT}")
client_socket, addr = server_socket.accept()
# print add[0] and addr[1]
print(f"Connection from {addr[0]}:{addr[1]}")

while True:
    client_msg = client_socket.recv(1024).decode("utf-8")
    print(f"Received from client: {client_msg}")
    reply_msg = ""
    if client_msg.lower() == "hi":
        reply_msg = "Hello from server!"
        client_socket.send(reply_msg.encode("utf-8"))
    elif client_msg.lower() == "exit":
        client_socket.send("exit".encode("utf-8"))
        client_socket.close()
        server_socket.close()
        break
    else:
        reply_msg = "what ??"
        client_socket.send(reply_msg.encode("utf-8"))
