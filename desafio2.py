## Desafío 2: Mejora del Cálculo del Promedio 

#inicializamos variables que serán usadas posteriormente en el algoritmo
agregarMasEstudiantes = True
promedioDelEstudiante = 0

#Dado que son varios los estudiantes se utiliza un bucle while. 
#esta estructura se ejectuara mientras la condición evaluada sea verdadera. 
#se ha incializado como True para que se ejecute al menos una vez

while agregarMasEstudiantes:
    
    #solicito la calificación de cada estudiante
    #no estoy realizando la validación en el campo de calificación para evaluar que sea un número dado que es un tema que no corresponde a la unidad
    #no obstante sería correcto hacerlo ya que aporta robustes al codigo, mediante un try catch. 
    #utilizo la \" para que se muestre efectivamente la comilla en el comentario. 
    notasDeCalificacion= input("Ingrese la calificación del estudiante, separe las notas con una ""\",\""" :")
   
    #Divido la cadena en sus componentes usando la coma como separador
    coleccionDeCalificaciones = notasDeCalificacion.split(',')
    #inicializo las calificaciones en 0
    calificaciones = 0
    #recorro la colección de calificaciones de un estudiante 
    for calificacion in coleccionDeCalificaciones:
        calificacion = float(calificacion)
        #sumo todas las calificaciones de ese estudiante
        calificaciones+=calificacion
        
    #calculo el promedio utilizo la función len para obtener la cantidad de calificaciones 
    promedioDelEstudiante = calificaciones / len(coleccionDeCalificaciones)
    
    print(len(coleccionDeCalificaciones))
    #imprimo el promedio de calificaciones para el estudiante. 
    print(f"El promedio de las calificaciones del estudiante es: {promedioDelEstudiante}")
    
    #pregunto si desea ingresar otra calificación, utilizo lower para convertir el string ingresado a minusculas 
    #para poder evaluar solo "no" y no tener que contemplar también el No en mayusculas. 
    ingresarOtraCalificacion  = input("Desea ingersar las calificaciones de otro estudiante? Si / No ").lower()
    
    if ingresarOtraCalificacion == "no":
        #si no quiere agregar más estudiantes salgo del bucle
        agregarMasEstudiantes = False




  