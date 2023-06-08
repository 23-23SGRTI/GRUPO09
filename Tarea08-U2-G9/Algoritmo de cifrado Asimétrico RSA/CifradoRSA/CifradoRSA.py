#importamos las librerias necesarias
import Crypto
from Crypto.PublicKey import RSA #codificar
import binascii
from Crypto.Cipher import PKCS1_OAEP 
import time 


#Encriptacion----------------------------------------------------------------------------------------------------
##generamos un numero random
#random_generator = Crypto.Random.new().read


##tiempo inicio de generacion de clave
#tiempInicio = time.time()

##generamos la llave privada para despues generar la llave publica
#private_key = RSA.generate(1024, random_generator)
#public_key = private_key.publickey()

##tiempo final de generacion de clave
#tiempoFinal = time.time();

##imprimimos el tiempo total de generacion de clave
#print("\nTiempo de generacion y lectura de clave:", tiempoFinal-tiempInicio,"s\n")



##exportamos las llaves en formato binario
#private_key = private_key.exportKey(format='DER')
#public_key = public_key.exportKey(format='DER')
##transformamos las llaves a formato utf8
#private_key = binascii.hexlify(private_key).decode('utf8')
#public_key = binascii.hexlify(public_key).decode('utf8') 



##imprimimos las llaves
#print('Llave privada:')
#print(private_key)
#print()
#print('Llave publica:')
#print(public_key)



##proceso a la inversa para convertir de utf-8 a un objeto tipo llave
#private_key = RSA.import_key(binascii.unhexlify(private_key))
#public_key= RSA.import_key(binascii.unhexlify(public_key))



##tiempo inicio de lectura de archivo
#tiempInicio = time.time() 

##leemos el archivo y creamos el objeto PKCS1_OAEP de la clase importada con el que encriptamos el mensaje
#message = open("10caracteres.txt").read()
#message = message.encode()
#cipher = PKCS1_OAEP.new(public_key) 

##tiempo final de lectura de archivo
#tiempoFinal = time.time();

##imprimimos el tiempo total de lectura de archivo
#print("\nTiempo de lectura de archivo:", tiempoFinal-tiempInicio,"s")





##tiempo inicio de encriptacion e impresion del texto
#tiempInicio = time.time()

##encriptamos el mensaje y lo imprimimos
#encrypted_message = cipher.encrypt(message)
#print()
#print("Mensaje encriptado:")
#print(encrypted_message)

##tiempo final de encriptacion e impresion del texto
#tiempoFinal = time.time();

##imprimimos el tiempo total de encriptacion e impresion del texto
#print("\nTiempo de encriptacion e impresion del texto:", tiempoFinal-tiempInicio,"s")




##guardamos el mensaje encriptado en el archivo
#f = open("10caracteres.txt", "wb")
#f.write(encrypted_message)
#f.close()



#Desencriptacion------------------------------------------------------------------------------------------------------
#tiempo inicio de decifrado e impresion de informacion
tiempoInicio = time.time()
cipher = PKCS1_OAEP.new(private_key)
message = cipher.decrypt(encrypted_message)
print()
print("Mensaje desencriptado:")
print(message)

#timpo final de decifrado e impresion de informacion
tiempoFinal = time.time()

#imprimimos el tiempo de decifrado e impresion de informacion
print("\nTiempo en descifrar e imprimir la informacion:", tiempoFinal-tiempoInicio, "s")


#guardamos el mensaje desencriptado en el archivo
f = open("10caracteres.txt", "wb")
f.write(message)
f.close()
