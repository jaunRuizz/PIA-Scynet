# Desde modulos.py importa los modulos necesarios


from importa import *


# Encrypt se encarga de encriptar en Base64


def encrypt():
    hora = tiempo()
    try:
        comando = ".\base64.ps1"
        subprocess.call(["C://WINDOWS//system32//WindowsPowerShell" +
                        "//v1.0//powershell.exe", './base64.ps1'])
        logging.info(hora[0:19]+" Se ejecuto Encrypt correctamente ")
    except:
        logging.error(hora[0:19] + " Fallo Encrypt ")


# Hashes se encarga de sacar los hash de todos los archivos


def hashes():
    hora = tiempo()
    try:
        comando = ".\hashes.ps1"
        subprocess.call(["C://WINDOWS//system32//WindowsPowerShell" +
                        "//v1.0//powershell.exe", './hashes.ps1'])
        logging.info(hora[0:19]+" Se ejecuto Hashes correctamente ")
    except:
        logging.error(hora[0:19] + " Fallo Hashes ")


# Se encarga de buscar direcciones de correo electrónico de ...@uanl.edu.mx


def paiton():
    hora = tiempo()
    try:
        python = ".\APIhunter.py"
        subprocess.call(["python", './APIhunter.py'])
        logging.info(hora[0:19]+" Se ejecuto APIHUNTER correctamente ")
    except:
        logging.error(hora[0:19]+" Fallo APIHUNTER ")


# Trae la hora del sistema para usarse en logging


def tiempo():
    hora = str(datetime.datetime.now())
    return hora


# Funcion para la barra de progreso
def barra():
    bar2 = ChargingBar('Obteniendo Datos:', max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.1))
        bar2.next()
    bar2.finish()


# Argumentos de entrada del script para cada tarea


def argumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", dest="ip_public", default='8.8.8.8',
                        help="Ingresa la ip, si no pones" +
                        "nada se tomará automatico 8.8.8.8")
    parser.add_argument("-i", dest="ip_local", help="Ingresa la ip")
    parser.add_argument("-user", dest="user_name",
                        help="Ingresa un username para el envio del correo ")
    parser.add_argument("-pts", dest="puerto", default='20-30',
                        help="Ingresa los puertos a escanear ej. --> 80-90 " +
                        "si no ingresas nada parametro se tomara por defecto" +
                        " del puerto 20 al 100")
    parser.add_argument("-m", dest="msg",
                        help="Ingresa el mensaje a enviar, si no ingresas" +
                        " mensaje no se detiene el programa ")
    parser.add_argument("-dest", dest="numero",
                        help="Ingresa el numero a dodne enviaras el mensaje  ")
    mensaje = parser.parse_args()
    numero = parser.parse_args()
    puertos = parser.parse_args()
    ip_public = parser.parse_args()
    ip_local = parser.parse_args()
    user = parser.parse_args()
    return ip_local, ip_public, user, puertos, mensaje, numero


# Funcion para hacer la llamada a la API de Geolocalizacion


def geolocalizacion(ip_public):
    hora = tiempo()
    url = "http://free.ipwhois.io/json/{}".format(ip_public.ip_public)
    barra()
    soup = requests.get(url)
    data = soup.text
    data = soup.json()
    datos = open("datos.txt", "w")
    n = 1
    q = 0
    r = 0
    valor = []
    valor2 = []
    wb = openpyxl.Workbook()
    ws = wb.active
    Columna1 = ['A' + str(n)]
    for key in data:
        # que lo escriba en txt
        datos.write(key + ": " + str(data[key]) + "\n")
        # para guardar el excel
        valor.append(str(key))
        ws.cell(row=r + 1, column=1).value = str(valor[q])
        valor2.append(str(data[key]))
        ws.cell(row=r+1, column=2).value = str(valor2[q])
        n = n + 1
        q = q + 1
        r = r + 1
    wb.save('datoss.xlsx')
    datos.close()
    print("Archivo con datos de Geolocalizacion generado con exito ")
    logging.info(hora[0:19]+" Ejecucion de geolocalizacion correcta")


# Funcion para scanear las ip activas en una red local


def scan(ip_local):
    hora = tiempo()
    try:
        # Usamos argparser para pasar los argumentos por terminal
        archivo = open("ips.txt", "w")
        print("Scanning...")
        # iniciamos el scaneo
        arp_request = scapy.ARP(pdst=ip_local.ip_local+"/24")
        brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp = brodcast / arp_request
        barra()
        answered = scapy.srp(arp, timeout=1, verbose=False)[0]
        # Guardamos en un txt las ip y las mac addres
        # con un for recorriendo answered
        for element in answered:
            archivo.write("IP:{} ".format(element[1].psrc))
            archivo.write(" MAC address: {}\n ".format(element[1].hwsrc))
        archivo.close()
        print("Archivo con ip´s activas en la" +
              "red local ingresada generado con exito")
        logging.info(hora[0:19]+" Ejecucion de funcion scan correctamente")
        correcto = True
    except:
        logging.error(hora[0:19]+" Ejecucion de funcion scan fallo ")
        correcto = False
    return correcto


# Se empieza a leer el archivo que contiene las ip para almacenar en una lista


