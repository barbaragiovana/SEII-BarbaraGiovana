import socket
import threading

HEADER = 64 #define o numero de bytes recebidos
PORT = 5050 #define a porta
SERVER = socket.gethostbyname(socket.gethostname()) #atribui o endereço de ip pra o servidor
ADDR = (SERVER, PORT) #relaciona o servidor e a porta
FORMAT = 'utf-8' #define o formato binário
DISCONNECT_MESSAGE = '!DISCONNECT' #define a mensagem de desconexão

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn: socket.socket, addr): #define como é a função que administra as configurações entre servidor e cliente
  print(f'[NEW CONNECTION] {addr} connected.')

  connected = True
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)

    if msg_length:
      msg_length = int(msg_length)
      msg = conn.recv(msg_length).decode(FORMAT)

      if msg == DISCONNECT_MESSAGE:
        connected = False

      print(f'[{addr}] {msg}') #printa o endereço do cliente(ou seja, sua identidade) e sua mensagem

      conn.send('Message received'.encode(FORMAT))
  
  conn.close()

def start(): #define como é a função que administra as conexões servidor-cliente
  server.listen()
  print(f'[LISTENING] Server is listening on {SERVER}')

  while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')

print('[STARTING] server is starting...')
start()
