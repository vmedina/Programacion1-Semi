# Desafío 2: Ordenar el Inventario de Libros

#Como encargado de la biblioteca, necesitas organizar los libros de acuerdo con sus 
# códigos de identificación en orden decreciente, sin modificar la lista original. 
# Se recomienda usar la función sorted(). ¿Por qué es importante no modificar la lista original? 
# ¿Por qué no puedo usar el método sort sobre la lista original?


# Lista de ISBN de libros
isbn_libros = [
    "978-0-307-40676-8",
    "978-3-16-148410-0", 
    "978-0-262-13472-9", 
    "978-1-56619-909-4", 
    "978-0-395-19395-8"
   
]

copy_list_isbn_libros =isbn_libros.copy()
lista_ordenada = sorted(copy_list_isbn_libros, reverse=True)
print('lista ordenada',lista_ordenada)
