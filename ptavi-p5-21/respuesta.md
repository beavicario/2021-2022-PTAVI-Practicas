
## Respuesta: Ejercicio 3. Análisis general.

* ¿Cuántos paquetes componen la captura?
  * La captura se compone de 1090 paquetes.
* ¿Cuánto tiempo dura la captura?
    * La captura tiene una duración de unos 14.50 segundos. 
  Tiempo en el último paquete de la captura: **[Time since reference or first frame: 14.491079516 seconds]**
* ¿Qué IP tiene la máquina donde se ha efectuado la captura? ¿Se trata de una IP pública o de una IP privada? ¿Por qué lo sabes?
  * La IP del cliente es: **192.168.1.34**.
  Se trata de una IP privada porque se encuentra dentro de las redes privadas de IPV4. Dicha IP es de clase C, donde se encuentran todas las IPs privadas dentro del rango: 192.168.0.0 – 192.168.255.255.
  
Antes de analizar las tramas, mira las estadísticas generales que aparecen en el menú de `Statistics`. En el apartado de jerarquía de protocolos (`Protocol Hierarchy`) se puede ver el número de paquetes y el tráfico correspondiente a los distintos protocolos.

* ¿Cuáles son los tres principales protocolos de nivel de aplicación por número de paquetes?
  * Real-Time Transport Protocol (RTP): Formado por 1049 paquetes, un 96,2% de la trama total.
  * Session Initiation Protocol (SIP): Formado por 9 paquetes, un 0,8% de la trama total.
  * Real-Time Transport Control Protocol (RTCP): Formado por 8 paquetes, un 0,7% de la trama total.
* ¿Qué otros protocolos podemos ver en la jerarquía de protocolos?
  * Internet Protocol Version 4 (IPv4)
    * Internet Control Message Protocol (ICMP)
    * Use Datagram Protocol (UDP)
      * Session Traversal Utilities for NAT (STUN)
  * La trama se transmite en red IPV4. El protocolo de transporte UDP ocupa toda la trama excepto 3 paquetes ICMP que pertenecen a la capa de red para control.
  Dentro de los paquetes UDP nos encontramos el resto de protocolos de transporte en los que se divide el mensaje (RTP, SIP, RTCP, STUN).
* ¿Qué protocolo de nivel de aplicación presenta más tráfico, en bytes por segundo? ¿Cuánto es ese tráfico?
  * Real-Time Transport Protocol (RTP): 180.428 bytes enviados, es decir, 12443 bytes/s.

Observa por encima el flujo de tramas en el menú de `Statistics` en `IO Graphs`. La captura que estamos viendo incluye desde la inicialización (registro) de la aplicación hasta su finalización, incluyendo una llamada. 

* Filtra por `sip` para conocer cuándo se envían paquetes SIP. ¿En qué segundos tienen lugar esos envíos?
  * Time = 0s: Envío de 4 paquetes.
  * Time = 3s: Envío de 3 paquetes.
  * Time = 14s: Envío de 2 paquetes.
* Y los paquetes con RTP, ¿cuándo se empiezan a enviar?
  * Los primeros paquetes enviados se encuentran en el segundo 4.
* Los paquetes RTP, ¿cuándo se dejan de enviar?
  * El último paquete RTP enviado se presenta después de 14 segundos del inicio.
* Los paquetes RTP, ¿cada cuánto se envían?
  * Se envían 100 paquetes RTP en un segundo.

Sigue respondiendo las cuestiones que se plantean en este guion en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.


## Respuesta: Ejercicio 4. Primeras tramas

Analiza ahora las dos primeras tramas de la captura. Cuando se pregunta por máquinas, llama "Linphone" a la máquina donde está funcionando el cliente SIP, y "Servidor" a la máquina que proporciona el servicio SIP.

* ¿De qué protocolo de nivel de aplicación son?
  * Paquetes SIP (Session Initiation Protocol)
