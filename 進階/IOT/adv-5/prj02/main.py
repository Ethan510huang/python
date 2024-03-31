import socket

Host = "localhost"
Port = 5438
server_socket = socket.socket()
server_socket.bind((Host, Port))
server_socket.listen(5)
print("server:{} port:{} start".format(Host, Port))
client, addr = server_socket.accept()
print("client address:{}, port:{}".format(addr[0], addr[1]))
while True:
    msg = client.recv(128).decode("utf8")
    print("Recieve Message:" + msg)
    reply = ""
    if msg == "Hi":
        reply = "Hello!"
        client.send(reply.encode("utf8"))
    elif msg == "Bye":
        client.send(b"quit")
        break
    else:
        reply = "what??"
        client.send(reply.encode("utf8"))
client.close()
server_socket.close()
