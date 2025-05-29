import socket

# Cria socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Escolhe a porta
client.connect(('localhost', 7777))
print("Conected to server...\n")

# Envia o dado
send_data = "Receba!".encode()
client.send(send_data)
print("Send   >>", send_data.decode())

# Recebe o dado
recived_data = True
data = ''
while recived_data:
    recived_data = client.recv(1024).decode()

    data += recived_data
    if not recived_data:
        break

    print("Recive <<", data)

input("Press enter to quit.")