* ¿Cuál es la dirección IP de la máquina "Linphone"?
  * IP Src: 192.168.1.34.
* ¿Cuál es la dirección IP de la máquina "Servidor"?
  * IP Dst: 212.79.111.155
* ¿En qué máquina está el UA (user agent)?
  * Se encuentra en la petición de la máquina 'Linphone' (192.168.1.34).
  **User-Agent: Linphone/3.12.0 (belle-sip/1.6.3)**
* ¿Entre qué máquinas se envía cada trama?
  * La primera trama se lanza una petición de cliente 'Linphone' (192.168.1.34) a Servidor (212.79.111.155).
  **Internet Protocol Version 4, Src: 192.168.1.34, Dst: 212.79.111.155**
  * La segunda trama el Servidor (212.79.111.155) contesta a la petición de cliente 'Linphone' (192.168.1.34).
  **Internet Protocol Version 4, Src: 212.79.111.155, Dst: 192.168.1.34**
* ¿Qué ha ocurrido para que se envíe la primera trama?
  * El cliente 'Linphone' le envía una petición REGISTER al Servidor.
* ¿Qué ha ocurrido para que se envíe la segunda trama?
  * El Servidor contesta a la petición REGISTER del cliente 'Linphone' con el siguiente mensaje de error:
  **Status-Line: SIP/2.0 401 Unauthorized**, 

Ahora, veamos las dos tramas siguientes.

* ¿De qué protocolo de nivel de aplicación son?
  * Session Initiation Protocol (SIP)
* ¿Entre qué máquinas se envía cada trama?
  * Ambas tramas se envían entre las máquinas 192.168.1.34 y 212.79.111.155.
  En la primera el mensaje es enviado por 192.168.1.34 hacia 212.79.111.155 
  y en la segunda se envía en dirección inversa. 
  * 1º trama: **Internet Protocol Version 4, Src: 192.168.1.34, Dst: 212.79.111.155**
  * 2º trama: **Internet Protocol Version 4, Src: 212.79.111.155, Dst: 192.168.1.34**
* ¿Qué ha ocurrido para que se envíe la primera de ellas (tercera trama en la captura)?
  * Se vuelve a enviar la petición REGISTER pero con la  autentificación firmada por el usuario.
* ¿Qué ha ocurrido para que se envíe la segunda de ellas (cuarta trama en la captura)?
  * El Servidor contesta a la petición REGISTER con **SIP/2.0 200 OK**, es decir, se inicia la sesión del usuario
  y esta se registra en el Servidor.

Ahora, las tramas 5 y 6.

* ¿De qué protocolo de nivel de aplicación son?
  * Session Initiation Protocol (SIP/SDP)
* ¿Entre qué máquinas se envía cada trama?
  * Ambas tramas se envían entre las máquinas 192.168.1.34 y 212.79.111.155.
  En la primera el mensaje es enviado por 192.168.1.34 hacia 212.79.111.155 
  y en la segunda se envía en dirección inversa. 
  * 1º trama: **Internet Protocol Version 4, Src: 192.168.1.34, Dst: 212.79.111.155**
  * 2º trama: **Internet Protocol Version 4, Src: 212.79.111.155, Dst: 192.168.1.34**
* ¿Qué ha ocurrido para que se envíe la primera de ellas (quinta trama en la captura)?
  * El usuario envía petición INVITE para establecer una sesión de intercambio de datos.
* ¿Qué ha ocurrido para que se envíe la segunda de ellas (sexta trama en la captura)?
  * El Servidor contesta a la petición INVITE con **SIP/2.0 200 OK** y con las características
  de la sesión RTP a iniciar.
