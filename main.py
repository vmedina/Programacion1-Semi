### Desafío 4: Algoritmo MCD
##El MCD de dos números es el número más grande que divide a ambos sin dejar un residuo

def calcular_maximo_comun_divisor(numero_uno, numero_dos):
    
    while numero_dos != 0:
        #se realiza la división del primer y segundo número
        residuo = numero_uno % numero_dos
        #se asigna el valor del segundo numero a la variable correspondiente al primer número
        numero_uno = numero_dos
        #se asinga el residuo o resto al valor de la segunda varible. 
        numero_dos = residuo
       
    #finalizada la iteración se retorna el valor del primer número que corresponde al MCD
    return numero_uno

# Ejemplo de uso
numero1 = 48
numero2 = 18
resultado = calcular_maximo_comun_divisor(numero1, numero2)

print(f"El MCD de {numero1} y {numero2} es: {resultado}")