def Ports(puertos, ip_local):
    hora = tiempo()
    try:
        archivo = open('.\Data/puertos_scaneado.txt', 'w')
        ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
        port_min = 0
        port_max = 65535
        open_ports = []
        while True:
            ip_add_entered = ip_local.ip_local
            if ip_add_pattern.search(ip_add_entered):
                print(f"{ip_add_entered} is a valid ip address")
                break
        while True:
            port_range = puertos.puerto
            port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))  # *
            if port_range_valid:
                port_min = int(port_range_valid.group(1))
                port_max = int(port_range_valid.group(2))
                break
        nm = nmap.PortScanner()
        for port in range(port_min, port_max + 1):
            try:
                result = nm.scan(ip_add_entered, str(port))
                port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])  # *
                archivo.write(nm.csv()+(f"Port {port} is {port_status}")+'\n')
            except:
                print(f"Cannot scan port {port}.")
        archivo.close()
        logging.info(hora[0:19]+" Ejecucion de funcion ports correctamente")
    except:
        logging.error(hora[0:19]+" Ejecucion de funcion ports fallo")
        pass


# Trae tu propia IP publica


def my_ip():
    hora = tiempo()
    try:
        url1 = 'https://www.cual-es-mi-ip.net/'
        # Peticiones a cada uno de los links
        page1 = requests.get(url1)
        soup1 = BeautifulSoup(page1.content, "html.parser")
        origen = soup1.find_all("span", class_="big-text font-arial")
        for i in origen:
            ip_public = i.text
        code = page1.status_code
        if code == 200:
            return ip_public
        else:
            ip = ''
        logging.info(hora[0:19]+" Ejecucion de funcion my_ip correctamente")
    except:
        logging.error(hora[0:19]+" Ejecucion de funcion my_ip fallo")
        pass


# Por medio de la API de Twilio, envía un mensaje de texto a un número telefónico


def enviar_sms(numero, mensaje):
    hora = tiempo()
    try:
        archivo = open('.\llaves\llaves.txt')
        claves = []
        lineas = archivo.readlines()
        for linea in lineas:
            claves.append(linea)
        archivo.close()
        accountSID = claves[0]
        authToken = claves[1]
        twilioCli = Client(accountSID, authToken)

        myTwilioNumber = claves[2]

        destCellPhone = '+52'+numero.numero

        msg = mensaje.msg
        message = twilioCli.messages.create(to=destCellPhone,
                                            from_=myTwilioNumber,
                                            body=msg)
        print(message.to)
        logging.info(hora[0:19]+" Ejecucion de funcion" +
                     " enviar_sms correctamente")
    except:
        logging.error(hora[0:19]+" Ejecucion de funcion enviar_sms fallo")
        pass


# Se encarga de enviar archivos por correo


def enviar_correo(user):
    hora = tiempo()
    try:
        archivo = open('./llaves/pass.txt', 'r')
        contraseña = archivo.readline()
        archivo = open("./llaves/Correos.txt")
        correos = []
        lineas = archivo.readlines()
        for linea in lineas:
            correos.append(linea.rstrip())
        fromaddr = user.user_name
        password = contraseña
        toaddrs = correos

        content = 'Este es el reporte de fin de mes. ' + hora[0:19]
        textApart = MIMEText(content)

        datosFile = '.\datos.txt'
        datosApart = MIMEImage(open(datosFile, 'rb').read(), datosFile.split('.')[-1])  # *
        datosApart.add_header('Content-Disposition', 'attachment', filename="datos.txt")  # *

        ipsFile = '.\ips.txt'
        ipsApart = MIMEApplication(open(ipsFile, 'rb').read())
        ipsApart.add_header('Content-Disposition', 'attachment', filename="ip's.txt")  # *

        correosFile = '.\Data\correos.txt'
        correosApart = MIMEApplication(open(correosFile, 'rb').read())
        correosApart.add_header('Content-Disposition', 'attachment', filename="correos.txt")  # *
        
        infoFile = '.\logging\info.log'
        infoApart = MIMEApplication(open(infoFile, 'rb').read())
        infoApart.add_header('Content-Disposition', 'attachment', filename="info.log")  # *

        m = MIMEMultipart()
        m.attach(textApart)
        m.attach(datosApart)
        m.attach(ipsApart)
        m.attach(correosApart)
        # m.attach(uanlApart)
        m.attach(infoApart)
        m['Subject'] = 'Reporte'

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:  # *
                server.login(fromaddr, password)
                server.sendmail(fromaddr, toaddrs, m.as_string())
                print('Envio Correos Exitoso')
                server.quit()
        except smtplib.SMTPException as e:
                print ('error:', e)  # Error de impresión
        logging.info(hora[0:19]+" Ejecucion de funcion" +
                     "enviar correo correctamente")
    except:
        logging.error(hora[0:19]+" Ejecucion de funcion enviar correo fallo")
        pass


# Realiza cifrado asimetrico de una lista de archivos .txt


def cifrado():
    try:
        archivos = ['CLave-API.txt', 'llaves.txt', 'pass.txt']
        encrypt = open(".\cript.txt", "wb")
        c = 0
        for i in range(len(archivos)):
            modulos = open(".\llaves\{}".format(archivos[c]), "rb")
            c += 1
            lineas = modulos.readlines()
            for palabras in lineas:
                texto = (palabras.strip())
                clave = Fernet.generate_key()
                f = Fernet(clave)
                token = f.encrypt(texto)
                encrypt.write(token+b"\n")
        encrypt.close()
        os.system("move ./cript.txt ./bas")
        logging.info("Se ejecuto cifrado simetrico con éxito")
    except:
        logging.error("Fallo cifrado Simetrico")
        pass
