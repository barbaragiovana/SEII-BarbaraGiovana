import socket
import select

UDP_IP = "127.0.0.1"  #define o endereço de ip do host
IN_PORT = 5005  #define a porta de conexao
timeout = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT)) #relaciona o socket com o endereço de ip e porta de conexao indicados anteriormente

while True:
    data, addr = sock.recvfrom(1024) #recebe 1024 bytes de dados
    if data:
        print ("File name:", data) #printa o nome do arquivo
        file_name = data.strip()  #salva o nome do arquivo 

    f = open(file_name, 'wb') #cria um arquivo nesse lado da conexao

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data) #escreve os dados do arquivo recebido
        else:
            print ("%s Finish!" % file_name)
            f.close()
            break