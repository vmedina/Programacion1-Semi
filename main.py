def evaluar_listas(mi_lista_uno, mi_lista_dos):   
    #con split se puede corta cada palabra para generar un arreglo.
    for elemento in mi_lista_uno:
        if elemento in mi_lista_dos:
            return True
    return False

#se define un string cualquiera 
mi_lista_uno = [1,3,5,6]
mi_lista_dos = [12,4, 7, 10]

#la funcion manipular cadena recibe 


print(evaluar_listas(mi_lista_uno, mi_lista_dos))
