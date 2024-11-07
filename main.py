import re


def contar_palabras(archivo):
   #Cuenta la frecuencia de cada palabra en un archivo de texto y muestra las 5 palabras más comunes.
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            texto = file.read().lower()  # Lee todo el texto y convierte a minúsculas para evitar duplicados
            
           
            # Utilizamos expresiones regulares para extraer solo las palabras
            palabras = re.findall(r'\b\w+\b', texto)
           
            diccionarioDePalabras = {}
            for palabra in palabras:
                if palabra in diccionarioDePalabras:
                    diccionarioDePalabras[palabra] += 1  # Incrementa en 1 la frecuencia
                else:
                    diccionarioDePalabras[palabra] = 1
            
            # Convertir el diccionario en una lista de tuplas y ordenar por valor de mayor a menor
            arreglo_ordenado = sorted(diccionarioDePalabras.items(), key=lambda x: x[1], reverse=True)[:5]

            # Mostrar el resultado
            print(arreglo_ordenado)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no fue encontrado.")

# Ejecución de la función
contar_palabras("texto.txt")
