import socket

host_ip=host_ip="192.168.56.1"

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.connect((host_ip,0))
except:
    print("Ha habido un problema")
    client_socket.close()
while True:
    print("Escriba un número del 0 al 99")
    numero=input(int())
    numero=numero.encode()
    client_socket.send(numero)
    mensaje_servidor=client_socket.recv(1024).decode()
    if mensaje_servidor=="Felicidades":
        break
        client_socket.close()
    else:
        continue