* ¿Qué se indica (en líneas generales) en la parte SDP de cada una de ellas?
  * 1º trama.
    * Usuario: jgbarah
    * IP Src: 192.168.1.34
    * Type Media: audio 
      * Puerto: 7078 
      * Protocolo de audio: RTP/AVP
      * Media Format: DynamicRTP-Type-96
    * Type Media: video. 
      * Puerto: 9078 
      * Protocolo de video: RTP/AVP
      * Media Format: DynamicRTP-Type-96
    * Valores codificación de trama.
  * 2ª trama.
    * ID sesión: 1902109695
    * IP Src: 212.79.111.155
    * Type Media: audio 
      * Puerto: 27138 
      * Protocolo de audio: RTP/AVP
      * Media Format: DynamicRTP-Type-96
      * Media Format: DynamicRTP-Type-97
      * Media Format: DynamicRTP-Type-98
    * Type Media: video. 
      * Puerto: 0
      * Protocolo de video: RTP/AVP
      * Media Format: DynamicRTP-Type-96
    * Valores codificación de trama.

Después de la trama 6, busca la primera trama SIP.

* ¿Qué trama es?
  * Es la trama 11 y corresponde a una respuesta ACK.
* ¿De qué máquina a qué máquina va?
  * **Internet Protocol Version 4, Src: 192.168.1.34, Dst: 212.79.111.155**
* ¿Para qué sirve?
  * Una respuesta ACK confirma la solicitud INVITE.
* ¿Puedes localizar en ella qué versión de Linphone se está usando?
  * **Linphone/3.12.0 (belle-sip/1.6.3)**

Sigue respondiendo las cuestiones que se plantean en este guion en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.


## Respuesta: Ejercicio 5. Tramas especiales

Las tramas 7 y 9 parecen un poco especiales:

* ¿De qué protocolos son (indica todos los protocolos relevantes por encima de IP)?
  * Use Datagram Protocol (UDP)
  * Session Traversal Utilities for NAT (STUN)
* ¿De qué máquina a qué máquina van?
  * Desde máquina origen con IP 192.168.1.34, a la máquina destino con IP 212.79.111.155.
  **Internet Protocol Version 4, Src: 192.168.1.34, Dst: 212.79.111.155**
* ¿Para qué crees que sirven?
  * El protocolo STUN, en la capa de red, se utiliza para comunicaciones cliente-servidor.
  Permite a clientes NAT encontrar su dirección IP pública y el puerto asociado y así configurar la comunicación UDP entre las máquinas.
  Por lo tanto, el servidor sabe que IP pública y puerto tiene asociado el cliente que levanta comunicación UDP, 
  ambos hosts se configuran con esos datos para el envío de tráfico.

Sigue respondiendo las cuestiones que se plantean en este guion en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Respuesta: Ejercicio 6. Registro

Repasemos ahora qué está ocurriendo (en lo que al protocolo SIP se refiere) en las primeras tramas SIP que hemos visto ya:

* ¿Qué dirección IP tiene el servidor que actúa como registrar SIP? ¿Por qué?
  * El Servidor tiene la dirección IP 212.79.111.155. 
  Ya que esta IP responde a la petición SIP REGISTER que envía al cliente.
* ¿A qué puerto (del servidor Registrar) se envían los paquetes SIP?
  * El puerto de transmisión de datos es 5060.
  **User Datagram Protocol, Src Port: 5060, Dst Port: 5060**
* ¿Qué método SIP utiliza el UA para registrarse?
  * **Method: REGISTER**
* ¿Qué diferencia fundamental ves entre la primera línea del paquete SIP que envía Linphone para registrar a un usuario, y el que hemos estado enviando en la práctica 4?
  * En la práctica 4 teníamos que indicar la IP y el puerto del usuario que se quería registrar (REGISTER), 
  mientras que, en esta captura, la IP y el puerto se asignan en la cabecera de la trama SIP.
* ¿Por qué tenemos dos paquetes `REGISTER` en la traza?
  * El usuario 'Linphone' envía una petición REGISTER al servidor encapsulada en una trama SIP. 
  El servidor contesta a esta petición con un mensaje de error porque necesita la autentificación del usuario.
  Por lo que la segunda traza el usuario vuelve a enviar la petición REGISTER con la autentificación.
