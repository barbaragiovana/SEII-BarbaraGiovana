import socket

HEADER = 64 #define o número de bytes enviados
PORT = 5050 #define a porta de comunicação
FORMAT = 'utf-8'#define o formato de codificação binária
DISCONNECT_MESSAGE = "!DISCONNECT" #define a mensagem de desconexão
SERVER = "192.168.1.26" #atribui o endereço de ip pra o servidor
ADDR = (SERVER, PORT) #relaciona o servidor e a porta

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg): #função que envia as mensagens ao servidor
    
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

#envia mensagens 
send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")

send(DISCONNECT_MESSAGE) #desconecta
