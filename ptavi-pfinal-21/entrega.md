## Parte básica.
El proyecto consta de dos servidores, un SIP y un RTP, y Cliente. 
El Servidor SIP actúa como Proxy entre Servidor RTP y Cliente.
Lanzamos el serversip.py en primer lugar, el servidor se encuentra escuchando. 
Lanzamos en segundo lugar el serverrtp.sy indicandole el mismo puerto que el serversip.py, aunque en realidad el 
servidor RTP se conecta por otro puerto, el 6002, forzado en el código. Realizamos esta medida, porque no se pueden
conectar dos servidores al mismo puerto. Por último lanzamos el cliente, con los parámetros indicados. En cualquiera
de las conexiones si los parámetros de entrada no son correctos, el código está diseñado para indicarte cuál es la 
forma requerida en el mismo terminal. 
Una vez lanzado el cliente, se envía un REGISTER al servidor SIP, al igual que el servidor RTP envía su propio REGISTER
a dicho servidor SIP. Ambos extremos ya se encuentran registrados en serversip.py, que actúa como Proxy entre ambos.
El cliente realizaa un INVITE al servidor SIP y este se lo envía a servidor RTP, una vez aceptadas las invitaciones 
se envía el ACK y comienza el evío RTP desde servidor RTP a cliente.
En el momento de la invitación del cliente se abre un puerto de escucha UDP, donde se ha programado que recoga todas 
las trazas enviadas en un fichero 'output.mp3'.
Una vez terminado el tiempo de expiración del cliente se realiza un BYE en este y termina su conexión, mientras que 
ambos servidores siguen escuchando.
El servidor SIP recrea su código de respuesta  que se analiza y se gestiona dependiendo el caso.

## Parte adicional.

* Gestión de errores.
Hemos programado el código para que recoja los siguientes errores:
SIP/2.0 400 Bad Request -> Mensaje con una estructura errónea.
SIP/2.0 404 User Not Found -> Usuario no encontrado.
SIP/2.0 405 Method Not Allowed -> Método de petición desconocido. Sólo acepta REGISTER, INVITE, ACK, BYE.

* Cabecera de tamaño.
En el INVITE creado por el cliente se añade el parámetro 'Content-Length' donde se indica el tamaño de la cabecera del
paquete en bytes.

* Tiempo de expiracion.
En el servidor RTP dentro del método REGISTER creamos un bucle que reenvía este método cada 30 segundos.
Si el servidor se encuentra en activo se envía el socket del REGISTER cada 30 segundos, si dicho Servidor está 
inactivo se sale del bucle. Dentro de este bucle se encuentra la excepción 'Connection refused' que realiza un 
'sys.exit' y cierra el programa directamente sin importar el bucle que tiene por encima. 
NOTA: A la hora de salir de este Servidor (CTRL C) se crea el mensaje 'Server finish' y el servidor RTP no se cierra
hasta que no haya acabado los 30 segundos del 'time.sleep'.
