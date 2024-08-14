def evaluar_listas(mi_lista_uno, mi_lista_dos):   
    # itero a través de una lista y verifico si cada elemento está presente en la otra lista.
    for elemento in mi_lista_uno:
        if elemento in mi_lista_dos:
            return True
    return False

#se defined dos listas 
mi_lista_uno = [1,3,5,6]
mi_lista_dos = [12,4, 7, 10]

#la funcion evaluar_listas recibe dos listas y si comparten elementos retorna true
print(evaluar_listas(mi_lista_uno, mi_lista_dos))
