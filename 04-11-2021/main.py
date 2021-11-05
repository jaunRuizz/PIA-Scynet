from logging import Logger
from analisis import *

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

logging.basicConfig(filename='./logging/info.log', level='DEBUG')


if __name__ == "__main__":
    # ip_public=my_ip()
    print(G+"                                                    ")
    print('      _________                           __        ')
    print('     /   _____/ ____ ___.__. ____   _____/  |_      ')
    print('     \_____  \_/ ___<   |  |/    \_/ __ \   __\     ')
    print('     /        \  \___\___  |   |  \  ___/|  |       ')
    print('     _______  /\___  > ____|___|  /\___  >__|       ')
    print('            \/     \/\/         \/     \/           '+W)

    print(C+"[+] Este proyecto fue elaborado en colaboracion de Maximiliano hernandez" 
            " , Carlos pat , Emilio  JAQUEZ , Daniel Luevano  & Jose jose ")
    print("[-] emilio.jaquezel@uanl.edu.mx ")
    print("[-] maximilianohdzlopez@gmail.com")
    print("[-] daniel.luevanoui@uanl.edu.mx")
    print("[-] carlos.patflrs@uanl.edu.mx")
    print("[-] jose.mendiolatrvn@uanl.edu.mx"+W)
    
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