* ¿Por qué la cabecera `Contact` es diferente en los paquetes 1 y 3? ¿Cuál de las dos cabeceras es más "correcta", si nuestro interés es que el UA sea localizable?
  * La cabecera 'Contact' muestra las direcciones para contactar con el usuario.
    * 1º trama: **Contact: <sip:jgbarah@192.168.1.34;transport=udp>;+sip.instance="<urn:uuid:d01e6e35-b5ca-4b00-94a6-a6f85fc4cb37>"**
    * 3º trama: **Contact: <sip:jgbarah@83.38.204.116;transport=udp>;+sip.instance="<urn:uuid:d01e6e35-b5ca-4b00-94a6-a6f85fc4cb37>"**
  * Sería más correcto la IP del 'Contact' de la 3º trama ya que es el REGISTER que ha aceptado el servidor.
* ¿Qué tiempo de validez se está dando para el registro que pretenden realizar los paquetes 1 y 3?
  * El tiempo de expiración es 1 hora.
  **Expires: 3600**

Para responder estas preguntas, puede serte útil leer primero [Understanding REGISTER Method](https://blog.wildix.com/understanding-register-method/), además de tener presente lo explicado en clase.

Sigue respondiendo las cuestiones que se plantean en este guion en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Respuesta: Ejercicio 7. Indicación de comienzo de conversación

* Además de REGISTER, ¿podrías decir qué instrucciones SIP entiende el UA?
  * INVITE: Invitar a sesión.
  * ACK: Confirmación de respuesta INVITE.
  * BYE: Terminar sesión.
  * CANCEL: Cancela petición, pero no finaliza sesión.
  * OPTIONS: Pregunta la capacidad del servidor.
* ¿En qué paquete el UA indica que quiere comenzar a intercambiar datos de audio con otro? 
¿Qué método SIP utiliza para ello?
  * El usuario envía un INVITE en la traza 5, para intercambiar datos de audio con el servidor.
  **Session Initiation Protocol (INVITE)**
* ¿Con qué dirección quiere intercambiar datos de audio el UA?
  * Con el servidor, de IP 212.79.111.155.
  **Internet Protocol Version 4, Src: 192.168.1.34, Dst: 212.79.111.155**
* ¿Qué protocolo (formato) está usando para indicar cómo quiere que sea la conversación?
  * Session Description Protocol (SDP)
* En la indicación de cómo quiere que sea la conversación, puede verse un campo `m` con un valor que empieza por `audio 7078`. ¿Qué indica el `7078`? ¿Qué relación tiene con el destino de algunos paquetes que veremos más adelante en la trama? ¿Qué paquetes son esos?
  * El '7078' es el puerto Media, por este puerto se enviarán todos los datos del audio que son paquetes RTP.
* En la respuesta a esta indicación vemos un campo `m` con un valor que empieza por `audio 27138`. ¿Qué indica el `27138`?  ¿Qué relación tiene con el destino de algunos paquetes que veremos más adelante en la trama? ¿Qué paquetes son esos? 
  * El '27138' es el puerto Media del servidor, se utilizará para el tráfico de datos de audio que son paquetes RTP.
* ¿Para qué sirve el paquete 11 de la trama?
  * Respuesta ACK que envía el usuario al servidor, valida las condiciones para intercambio RTP con el servidor.

Sigue respondiendo las cuestiones que se plantean en este guion en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Respuesta: Ejercicio 8. Primeros paquetes RTP

Vamos ahora a centrarnos en los paquetes RTP. Empecemos por el paquete 12 de la traza:

* ¿De qué máquina a qué máquina va?
  * Trama enviada por el usuario, con IP 192.168.1.34, hacia el servidor, con IP 212.79.111.155.
  **Internet Protocol Version 4, Src: 192.168.1.34, Dst: 212.79.111.155**
* ¿Qué tipo de datos transporta?
  * Transporta los datos de audio.
* ¿Qué tamaño tiene?
  * **Frame Length: 214 bytes (1712 bits)**
* ¿Cuántos bits van en la "carga de pago" (payload)?
  * La trama consta 214 bytes, para poder sacar el tamaño de payload se restan 12 bytes de la cabecera RTP, 
  14 bytes Ethernet, 20 bytes de la IP y 8 bytes de la cabecera UDP. Por lo tanto, el tamaño de payload es de 160 bytes.
* ¿Se utilizan bits de padding?
  * NO. **Padding: False**
* ¿Cuál es la periodicidad de los paquetes según salen de la máquina origen?
  * Existe una periodicidad de 20 ms con mínimas variaciones.
* ¿Cuántos bits/segundo se envían?
  * 99.000 bits/s.

Y ahora, las mismas preguntas para el paquete 14 de la traza:

* ¿De qué máquina a qué máquina va?
  * Trama enviada por el servidor, con IP 212.79.111.155, hacia el usuario, con IP 192.168.1.34.
  **Internet Protocol Version 4, Src: 212.79.111.155, Dst: 192.168.1.34**
* ¿Qué tipo de datos transporta?
  * Transporta los datos de audio.
* ¿Qué tamaño tiene?
  * **Frame Length: 214 bytes (1712 bits)**
* ¿Cuántos bits van en la "carga de pago" (payload)?
  * La trama consta 214 bytes, para poder sacar el tamaño de payload se restan 12 bytes de la cabecera RTP, 
  14 bytes Ethernet, 20 bytes de la IP y 8 bytes de la cabecera UDP. Por lo tanto, el tamaño de payload es de 160 bytes.
* ¿Se utilizan bits de padding?
  * NO. **Padding: False**
* ¿Cuál es la periodicidad de los paquetes según salen de la máquina origen?
  * Existe una periodicidad de 20 ms con mínimas variaciones.
* ¿Cuántos bits/segundo se envían?
  * 99.000 bits/s.

Sigue respondiendo las cuestiones que se plantean en este guion en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Respuesta: Ejercicio 9. Flujos RTP

Vamos a ver más a fondo el intercambio RTP. Busca en el menú `Telephony` la opción `RTP`. Empecemos mirando los flujos RTP.

* ¿Cuántos flujos hay? ¿por qué?
  * Nos encontramos con 2 flujos. El primer flujo va desde usuario a servidor (Src: 192.168.1.34, Dst: 212.79.111.155)
  y el segundo flujo de servidor a usuario (Src: 212.79.111.155, Dst: 192.168.1.34)
* ¿Cuántos paquetes se pierden?
  * En ninguno de los 2 flujos se pierde ningún paquete.
* Para el flujo desde LinPhone hacia Servidor: ¿cuál es el valor máximo del delta?
  * 30.834 ms
* Para el flujo desde Servidor hacia LinPhone: ¿cuál es el valor máximo del delta?
  * 59.586 ms
* ¿Qué es lo que significa el valor de delta?
  * La delta es la diferencia entre la llegada de un paquete y la llegada del paquete anterior. 
  Se encuentra en la capa de red y refleja el tiempo  de llegada entre cada paquete a la interfaz de captura.
* ¿En qué flujo son mayores los valores de jitter (medio y máximo)? 
  * Flujo LinPhone - Servidor: Max Jitter: 8.445462075089944, Mean Jitter: 4.152747555343614.
  * Flujo Servidor - LinPhone: Max Jitter: 5.769810580072752, Mean Jitter: 1.2051589504762101.
  * El flujo LinPhone - Servidor tiene mayores valores de jitter.
* ¿Cuáles son esos valores?
  * Flujo LinPhone - Servidor: Max Jitter: 8.445462075089944, Mean Jitter: 4.152747555343614.
* ¿Qué significan esos valores?
  * El jitter de paquetes es la fluctuación en el retardo de paquetes. 
  Esto se refiere a la variación en el tiempo de retardo (ms) entre paquetes de datos a través de la red.
  Si el jitter alcanza un valor elevado de tiempo de retardo podría dar lugar a congestión en la red y producirse pérdida de paquetes.
* Dados los valores de jitter que ves, ¿crees que se podría mantener una conversación de calidad?
  * En ninguno de los flujos se produce pérdida de paquetes, lo que nos indica que la red no está congestionada, esto ya es una buena señal.
  Además, los valores del jitter (medio y máximo) son bajos, inferiores a 10ms, lo que nos indica que la conversación tiene muy buena calidad.

Vamos a ver ahora los valores de un paquete concreto, el paquete 17. Vamos a analizarlo en opción `Stream Analysis`:

* ¿Cuánto valen el delta y el jitter para ese paquete?
  * Delta: 20.58 ms y Jitter: 0.10 ms
* ¿Podemos saber si hay algún paquete de este flujo, anterior a este, que aún no ha llegado?
  * El número de secuencia se encuentra ordenado por lo tanto sabemos que no se pierde ningún paquete.
* El "skew" es negativo, ¿qué quiere decir eso?
  * Significa que los paquetes llegan más tarde que el período establecido entre paquetes, 
  de 20 ms aproximadamente.

Si sigues el jitter, ves que en el paquete 78 llega a ser de 5.52:

* ¿A qué se debe esa subida desde el 0.57 que tenía el paquete 53?
  * Hasta el paquete 53 hay una periodicidad de 20 ms, a partir de ahí el periodo de llegada de paquetes varía 
  entre los 10 ms y los 30 ms. Esto afecta en el paquete 78 en que la Delta baja considerablemente (9.30ms) y el jitter aumenta, 
  ya que ambos parámetros están relacionados. 

En el panel `Stream Analysis` puedes hacer `play` sobre los streams:

* ¿Qué se oye al pulsar `play`?
  * Se oye una canción.
* ¿Qué se oye si seleccionas un `Jitter Buffer` de 1, y pulsas `play`?
  * Se escucha la misma canción pero con pequeños cortes.
* ¿A qué se debe la diferencia?
  * Al disminuir el jitter se encolan los paquetes y se produce un retardo en estos.

Sigue respondiendo las cuestiones que se plantean en este guion en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.
  
## Respuesta: Ejercicio 10. Llamadas VoIP

Podemos ver ahora la traza, analizándola como una llamada VoIP completa. Para ello, en el menú `Telephony` selecciona el menú `VoIP calls`, y selecciona la llamada hasta que te salga el panel correspondiente:

* ¿Cuánto dura la llamada?
  * **Start Time: 3.877806s - Stop Time: 14.491080s**.
  La llamada dura unos 10 segundos, aproximadamente.

Ahora, pulsa sobre `Flow Sequence`:

* Guarda el diagrama en un fichero (formato PNG) con el nombre `diagrama.png`.
* ¿En qué segundo se realiza el `INVITE` que inicia la conversación?
  * En el segundo, 3.877805840.
* ¿En qué segundo se recibe el último OK que marca su final? 
  * En el segundo, 14.491079516.

Ahora, pulsa sobre `Play Sterams`, y volvemos a ver el panel para ver la transmisión de datos de la llamada (protocolo RTP):

* ¿Cuáles son las SSRC que intervienen?
  * Src: 212.79.111.155, Dst: 192.168.1.34 -- 0x761f98b2.
  * Src: 192.168.1.34, Dst: 212.79.111.155 -- 0xeeccf15f.
* ¿Cuántos paquetes se envían desde LinPhone hasta Servidor?
  * Desde **Src: 192.168.1.34, Dst: 212.79.111.155** se envían 524 paquetes.
* ¿Cuántos en el sentido contrario?
  * Desde **Src: 212.79.111.155, Dst: 192.168.1.34** se envían 525 paquetes.
* ¿Cuál es la frecuencia de muestreo del audio?
  * La frecuencia de muestreo es de 8000 Hz, **Sample Rate(Hz): 8000**.
* ¿Qué formato se usa para los paquetes de audio?
  * Se utiliza un formato g711U de audio.

Sigue respondiendo las cuestiones que se plantean en este guion en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Respuesta: Ejercicio 11. Captura de una llamada VoIP

Dirígete a la [web de LinPhone](https://www.linphone.org/freesip/home) con el navegador y créate una cuenta SIP.  Recibirás un correo electrónico de confirmación en la dirección que has indicado al registrarte (mira en tu carpeta de spam si no es así).
  
Lanza LinPhone, y configúralo con los datos de la cuenta que te acabas de crear. Para ello, puedes ir al menú `Ayuda` y seleccionar `Asistente de Configuración de Cuenta`. Al terminar, cierra completamente LinPhone.

* Captura una llamada VoIP con el identificador SIP `sip:music@sip.iptel.org`, de unos 15 segundos de duración. Recuerda que has de comenzar a capturar tramas antes de arrancar LinPhone para ver todo el proceso. Guarda la captura en el fichero `linphone-music.pcapng`. Procura que en la captura haya sólo paquetes entre la máquina donde has hecho la captura y has ejecutado LinPhone, y la máquina o máquinas que han intervenido en los intercambios SIP y RTP con ella.
* ¿Cuántos flujos tiene esta captura?
  * La captura se compone de dos flujos.
    * 1º Flujo: **Source Address: 212.79.111.155, Source Port: 26186, Destination Address: 212.128.255.43, Destination Port: 7078**. 
    * 2º Flujo: **Source Address: 212.128.255.43, Source Port: 7078, Destination Address: 212.79.111.155, Destination Port: 26186**.
* ¿Cuánto es el valor máximo del delta y los valores medios y máximo del jitter de cada uno de los flujos? 
  * 1º Flujo: **Max Delta (ms): 26.235781999999745, Max Jitter: 1.0277200051537116, Mean Jitter: 0.3554440777142424**. 
  * 2º Flujo: **Max Delta (ms): 33.04834299999857, Max Jitter: 6.522378959045448, Mean Jitter: 2.5885184912485464**.

Sigue respondiendo las cuestiones que se plantean en este guion en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Respuesta: Ejercicio 12 (segundo periodo). Llamada LinPhone

Ponte de acuerdo con algún compañero para realizar una llamada SIP conjunta (entre los dos) usando LinPhone, de unos 15 segundos de duración.  Si quieres, usa el foro de la asignatura, en el hilo correspondiente a este ejercicio, para enconrar con quién hacer la llamada.
Realiza una captura de esa llamada en la que estén todos los paquetes SIP y RTP (y sólo los paquetes SIP y RTP). No hace falta que tu compañero realice captura (pero puede realizarla si quiere que le sirva también para este ejercicio).
Guarda tu captura en el fichero `captura-a-dos.pcapng`

Como respuesta a este ejercicio, indica con quién has realizado la llamada, quién de los dos la ha iniciado, y cuantos paquetes hay en la captura que has realizado.

* captura-a-dos_SRC.pcapng
  * **Internet Protocol Version 4, Src: 212.128.255.40, Dst: 212.128.255.48**
  * Llamada iniciada desde 'Linphone' **sip:refferenz@212.128.255.48:5060 SIP/2.0** hacia mi máquina, **sip:b.vicariog@212.128.255.40 SIP/2.0**, que actúa como servidor.
  * La captura consta de 6939 paquetes.
* captura-a-dos_DST.pcapng
  * **Internet Protocol Version 4, Src: 212.128.255.40, Dst: 212.128.255.48**
  * Llamada iniciada desde 'Linphone' **sip:b.vicariog@212.128.255.40 SIP/2.0** hacia mi máquina, **sip:namengua@212.128.255.50**, que actúa como servidor.
  * La captura consta de 9941 paquetes.
