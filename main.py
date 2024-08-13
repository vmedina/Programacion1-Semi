
def suma_y_promedio(lista_de_numeros):
    if not lista_de_numeros:  # Verifica si la lista está vacía
        return 0, 0
    else:
        sumaTotal = 0 
        promedio = 0
        for valor in lista_de_numeros:
            # Sumar cada valor en la lista para calcular la suma total
            sumaTotal += valor    
    
        # Calcular el promedio dividiendo la suma entre la cantidad de elementos
        promedio = sumaTotal/len(lista_de_numeros)
        
        return sumaTotal, promedio

#se define un arreglo cualquiera de números
arreglo = [3, 6, 4, 7, 8]

suma, promedio = suma_y_promedio(arreglo)

print("la suma toal es: ", suma)
print("el promedio es:", promedio)
    