# Reverse Shell Python

Script de Python Cliente-Servidor para establecer una conexión reversa entre ambas máquina (máquina víctima, máquina atacante)

Necesitaremos ejecutar el script atacante.py desde la máquina atacante, donde se va a pedir al usuario que inserte un comando para que se envíe a la máquina víctima y se pueda ejecutar gracias a la librería subprocess. Después, al mismo tiempo, recibiremos ese output procedente de la máquina víctima de vuelta a nuestra máquina atacante con la ejecución del comando correspondiente.

El funcionamiento será el siguiente, donde primero ejecutaremos el código desde la máquina víctima para que permanezca en escucha a espera del comando enviado por la máquina atacante:

![imagen](https://user-images.githubusercontent.com/96432001/223709097-8ac5ff76-c14d-4b8c-a1c5-ae240577109f.png)
 
 Y ahora si ejecutamos el código desde la máquina atacante, ya podremos insertar el comando que queramos y recibirlo de vuelta:
 
![imagen](https://user-images.githubusercontent.com/96432001/223709031-eb2f57d2-1f78-4edb-af0c-c662dbc75959.png)

