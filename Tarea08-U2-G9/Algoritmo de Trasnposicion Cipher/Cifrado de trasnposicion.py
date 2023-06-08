import time


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        texto = archivo.read()
    return texto


def escribir_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)


def generar_claves(columnas):
    claves = []
    for i in range(1, columnas + 1):
        claves.append("".join(str(d) for d in range(1, i + 1)))
    return claves


def cifrar_transposicion(texto, clave):
    filas = len(texto) // len(clave)
    if len(texto) % len(clave) != 0:
        filas += 1

    texto += (filas * len(clave) - len(texto)) * "*"

    matriz = [[''] * len(clave) for _ in range(filas)]

    indice = 0
    for i in range(filas):
        for j in range(len(clave)):
            matriz[i][j] = texto[indice]
            indice += 1

    texto_cifrado = ""
    for letra in clave:
        j = int(letra) - 1
        for i in range(filas):
            texto_cifrado += matriz[i][j]

    return texto_cifrado


def descifrar_transposicion(texto_cifrado, clave):
    filas = len(texto_cifrado) // len(clave)
    if len(texto_cifrado) % len(clave) != 0:
        filas += 1

    matriz = [[''] * len(clave) for _ in range(filas)]

    indice = 0
    for letra in clave:
        j = int(letra) - 1
        for i in range(filas):
            matriz[i][j] = texto_cifrado[indice]
            indice += 1

    texto_descifrado = ""
    for i in range(filas):
        for j in range(len(clave)):
            if matriz[i][j] != "*":
                texto_descifrado += matriz[i][j]

    return texto_descifrado


# Leer archivo con el texto a cifrar
nombre_archivo = "CifradoTranspocicion/100palabras.txt"
inicio = time.time()
texto_original = leer_archivo(nombre_archivo)
tiempo_lectura = time.time() - inicio
print("Texto original:", texto_original)
print("Tiempo de lectura:", tiempo_lectura, "segundos")

# Generar claves de cifrado
columnas = 10  # Número de columnas para las claves de cifrado
inicio = time.time()
claves = generar_claves(columnas)
tiempo_generacion_claves = time.time() - inicio
print("Claves de cifrado:", claves)
print("Tiempo de generación de claves:", tiempo_generacion_claves, "segundos")

# Cifrar texto
clave_cifrado = claves[5]  # Utilizar la cuarta clave de cifrado
inicio = time.time()
texto_cifrado = cifrar_transposicion(texto_original, clave_cifrado)
tiempo_cifrado = time.time() - inicio
print("\n Texto cifrado:", texto_cifrado)
print("Tiempo de cifrado:", tiempo_cifrado, "segundos")

# Descifrar texto
inicio = time.time()
texto_descifrado = descifrar_transposicion(texto_cifrado, clave_cifrado)
tiempo_descifrado = time.time() - inicio
print("\n Texto descifrado:", texto_descifrado)
print("Tiempo de descifrado:", tiempo_descifrado, "segundos")
print 