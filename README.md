# PIA-Scynet
Proyecto Final de Ciberseguridad ........
<p align="center"><img src="https://lh3.googleusercontent.com/qracujYPlPttXJ1BHo4t27KN6ofLsXzOK1witnDIn9AH-QfCz2Kp-Vf1JLKnk3Rvgsi7jw=s101"></p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic">
<img src="https://img.shields.io/badge/Scynet-✔-blue.svg?style=plastic">
</p>


<p align="center">
  <br>
  <b>Documentacion</b>
  <br>
  <img src="https://www.redusers.com/noticias/wp-content/uploads/2016/04/linux-240x160.jpg">
</p>

<p>
  <a style="margin-right: 10px;" href="https://github.com/jaunRuizz/PIA-Scynet/blob/main/04-11-2021/install.py">
    <img src="https://dabuttonfactory.com/button.png?t=INSTALL&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=00e2ff">
  </a>
</p>

Scynet es una herramienta desarrollada para la elaboracion de un reporte que te dara informacion sobre la ip de una red tanto ip local como publica y podras hacer un escaneo de puertos de una ip, tenemos la opcion de mandar todos estos datos via correo electronico y un sms para saber cuando el script termino con su funcion :

* Longitude
* Latitude
* ip publica
* Puertos abiertos de una ip 
* Correos electronicos 

Realiza 5 tareas principales las cuales nos ayudaran a obtener informacion detallada en multiples reportes generados automaticamente  :

* Envio sms
* Envio de correos
* Cifrado 
* Platform
* Public IP Address
* Local IP Address
* Local Port



## Informacion de una ip publica 

*  Se hace una consulta a la API http://free.ipwhois.io/json/ la cual nos devolvera un JSON con informacion sobre dicha ip con ese formato JSON podemos sustraer la info mas  relevante y almacenarla en un txt, por ejuemplo provedor de servicios region de la ip etc.

## Tareas

Ciberseguridad : 

* Envio de Correos electronicos
* Envio de SMS
* Cifrado base 64 & Simetrico
* Escaneo de puertos & Escaneo de las ip de una red 

## Tested On :

* Kali Linux
* Ubuntu
* Parrot OS
* Windows 10/11

## Installation

### Kali Linux / Ubuntu / Parrot OS

```bash
git clone  https://github.com/jaunRuizz/PIA-Scynet.git
cd 04/11/2021
python3 install.py
python3 main.py  --help
```

### Windows10/11

``` Git bash
git clone  https://github.com/jaunRuizz/PIA-Scynet.git
cd 04/11/2021
Ejecutar con doble click el ejecutable install.exe
python main.py  --help
```

## Uso

``Git bash
python analisis.py -h

usage: main.py [-h] [-ip IP_PUBLIC] [-i IP_LOCAL] [-user USER_NAME] [-pts PUERTO] [-m MSG] [-dest NUMERO]

options:
  -h, --help       show this help message and exit
  -ip IP_PUBLIC    Ingresa la ip, si no ponesnada se tomará automatico 8.8.8.8
  -i IP_LOCAL      Ingresa la ip
  -user USER_NAME  Ingresa un username para el envio del correo
  -pts PUERTO      Ingresa los puertos a escanear ej. --> 80-90 si no ingresas nada parametro se tomara por defecto del puerto 20 al 100
  -m MSG           Ingresa el mensaje a enviar, si no ingresas mensaje no se detiene el programa
  -dest NUMERO     Ingresa el numero a dodne enviaras el mensaje

##################
# Uso Ejemplo #
##################

python .\main.py    -user ************@gmail.com  -m 'Mensaje a enviar' -dest numero destinatario   -i 192.168.0.1 -ip 8.8.8.8 o ip publica
```
