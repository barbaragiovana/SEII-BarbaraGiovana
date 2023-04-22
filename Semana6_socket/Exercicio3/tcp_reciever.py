import socket

TCP_IP = "127.0.0.1" #define o endereço de ip
FILE_PORT = 5005 #define a porta para o qual o nome do arquivo vai ser recebido
DATA_PORT = 5006 #define a porta para os quais os dados do arquivo vão ser recebidos
timeout = 3
buf = 1024


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_f.bind((TCP_IP, FILE_PORT)) #relaciona o endereço de ip e a porta
sock_f.listen(1)  #permite o socket para aceitar conexões

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind((TCP_IP, DATA_PORT)) #relaciona o socket com o endereço de ip do host e a porta definida para os dados do arquivo
sock_d.listen(1) #permite o socket para aceitar conexões


while True:
    conn, addr = sock_f.accept() #indica que a execucao do codigo so acontece com conexao
    data = conn.recv(buf) #recebe qualquer dado enviado do outro lado da conexão armazenando em uma variável
    if data:
        print ("File name:", data) #printa o nome do arquivo
        file_name = data.strip() #armazena o nome do arquivo

    f = open(file_name, 'wb') #cria um arquivo com o nome do arquivo recebido

    conn, addr = sock_d.accept() #indica que a execucao do codigo so acontece com conexao
    while True:
        data = conn.recv(buf) #recebe qualquer dado enviado do outro lado da conexão armazenando em uma variável
        if not data:
            break
        f.write(data) #escreve os dados recebidos no arquivo

    print ("%s Finish!" % file_name)
    f.close()