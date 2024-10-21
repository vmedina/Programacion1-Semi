
# Desarrolla un programa que abra un archivo de texto, lea su contenido y lo muestre. 
# Implementa manejo de excepciones para archivos que no existan y usa finally para asegurarte de que el 
# archivo se cierre adecuadamente en cualquier caso.



def leer_archivo(nombre_archivo):
    try:
        # Intenta abrir el archivo en modo de lectura
        archivo = open(nombre_archivo, 'r')
        # Lee el contenido del archivo
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        # Asegura el cierre del archivo si fue abierto
        try:
            archivo.close()
            print("El archivo ha sido cerrado.")
        except NameError:
            # Si 'archivo' no se ha definido (porque falló la apertura), no hay nada que cerrar
            print("El archivo no se pudo abrir, por lo que no hay nada que cerrar.")

# Ejemplo de uso del programa
nombre_archivo = input("Ingresa el nombre del archivo que deseas leer: ")
leer_archivo(nombre_archivo)
