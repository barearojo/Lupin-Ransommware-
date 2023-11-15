# Lupin-Ransommware-
Sencillo Ransomware realizado en python3 para ver un funcionamiento básico

Lupin.py se trata del cifrador

ganimard.py es el encargado de descifrar los archivos una vez introducido la contraseña
Utiliza fernet para la codificar los archivos haciendo que sea necesaria la llave para poder decodificarlo luego
Genera una llave(laLLave.py) que luego ganimard.py utilizar para desencriptarlos.
ganimard.py pedirá una contraseña también para poder realizar su acción (gentleman-cambrioleur)

Recorre de forma recursiva los directorio inferiores cifrando todos los archivos que se encuentre. Utilización os.walk y os.path.join

Ejecución: python3 Lupin.py
Ejecución: python3 ganimard.py


