

import pdb

def agregarLibro(libro):
    if buscarLibro(libro)==False:
        # Agregar nuevos libPeter panros al archivo
        with open("prestamos.txt", "a") as archivo:
            archivo.write(libro+"\n")
            print("El libro se ingreso correctamente")
    else:
        print("El libro existe en el listado")
    
def buscarLibro(libro):   
    # Leer línea por línea con readline()
    with open("prestamos.txt", "r") as archivo:
        linea = archivo.readline().rstrip()
        if linea != "":
            while linea:           
                linea.strip()  # Eliminamos los saltos de línea
                
                print(linea)
                if linea == libro:
                    return True                    
                linea = archivo.readline()
    return False
libro = input("Ingrese el título del libro : ")
agregarLibro(libro)