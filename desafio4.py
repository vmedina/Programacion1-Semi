from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

#inicializamos variables que seran usadas posteriormente en el algoritmo
agregarMasNotas = True
total = 0
notas = []


#Dado que son varios los notas que hay que agregar voy a usar un bucle while. 
#esta estructura se ejectuara mientras la condicion evaluada sea verdadera. 
#se ha incializado como True para que se ejecute al menos una vez

while agregarMasNotas:
    #solicito las notas 
    notaIngresada =int(input("Ingrese la nota:"))
    
    #pregunto si desea agregar otro Nota
    otroNota  = input("Desea ingersar otro Nota? Si / No ")
    #se agrega la nota al array 
    notas.append(notaIngresada)
    
    if otroNota =="No" or otroNota == "no":
        #si no quiere agregar mas Notas salgo del bucle
        agregarMasNotas = False
        

sumaDeNotas = 0 
#len lo utilizo para obtener la cantidad de notas
cantidadDeNotas = len(notas)
#sum suma todas las notas del arreglo
#calculo del pormedio 
sumaDeNotas= sum(notas)
promedioDeNotas = sumaDeNotas/cantidadDeNotas


#utilizo min y max para obtener las notas más bajas y más altas
notaMasBaja = min(notas)
notaMasAlta = max(notas)

#utilizo counter para obtener la nota que más se reptie
#most_common(1) devuelve una lista con el elemento más común y su frecuencia.
#[0] se usa para obtener el primer elemento de esa lista, que es una tupla (nota, frecuencia).
contadorNotas = Counter(notas)
notaMasRepetida, frecuencia = contadorNotas.most_common(1)[0]

#imprimo la nota que mas se repite y la frecuencia
print(f"La nota que se repite más es {notaMasRepetida} con una frecuencia de {frecuencia}.")
print('El promedio de notas es:', {promedioDeNotas})
print('La nota que mas baja es:', {notaMasBaja} )
print('La nota que mas alta es:', {notaMasAlta} )


# Grafica de barras 
# Índices para las notas
indices = np.arange(len(notas))

# Crear el gráfico de barras
plt.bar(indices, notas, color='blue', alpha=0.7)

# Añadir una línea horizontal para el promedio
plt.axhline(y=promedioDeNotas, color='red', linestyle='--', label=f'Promedio: {promedioDeNotas:.2f}')

# Añadir etiquetas y título
plt.xlabel('Índice de la Nota')
plt.ylabel('Valor de la Nota')
plt.title('Notas y Promedio')
plt.legend()
# Mostrar el gráfico
plt.show()