TAM_MAX_CLAVE = 25
import time


def obtenerMensaje():

    f=open("100palabras.txt","r")
    ms= f.read()
    f.close()
    return ms



def obtenerMensajeTraducido(modo, mensaje, clave):

    

     if modo[0] == 'd':
         clave= -clave

     traduccion = ''


     for simbolo in mensaje:

         if simbolo.isalpha():

             num = ord(simbolo)

             num += clave



             if simbolo.isupper():

                 if num > ord('Z'):

                     num -= 26

                 elif num < ord('A'):

                     num += 26

             elif simbolo.islower():

                 if num > ord('z'):

                     num -= 26

                 elif num < ord('a'):

                     num += 26



             traduccion += chr(num)
             f=open("100palabras.txt","w")
             f.write(traduccion)

         else:

             traduccion += simbolo
             f = open("100palabras.txt", "w")
             f.write(traduccion)

     f = open("100palabras.txt", "r")
     return (f.read())



#Encriptamos---------------------------------------------------------------------------------------------------

##tiempo inicio de lectura de archivo
#tiempInicio = time.time() 

##leemos el archivo
#mensaje = obtenerMensaje()
#print('Texto claro:')
#print(mensaje)

##tiempo final de lectura de archivo
#tiempoFinal = time.time();

##imprimimos el tiempo total de lectura de archivo
#print("\nTiempo de lectura de archivo:", tiempoFinal-tiempInicio,"s")


#clave = 2

##tiempo inicio de encriptacion e impresion del texto
#tiempInicio = time.time()

##encriptamos el archivo
#print('\nTexto encriptado:')
#print(obtenerMensajeTraducido('e', mensaje, clave))

##tiempo final de encriptacion e impresion del texto
#tiempoFinal = time.time();

##imprimimos el tiempo total de encriptacion e impresion del texto
#print("\nTiempo de encriptacion e impresion del texto:", tiempoFinal-tiempInicio,"s")



#Desencriptamos------------------------------------------------------------------------------------------------------

mensaje = obtenerMensaje()
print('Texto encriptado:')
print(mensaje)

clave = 2

#tiempo inicio de decifrado e impresion de informacion
tiempoInicio = time.time()

print('\nTexto claro:')
print(obtenerMensajeTraducido('d', mensaje, clave))

#timpo final de decifrado e impresion de informacion
tiempoFinal = time.time()

#imprimimos el tiempo de decifrado e impresion de informacion
print("\nTiempo en descifrar e imprimir la informacion:", tiempoFinal-tiempoInicio, "s")

