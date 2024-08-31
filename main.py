import random
# La función randint(a, b) genera un número entero aleatorio n tal que a <= n <= b. 
# En este caso, el número estará en el rango de 0 a 100, ambos inclusive.
# El límite inferior es 0 
# El límite superior es 100

def generarNumeroRandom(num1, num2):
    # Verifica que el primer número no sea mayor al segundo.
    if num1 > num2:
        raise ValueError("El primer número debe ser menor o igual al segundo número.")
    else:
        #genera y retorna un número aleatorio
        return random.randint(num1, num2)
    
# Imprime un número aleatorio entre 1 y 100.
print(generarNumeroRandom(1,100))