import hashlib
import time

#metodo que convierte lo que le pasemos a hexadecimal
#variable h es el objeto que contiene el hash
def hashAHexadecimal(h):
    cadena=h.hexdigest()
    return cadena

ruta = "1000palabras.txt"

#tiempo inicio de lectura de archivo
tiempInicio = time.time()

#leemos el archivo
datos = open(ruta).read()
print("Texto claro:", datos)

#tiempo final de lectura de archivo
tiempoFinal = time.time();

#imprimimos el tiempo total de lectura de archivo
print("\nTiempo de lectura de archivo:", tiempoFinal-tiempInicio,"s")



bdatos = bytes(datos, 'utf-8') #el texto primero debe codificarse en bytes
algoritmo = "sha256" #especificamos el algoritmo que vamos a usar

#tiempo inicio de la obtencion del hash del texto
tiempInicio = time.time()

#obtenemos el hash
h = hashlib.new(algoritmo, bdatos)

#tiempo final de la obtencion del hash del texto
tiempoFinal = time.time();

#imprimimos el tiempo total de obtencion del hash
print("\nTiempo de Obtención del hash:", tiempoFinal-tiempInicio,"s")

print("\nHash del texto:", hashAHexadecimal(h)) #imprimimos el hash en hexadecimal