#Tienes un archivo inventario.csv que contiene una lista de libros y el número de copias disponibles. 
#Escribe un programa que permita actualizar la cantidad de copias de un libro específico. 
#El programa debe leer el archivo, modificar el número de copias y volver a escribir el archivo.
# Leer el archivo CSV y guardar los datos en una lista

import csv

# Ruta al archivo CSV
ruta_archivo = "libros.csv"
libros = []
with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
    lector_csv = csv.reader(archivo)
    encabezado = next(lector_csv)  # Leer la cabecera
    
    # Leer cada fila y agregarla a la lista de libros
    for fila in lector_csv:
        libros.append({"titulo": fila[0], "autor": fila[1], "copias": int(fila[2])})
        print(f'"titulo": "{fila[0]}", "autor": "{fila[1]}", "copias": {int(fila[2])}')


# Pedir al usuario el título del libro y el nuevo número de copias
titulo_buscar = input("Ingrese el título del libro a modificar: ")
nuevas_copias = int(input("Ingrese el nuevo número de copias disponibles: "))

# Modificar el número de copias del libro especificado
encontrado = False
for libro in libros:
    if libro["titulo"].lower() == titulo_buscar.lower():
        libro["copias"] = nuevas_copias
        encontrado = True
        print(f"El número de copias de '{titulo_buscar}' ha sido actualizado a {nuevas_copias}.")
        break

if not encontrado:
    print(f"No se encontró un libro con el título '{titulo_buscar}'.")

# Escribir los cambios de vuelta al archivo CSV
with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
    escritor_csv = csv.writer(archivo)
    
    # Escribir la cabecera
    escritor_csv.writerow(encabezado)
    
    # Escribir los datos de cada libro con los cambios
    for libro in libros:
        escritor_csv.writerow([libro["titulo"], libro["autor"], libro["copias"]])

print("Archivo CSV actualizado con éxito.")