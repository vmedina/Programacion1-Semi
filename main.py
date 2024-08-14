def main():
    # Este es el flujo principal del programa
    print("¡Bienvenido al programa de verificación y calculó de números primos!")
    
    # Solicitar al usuario que ingrese dos números
    numero1 = int(input("Ingresa un número para evaluar si es un número primo: "))    
    
    # llama a la función verificador_de_numero_primo 
    es_primo = verificador_de_numero_primo(numero1)
    if es_primo:
        resultado_print = "Es un número primo"
    else:
        resultado_print = "No es un número primo"
    # Mostrar el resultado
    print(f"El número {numero1} es: {resultado_print}")

    
    lista_numeros = input("Ingresa una lista de números (utilice la , como separador) para evaluar la cantidad de números primos: ")
    # llama a la función contador_de_numeros_primos     
    resultado_contador = contador_de_numeros_primos(lista_numeros)
   
    # Mostrar el resultado
    print(f"La cantidad de numeros primos es: {resultado_contador}")

    
def verificador_de_numero_primo(numero_a_evaluar):
    # los números primos son números naturales mayores que 1 y sin ningún divisor aparte de sí mismos y el número uno.
    if numero_a_evaluar <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    if numero_a_evaluar == 2:
        return True   # 2 es primo
    if numero_a_evaluar % 2 == 0:
        return False  # Si es divisible por 2, no es primo
    
    # Verificar si es divisible por algún número impar desde 3 hasta la raíz cuadrada de numero_a_evaluar
    for i in range(3, int(numero_a_evaluar**0.5) + 1, 2):
        if numero_a_evaluar % i == 0:
            return False
    
    return True

def contador_de_numeros_primos(lista_de_numeros):
    #separo los numeros ingresados por el usuario por la , y los ordeno usando sort()
    lista_de_numeros.split(",").sort()
    # Filtrar los elementos para dejar solo los números
    numeros = [int(elem) for elem in lista_de_numeros if elem.isdigit()]
    
    #inicializo un contador en 0
    contador = 0
    #itero la lista de numeros
    for numero in numeros:
        #llamo a la función encargada de verificar si un numero es primo
        if verificador_de_numero_primo(numero):
            #si retorna true se incrementa el contador en 1
            contador+=1
    #la función retorna la cantidad total de números primos en la lista
    return contador

# Verifica si este archivo es el programa principal
if __name__ == "__main__":
    main()