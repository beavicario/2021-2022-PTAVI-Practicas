# Protocolos para la transmisión de audio y video en Internet
# Práctica 5. Sesión SIP

**Nota:** Esta práctica se puede entregar para su evaluación como parte de
la nota de prácticas, pudiendo obtener el estudiante hasta un 0.7 puntos. Para
las instrucciones de entrega, mira al final del documento. Para la evaluación
de esta entrega se valorará el correcto funcionamiento de lo que se pide y el
seguimiento de la guía de estilo de Python.

**Conocimientos previos necesarios:**

* Nociones de uso de wireshark (pero repasaremos todo lo que haga falta)
* Nociones de SIP y RTP (las vistas en clase de teoría)

**Tiempo estimado:** 10 horas

**Repositorio plantilla:** https://gitlab.etsit.urjc.es/ptavi/2021-2022/ptavi-p5-21

**Fecha de entrega parte individual:** 18 de noviembre de 2021, 23:59 (hasta ejercicio 11, incluido)

**Fecha de entrega parte interoperación:** 22 de noviembre de 2021, 23:59 (ejercicio 12)

## Introducción

El protocolo de iniciación de sesión (SIP) es un protocolo que se limita solamente al establecimiento y control de una sesión ([RFC 3261](https://www.rfc-editor.org/rfc/rfc3261)). Los detalles del intercambio de datos, como por ejemplo la codificación o decodificación del audio/vídeo, no son controlados por SIP sino que se llevan a cabo por otros protocolos (por ejemplo, [RTP](https://www.rfc-editor.org/rfc/rfc3550.html)). Los principales objetivos de SIP son:

* SIP permite el establecimiento de una localización de usuario (o sea, traducir de un nombre de usuario a su dirección de red actual)
* SIP provee funcionalidad para la negociación de las características de una sesión, de manera que los participantes en una sesión pueden consensuar características soportadas por todos ellos.
* SIP es un mecanismo para la gestión de llamadas, por ejemplo para añadir, eliminar o transferir participantes
* SIP permite la modificación de características de la sesión durante su transcurso.

## Objetivos de la práctica

* Conocer el protocolo SIP y otros protocolos utilizados en una sesión con clientes SIP (como _Ekiga_ o _Linphone_).
* Profundizar en el uso de _Wireshark_: análisis, captura y filtrado.


## Ejercicio 1. Creación de repositorio para la práctica

Con el navegador, dirígete al [repositorio plantilla de esta práctica](https://gitlab.etsit.urjc.es/ptavi/2021-2022/ptavi-p5-21) y realiza un fork, de manera que consigas tener una copia del repositorio en tu cuenta de GitLab. Clona el repositorio que acabas de crear a local para poder editar los archivos. Trabaja a partir de ahora en ese repositorio, sincronizando los cambios que vayas realizando según los ejercicios que se comentan a continuación (haciendo commit y subiéndolo a tu repositorio en el GitLab de la ETSIT).

## Ejercicio 2. Prepara la respuesta

Se ha capturado una sesión SIP con el cliene SIP Linphone (archivo `linphone-call.pcapng`), que se puede abrir con _Wireshark_: desde la shell: `wireshark linphone-call.pcapng` (recuerda que puedes utilizar el tabulador en la shell para autocompletar). Se pide rellenar las cuestiones que se plantean en este guión en el fichero `respuesta.md`, que crearás en el repositorio (y que subiŕas tu repositorio en el GitLab de la ETSIT para su corrección).

Para crear el fichero `respuesta.md`, copia este documento, en formato Markdown, desde el ejercicio siguiente (incluido) en adelante, de forma que tengas los enunciados de las preguntas en él, y responde a cada una de las preguntas abriendo, tras el ejercicio correspondiente, una sección `## Respuesta n` donde escribas la respuesta.

## Ejercicio 3. Análisis general

* ¿Cuántos paquetes componen la captura?
* ¿Cuánto tiempo dura la captura?
* ¿Qué IP tiene la máquina donde se ha efectuado la captura? ¿Se trata de una IP pública o de una IP privada? ¿Por qué lo sabes?

Antes de analizar las tramas, mira las estadísticas generales que aparecen en el menú de `Statistics`. En el apartado de jerarquía de protocolos (`Protocol Hierarchy`) se puede ver el número de paquetes y el tráfico correspondiente a los distintos protocolos.

* ¿Cuáles son los tres principales protocolos de nivel de aplicación por número de paquetes?
* ¿Qué otros protocolos podemos ver en la jerarquía de protocolos?
* ¿Qué protocolo de nivel de aplicación presenta más tráfico, en bytes por segundo? ¿Cuánto es ese tráfico?

Observa por encima el flujo de tramas en el menú de `Statistics` en `IO Graphs`. La captura que estamos viendo incluye desde la inicialización (registro) de la aplicación hasta su finalización, incluyendo una llamada. 

* Filtra por `sip` para conocer cuándo se envían paquetes SIP. ¿En qué segundos tienen lugar esos envíos?
* Y los paquetes con RTP, ¿cuándo se empiezan a enviar?
* Los paquetes RTP, ¿cuándo se dejan de enviar?
* Los paquetes RTP, ¿cada cuánto se envían?

Sigue respondiendo las cuestiones que se plantean en este guión en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Ejercicio 4. Primeras tramas

Analiza ahora las dos primeras tramas de la captura. Cuando se pregunta por máquinas, llama "Linphone" a la máquina donde está funcionando el cliente SIP, y "Servidor" a la máquina que proporciona el servicio SIP.

* ¿De qué protocolo de nivel de aplicación son?
* ¿Cuál es la dirección IP de la máquina "Linphone"?
* ¿Cuál es la dirección IP de la máquina "Servidor"?
* ¿En qué máquina está el UA (user agent)?
* ¿Entre qué máquinas se envía cada trama?
* ¿Que ha ocurrido para que se envíe la primera trama?
* ¿Qué ha ocurrido para que se envíe la segunda trama?

Ahora, veamos las dos tramas siguientes.

* ¿De qué protocolo de nivel de aplicación son?
* ¿Entre qué máquinas se envía cada trama?
* ¿Que ha ocurrido para que se envíe la primera de ellas (tercera trama en la captura)?
* ¿Qué ha ocurrido para que se envíe la segunda de ellas (cuarta trama en la captura)?

Ahora, las tramas 5 y 6.

* ¿De qué protocolo de nivel de aplicación son?
* ¿Entre qué máquinas se envía cada trama?
* ¿Que ha ocurrido para que se envíe la primera de ellas (quinta trama en la captura)?
* ¿Qué ha ocurrido para que se envíe la segunda de ellas (sexta trama en la captura)?
* ¿Qué se indica (en líneas generales) en la parte SDP de cada una de ellas?

Después de la trama 6, busca la primera trama SIP.

* ¿Qué trama es?
* ¿De qué máquina a qué máquina va?
* ¿Para qué sirve?
* ¿Puedes localizar en ella qué versión de Linphone se está usando?

Sigue respondiendo las cuestiones que se plantean en este guión en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Ejercicio 5. Tramas especiales

Las tramas 7 y 9 parecen un poco especiales:

* ¿De que protocolos son (indica todos los protocolos relevantes por encima de IP).
* De qué máquina a qué máquina van?
* ¿Para qué crees que sirven?

Sigue respondiendo las cuestiones que se plantean en este guión en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Ejercicio 6. Registro

Repasemos ahora qué está ocurriendo (en lo que al protocolo SIP se refiere) en las primeras tramas SIP que hemos visto ya:

* ¿Qué dirección IP tiene el servidor que actúa como registrar SIP? ¿Por qué?
* ¿A qué puerto (del servidor Registrar) se envían los paquetes SIP?
* ¿Qué método SIP utiliza el UA para registrarse?
* ¿Qué diferencia fundamental ves entre la primera línea del paquete SIP que envía Linphone para registrar a un usuario, y el que hemos estado enviando en la práctica 4?
* ¿Por qué tenemos dos paquetes `REGISTER` en la traza?
* ¿Por qué la cabecera `Contact` es diferente en los paquetes 1 y 3? ¿Cuál de las dos cabeceras es más "correcta", si nuestro interés es que el UA sea localizable?
* ¿Qué tiempo de validez se está dando para el registro que pretenden realizar los paquetes 1 y 3?

Para responder estas preguntas, puede serte util leer primero [Understanding REGISTER Method](https://blog.wildix.com/understanding-register-method/), además de tener presente lo explicado en clase.

Sigue respondiendo las cuestiones que se plantean en este guión en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Ejercicio 7. Indicación de comienzo de conversación

* Además de REGISTER, ¿podrías decir qué instrucciones SIP entiende el UA?
* ¿En qué paquete el UA indica que quiere comenzar a intercambiar datos de audio con otro? ¿Qué método SIP utiliza para ello?
* ¿Con qué dirección quiere intercambiar datos de audio el UA?
* ¿Qué protocolo (formato) está usando para indicar cómo quiere que sea la conversación?
* En la inidicacion de cómo quiere que sea la conversación, puede verse un campo `m` con un valor que empieza por `audio 7078`. ¿Qué indica el `7078`? ¿Qué relación tiene con el destino de algunos paquetes que veremos más adelante en la trama? ¿Qué paquetes son esos?
* En la respuesta a esta indicacion vemos un campo `m` con un valor que empieza por `audio 27138`. ¿Qué indica el `27138`?  ¿Qué relación tiene con el destino de algunos paquetes que veremos más adelante en la trama? ¿Qué paquetes son esos?
* ¿Para qué sirve el paquete 11 de la trama?

Sigue respondiendo las cuestiones que se plantean en este guión en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Ejercicio 8. Primeros paquetes RTP

Vamos ahora a centrarnos en los paquetes RTP. Empecemos por el paquete 12 de la traza:

* ¿De qué máquina a qué máquina va?
* ¿Qué tipo de datos transporta?
* ¿Qué tamaño tiene?
* ¿Cuántos bits van en la "carga de pago" (payload)
* ¿Se utilizan bits de padding?
* ¿Cuál es la periodicidad de los paquetes según salen de la máquina origen?
* ¿Cuántos bits/segundo se envían?

Y ahora, las mismas preguntas para el paquete 14 de la traza:

* ¿De qué máquina a qué máquina va?
* ¿Qué tipo de datos transporta?
* ¿Qué tamaño tiene?
* ¿Cuántos bits van en la "carga de pago" (payload)
* ¿Se utilizan bits de padding?
* ¿Cuál es la periodicidad de los paquetes según salen de la máquina origen?
* ¿Cuántos bits/segundo se envían?

Sigue respondiendo las cuestiones que se plantean en este guión en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Ejercicio 9. Flujos RTP

Vamos a ver más a fondo el intercambio RTP. Busca en el menú `Telephony` la opción `RTP`. Empecemos mirando los flujos RTP.

* ¿Cuántos flujos hay? ¿por qué?
* ¿Cuántos paquetes se pierden?
* Para el flujo desde LinPhone hacia Servidor: ¿cuál es el valor máximo del delta?
* Para el flujo desde Servidor hacia LinPhone: ¿cuál es el valor máximo del delta?
* ¿Qué es lo que significa el valor de delta?
* ¿En qué flujo son mayores los valores de jitter (medio y máximo)?
* ¿Cuáles son esos valores?
* ¿Qué significan esos valores?
* Dados los valores de jitter que ves, ¿crees que se podría mantener una conversación de calidad?

Vamos a ver ahora los valores de un paquete concreto, el paquete 17. Vamos a analizarlo en opción `Stream Analysis`:

* ¿Cuánto valen el delta y el jitter para ese paquete?
* ¿Podemos saber si hay algún paquete de este flujo, anterior a este, que aún no ha llegado?
* El "skew" es negativo, ¿qué quiere decir eso?

Si sigues el jitter, ves que en el paquete 78 llega a ser de 5.52:

* ¿A qué se debe esa subida desde el 0.57 que tenía el paquete 53?

En el panel `Stream Analysis` puedes hacer `play` sobre los streams:

* ¿Qué se oye al pulsar `play`?
* ¿Qué se oye si seleccionas un `Jitter Buffer` de 1, y pulsas `play`?
* ¿A qué se debe la diferencia?

Sigue respondiendo las cuestiones que se plantean en este guión en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.
  
## Ejercicio 10. Llamadas VoIP

Podemos ver ahora la traza, analizándola como una llamada VoIP completa. Para ello, en el menú `Telephony` seleccina el menú `VoIP calls`, y selecciona la llamada hasta que te salga el panel correspondiente:

* ¿Cuánto dura la llamada?

Ahora, pulsa sobre `Flow Sequence`:

* Guarda el diagrama en un fichero (formato PNG) con el nombre `diagrama.png`.
* ¿En qué segundo se realiza el `INVITE` que inicia la conversación?
* ¿En qué segundo se recibe el último OK que marca su final?
  
Ahora, pulsa sobre `Play Sterams`, y volvemos a ver el panel para ver la transmisión de datos de la llamada (protocolo RTP):

* ¿Cuáles son las SSRC que intervienen?
* ¿Cuántos paquetes se envían desde LinPhone hasta Servidor?
* ¿Cuántos en el sentido contrario?
* ¿Cuál es la frecuencia de muestreo del audio?
* ¿Qué formato se usa para los paquetes de audio?

Sigue respondiendo las cuestiones que se plantean en este guión en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## Ejercicio 11. Captura de una llamada VoIP

Dirígete a la [web de LinPhone](https://www.linphone.org/freesip/home) con el navegador y créate una cuenta SIP.  Recibirás un correo electrónico de confirmación en la dirección que has indicado al registrarte (mira en tu carpeta de spam si no es así).
  
Lanza LinPhone, y configúralo con los datos de la cuenta que te acabas de crear. Para ello, puedes ir al menú `Ayuda` y seleccionar `Asistente de Configuración de Cuenta`. Al terminar, cierra completamente LinPhone.

* Captura una llamada VoIP con el identificador SIP `sip:music@sip.iptel.org`, de unos 15 segundos de duración. Recuerda que has de comenzar a capturar tramas antes de arrancar LinPhone para ver todo el proceso. Guarda la captura en el fichero `linphone-music.pcapng`. Procura que en la captura haya sólo paquetes entre la máquina donde has hecho la captura y has ejecutado LinPhone, y la máquina o máquinas que han intervenido en los intercambios SIP y RTP con ella.
* ¿Cuántos flujos tiene esta captura?
* ¿Cuánto es el valor máximo del delta y los valores medios y máximo del jitter de cada uno de los flujos?

Sigue respondiendo las cuestiones que se plantean en este guión en el fichero `respuesta.md` (respondiendo en una nueva sección de respuesta, como se ha indicado).
Al terminar el ejercicio es recomendable hacer commit de los ficheros modificados.

## ¿Qué se valora de esta la práctica?

Valoraremos de esta práctica sólo lo que esté en la rama principal de
tu repositorio, creado de la forma que hemos indicado (como fork del repositorio plantilla que os proporcionamos). Por lo tanto, aségurate de que está en él todo lo que has realizado.

Además, ten en cuenta:

* Se valorará que haya realizado al menos haya ocho commits, correspondientes más o menos con los ejercicios pedidos, en al menos dos días diferentes, sobre la rama principal del repositorio.
* Se valorará que el fichero de respuestas esté en formato Markdown correcto.
* Se valorará que esté el texto de todas las preguntas en el fichero de respuestas, tal y como se indica al principio de este enunciado.
* Se valorará que las respuestas sean fáciles de entender, y estén correctamente relacionadas con las preguntas.
* Se valorará que la captura que se pide tenga exactamente lo que se pide.
* Se valorará que el fichero con el diagrama de la llamada VoIP tenga solo ese diagrama, en el formato que se indica en el enunciado.
* Parte de la corrección será automática, así que asegúrate de que los nombres que utilizas para los archivos son los mismos que indica el enunciado.

## ¿Cómo puedo probar esta práctica?

Cuando tengas la práctica lista, puedes realizar una prueba general, de que los ficheros en el directorio de entrega son los adecuados, y alguna otra comprobación. Para ello, ejecuta el archivo `check.py`, bien en PyCharm, o bien desde la línea de comandos:

```shell
python3 check.py
```

## Ejercicio 12 (segundo periodo). Llamada LinPhone

Ponte de acuerdo con algún compañero para realizar una llamada SIP conjunta (entre los dos) usando LinPhone, de unos 15 segundos de duración.  Si quieres, usa el foro de la asignatura, en el hilo correspondiente a este ejercicio, para enconrar con quién hacer la llamada.

Realiza una captura de esa llamada en la que estén todos los paquetes SIP y RTP (y sólo los paquetes SIP y RTP). No hace falta que tu compañero realice captura (pero puede realizarla si quiere que le sirva también para este ejercicio).

Guarda tu captura en el fichero `captura-a-dos.pcapng`

Como respuesta a este ejercicio, indica con quién has realizado la llamada, quién de los dos la ha iniciado, y cuantos paquetes hay en la captura que has realizado.
