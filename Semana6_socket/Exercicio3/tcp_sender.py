import socket
import sys

TCP_IP = "127.0.0.1"  #define o endereço de ip
FILE_PORT = 5005 #define a porta para o qual o nome do arquivo vai ser enviado
DATA_PORT = 5006 #define a porta para os quais os dados do arquivo vão ser enviados
buf = 1024
file_name = sys.argv[1]


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, FILE_PORT)) #relaciona o endereço de ip e a porta
    sock.send(file_name) #envia o nome do arquivo
    sock.close() #fecha a conexão

    print ("Sending %s ..." % file_name)

    f = open(file_name, "rb") #abre o arquivo a ser enviado, em leitura binaria
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, DATA_PORT)) #conecta o socket ao endereço de ip e porta especificados
    data = f.read() #lê do conteúdo do arquivo
    sock.send(data) #envia o arquivo para o reciever

finally:
    sock.close()
    f.close()