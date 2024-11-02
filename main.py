#Dado un archivo libros.txt que contiene una lista de libros y sus autores, 
#implementa una función que busque todos los libros escritos por un autor específico y los muestre. 
#Si el autor no tiene libros en la lista, debe mostrar un mensaje indicando que no hay coincidencias.

import pdb
    
def buscarAutor(autor):   
    # Leer línea por línea con readline()
    with open("libros.txt", "r", encoding="utf-8") as archivo:
    # Itera sobre cada línea en el archivo
        for linea in archivo:   
            if autor in linea:
                print(linea)                 
            
    
autor = input("Ingrese el autor que desa buscar : ")
buscarAutor(autor)