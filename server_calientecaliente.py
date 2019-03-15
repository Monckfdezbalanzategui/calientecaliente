import socket
from random import randrange

host_ip="192.168.56.1"
port=8090
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
numero_aleatorio=randrange(0,99)

try:
    server_socket.bind((host_ip,port))
except:
    print("Ha habido un problema")
    server_socket.close()
server_socket.listen(10)
print("Esperando conexión")
conexion, addr_cliente=server_socket.accept()
print("Conexión establecida")
while True:
    numero=conexion.recv(1024).decode
    if numero_aleatorio+10==numero or (numero_aleatorio-10==numero):
        conexion.send("caliente, caliente").encode()
    elif numero_aleatorio+10>numero:
        conexion.send("frío, frío, por debajo")
    elif numero_aleatorio+10<numero:
        conexion.send("frío, frío, por arriba")
    elif numero_aleatorio==numero:
        conexion.send("Felicidades")
    continue
server_socket.close()
