# Lupin y Ganimard - Herramientas de Encriptación y Desencriptación

Este proyecto consiste en dos scripts escritos en Python, Lupin y Ganimard, que se utilizan para cifrar y descifrar archivos respectivamente. El propósito principal de estos scripts es proporcionar una demostración básica de un ransomware y su herramienta asociada para la recuperación de archivos.

## Lupin.py

Lupin.py es el componente de cifrado del proyecto. Su función es recorrer de forma recursiva los directorios, cifrar todos los archivos encontrados, y generar una llave que será necesaria para la posterior descifrado. Utiliza la biblioteca cryptography para la generación y gestión de claves Fernet.

### Ejecución:
```bash
python3 Lupin.py
```

## Ganimard.py

Ganimard.py es el componente de descifrado del proyecto. Después de solicitar una contraseña al usuario, recorre de forma recursiva los directorios cifrados por Lupin.py y utiliza la llave generada previamente para descifrar los archivos. También utiliza la biblioteca cryptography para la gestión de claves Fernet.

### Contraseña por defecto:
gentleman-cambrioleur


### Ejecución:
```bash
python3 ganimard.py


## Uso

1. Ejecute Lupin.py para cifrar los archivos del sistema.
2. Para descifrar los archivos, ejecute Ganimard.py e introduzca la contraseña cuando se le solicite.

**Nota:** Es importante tener en cuenta que este proyecto se proporciona únicamente con fines educativos y de demostración. No se debe utilizar para propósitos maliciosos ¡Advertencia! El uso indebido de este software puede resultar en daños irreversibles a los archivos del sistema. Utilice con responsabilidad y solo con fines educativos.


## Dependencias
- Python 3.x
- cryptography
