from logging import Logger
from analisis import *

logging.basicConfig(filename='./logging/info.log', level='DEBUG')


if __name__ == "__main__":
    # ip_public=my_ip()
    ip_local, ip_public, user, puertos, mensaje, numero = argumentos()
    geolocalizacion(ip_public)
    correcto = scan(ip_local)
    Ports(puertos, ip_local)
    enviar_sms(numero, mensaje)
    paiton()
    enviar_correo(user)
    cifrado()
    if correcto is True:
        encrypt()
        print("Esperando ejecucion de hash")
        time.sleep(6)
        hashes()
    else:
        print("Esperando ejecucion de hash")
        time.sleep(6)
        hashes()
        pass
