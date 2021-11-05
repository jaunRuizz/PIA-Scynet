import os
import logging

# Abrimos el archivo logging para almacenar los errores
logging.basicConfig(filename='./install.log', level='DEBUG')




def mkdir():
    try:
        carpetas = ['bas','Data','Encriptado','hashes']
        c=0
        for name in carpetas:
            os.system('mkdir ' + str(carpetas[c]))
            c+=1
        logging.info("Se ejecuto correctamente la" +
                     " funcion crear directorios ")
    except:
        logging.error("Fallo la ejecucion de la funcion crear directorios")
        pass

def install_modulos():
    try:
        modulos = open("Librerias/Modulos.txt", "r")
        lineas = modulos.readlines()
        for linea in lineas:
            os.system('pip install ' + str(linea))
            print('Instalado ' + str(linea))
        modulos.close()
        logging.info("Se ejecuto correctamente la" +
                     " funcion e instalar de modulos ")
    except:
        logging.error("Fallo la ejecucion de la funcion instalar modulos")
        pass

if __name__ == '__main__':
    install_modulos()
    mkdir()