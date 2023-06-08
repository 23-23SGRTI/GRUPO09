#llamamos a los recursos necesarios para encriptar y descencriptar la informacion
from cryptography.fernet import Fernet 
import time

#metodo para generar y guardar la clave
def generaClave():
    clave=Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)

#metodo para leer la clave
def cargarClave():
    return open("clave.key","rb").read()

#metodo para encriptar el archivo
def encript(nom_archivo,clave):
    f = Fernet(clave)
    with open(nom_archivo, "rb")as file:
        archivo_info = file.read()
    encrypted_data = f.encrypt(archivo_info)
    with open(nom_archivo, "wb")as file:
        file.write(encrypted_data)



#Encriptacion-----------------------------------------------------------------------------------------------------------
##tiempo inicio de lectura de archivo
#tiempInicio = time.time() 

##leemos el archivo
#print(open("1000palabras.txt").read())

##tiempo final de lectura de archivo
#tiempoFinal = time.time();

##imprimimos el tiempo total de lectura de archivo
#print("\nTiempo de lectura de archivo:", tiempoFinal-tiempInicio,"s")


##-----------------------------------------------------------------------------------------------------------
##tiempo inicio de generacion de clave
#tiempInicio = time.time()

##generamos y leemos la clave
#generaClave()
#clave = cargarClave()

##tiempo final de generacion de clave
#tiempoFinal = time.time();

##imprimimos el tiempo total de generacion de clave
#print("\nTiempo de generacion y lectura de clave:", tiempoFinal-tiempInicio,"s\n")
##-----------------------------------------------------------------------------------------------------------


##-----------------------------------------------------------------------------------------------------------
##tiempo inicio de encriptacion e impresion del texto
#tiempInicio = time.time()

##encriptamos el archivo
#nom_archivo = "1000palabras.txt"
#encript(nom_archivo, clave)

##imprimimos la info del texto
#print(open("1000palabras.txt").read())

##tiempo final de encriptacion e impresion del texto
#tiempoFinal = time.time();

##imprimimos el tiempo total de encriptacion e impresion del texto
#print("\nTiempo de encriptacion e impresion del texto:", tiempoFinal-tiempInicio,"s")





#Desencriptacion-----------------------------------------------------------------------------------------------------------
#metodo para cargar la clave
def cargarClave():
    return open("clave.key","rb").read()


#metodo para desencriptar el archivo
def desencript(nom_archivo,clave):
    f = Fernet(clave)
    with open(nom_archivo, "rb")as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(nom_archivo, "wb")as file:
        file.write(decrypted_data)


#tiempo inicio de decifrado e impresion de informacion
tiempoInicio = time.time()

#cargamos la clave
clave = cargarClave()

#desencriptamos el archivo
nom_archivo = "1000palabras.txt"
desencript(nom_archivo, clave)

#imprimimos la info del texto
print(open("1000palabras.txt").read())

#timpo final de decifrado e impresion de informacion
tiempoFinal = time.time()

#imprimimos el tiempo de decifrado e impresion de informacion
print("\nTiempo en descifrar e imprimir la informacion:", tiempoFinal-tiempoInicio, "s")