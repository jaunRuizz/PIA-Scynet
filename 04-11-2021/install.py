import os
import logging

# Abrimos el archivo logging para almacenar los errores
logging.basicConfig(filename='C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/info.log', level='DEBUG')


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
        exit()
    except:
        logging.error("Fallo la ejecucion de la funcion instalar modulos")
        pass

if __name__ == '__main__':
    install_modulos()
