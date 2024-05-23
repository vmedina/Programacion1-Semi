## Desafío 1: Calificaciones Aprobatorias y Desaprobatorias 

#inicializamos variables que serán usadas posteriormente en el algoritmo
agregarMasCalificaciones = True
totalAprobados = 0
totalDesaprobados = 0 

#Dado que son varios los estudiantes se utiliza un bucle while. 
#esta estructura se ejectuara mientras la condicion evaluada sea verdadera. 
#se ha incializado como True para que se ejecute al menos una vez

while agregarMasCalificaciones:
    
    #solicito la calificación de cada estudiante
    #no estoy realizando la validacion en el campo de calificacion para evaluar que sea un numero porque este tema no corresponde a la unidad
    #sería correcto hacerlo que el código sera más robusto mediante un try catch. 
    notaDeCalificacion= int(input("Ingrese la calificación del estudiante:"))
   
    
    #pregunto si desea ingresar otra calificación, utilizo lower para convertir el string ingresadoa minusculas 
    #para poder evaluar solo no y no tener que contemplar también el No en mayusculas. 
    ingresarOtraCalificacion  = input("Desea ingersar otra calificación? Si / No ").lower()
    
    #calculo la cantidad total de aprobados y desaprobados 
    #utilizo una estructura condicional para diferenciarlos según la condición dada
    #incremento en 1 el contador de cada grupo según sea el caso
    
    if(notaDeCalificacion >= 7):
        totalAprobados += 1
    else:
        totalDesaprobados += 1
    
    
    if ingresarOtraCalificacion == "no":
        #si no quiere agregar mas productos salgo del bucle
        agregarMasCalificaciones = False
        

#imprimo el toal de estudiantes que aprobaron y los que desaprobaron. 
print(f"Total de estudiantes desaprobados: {totalDesaprobados}")
print(f"Total de estudiantes aprobados: {totalAprobados}")



  