# Reverse Shell_Python

Script Cliente-Servidor para establecer una conexión reversa entre ambas máquina (máquina víctima, máquina atacante)

Necesitaremos un script de la máquina atacante, donde se va a pedir al usuario que envíe un comando para que se envíe a la máquina víctima; y después al mismo tiempo recibiremos ese output procedente de la máquina víctima de vuelta a nuestra máquina atacante.


Ahora el funcionamiento será el siguiente, donde primero ejecutaremos el código desde la máquina víctima para que permanezca en escucha a espera del comando enviado por la máquina atacante:

![[Pasted image 20230308125116.png]]
 
 Y ahora si ejecutamos el código desde la máquina atacante, ya podremos insertar el comando que queramos y recibirlo de vuelta:
 
![[Pasted image 20230308125219.png]]
