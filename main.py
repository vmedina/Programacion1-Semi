import string
import random

def generar_contraseña(longitud=12):
    # string.ascii_letters Esto incluye todas las letras del alfabeto en minúsculas y mayúsculas. 
    # Equivale a 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    # string.digits incluye todos los dígitos decimales, que son '0123456789'
    # string.punctuation 
    # incluye todos los caracteres de puntuación, tales como '!"#$%&\'()*+,-./:;<=>?@[\]^_{|}~'`.
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # utilizo random.choice para seleccionar un caracter al azar con for itera la cantidad esta indicada por la variable longitud,
    # join concatena los caracteres 
    return ''.join(random.choice(caracteres) for _ in range(longitud))

print("Su nueva contraseña es:" + generar_contraseña())

def analizar_texto(texto):
    #1 for c in texto if esto itera sobre cada letra de la variable texto, c recibe el valor de cada letra, numero o signo
    # sum es una funcion que suma los elementos de un iterable
    
    conteo_letras = sum(1 for c in texto if c in string.ascii_letters)
    conteo_numeros = sum(1 for c in texto if c in string.digits)
    conteo_puntuacion = sum(1 for c in texto if c in string.punctuation)
    return conteo_letras, conteo_numeros, conteo_puntuacion

texto = "Hola, 12345678, %$? !"
print(analizar_texto(texto))

def generar_nombre_usuario(longitud=8):
    palabras = ['Luna', 'Fuego', 'Mar', 'Cielo', 'Nube']
    #random.choice rebie en este caso un arreglo de palabras y selecciona una al azar. 
    palabra = random.choice(palabras)
    # string.ascii_letters Esto incluye todas las letras del alfabeto en minúsculas y mayúsculas. 
    # Equivale a 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    # k=4 equivale al número de elementos a seleccionar de la secuencia
    sufijo = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    return palabra + sufijo

print("Su nombre de usuario es: " + generar_nombre_usuario())