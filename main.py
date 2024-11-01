#Tienes una lista de estudiantes y su promedio de calificaciones. 
#Implementa un algoritmo que ordene a los estudiantes de acuerdo con su promedio utilizando el algoritmo de ordenamiento por selección. 
#Al final, el estudiante con el promedio más alto debe estar en primer lugar.

# Lista de códigos de promedios de estudiantes
notas = [ 10, 9, 8, 4, 12]

# Ordenamiento por selección
def ordenamiento_seleccion(notas):
    for i in range(len(notas)):
        min_idx = i
        for j in range(i + 1, len(notas)):
            if notas[j] > notas[min_idx]:
                min_idx = j
        # Intercambiar el elemento más pequeño con el primer elemento no ordenado
        notas[i], notas[min_idx] = notas[min_idx], notas[i]

# Ordenar la lista de promedios de estudiantes
ordenamiento_seleccion(notas)
print(f"notas ordenado: {notas}")
