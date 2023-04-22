import socket
import time
import sys

UDP_IP = "127.0.0.1" #define endereço de ip do host
UDP_PORT = 5005 #define porta de conexao
buf = 1024
file_name = sys.argv[1]


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(file_name, (UDP_IP, UDP_PORT)) #envia o nome do arquivo para o endereço ip e porta indicados
print ("Sending %s ..." % file_name)

f = open(file_name, "r") #abre o arquivo apenas para leitura
data = f.read(buf) 
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): #envia os dados do arquivo para o endereço de ip e porta indicados
        data = f.read(buf)
        time.sleep(0.02) # Give receiver a bit time to save

sock.close()
f.close()