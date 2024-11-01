#Tienes una tabla de calificaciones representada como una matriz, 
#donde cada fila contiene las calificaciones de un estudiante en distintas materias. 
#Implementa una función que busque una calificación específica en toda la matriz y devuelva el estudiante y la materia en la que se encuentra.

def buscar_calificacion(matriz, calificacion_buscada):
    for i, fila in enumerate(matriz):
        for j, calificacion in enumerate(fila):
            if calificacion == calificacion_buscada:
                return f"Calificación {calificacion_buscada} encontrada en el estudiante {i+1} (fila) y materia {j+1} (columna)"
    return "Calificación no encontrada en la matriz"


# matriz de calificaciones cada fila representa a un estudiante
# cada columna representa una materia
matriz_calificaciones = [
    [85, 90, 78],
    [92, 88, 76],
    [79, 85, 82]
]

# Buscamos una calificación específica
resultado = buscar_calificacion(matriz_calificaciones, 88)
print(resultado)
