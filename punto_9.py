# Crear función para pedir los números.
def pedir_numeros():
    while True: # Bucle para que solo se acepten valores numéricos.
        try: # Para que se pida el valor
            a = float(input("Ingrese un número real: "))
            b = float(input("Ingrese un número real: "))
            c = float(input("Ingrese un número real: "))
            d = float(input("Ingrese un número real: "))
            e = float(input("Ingrese un número real: "))
            break # Sí es un número, terminar ciclo
        except ValueError: # Para solo esperar como tipo de dato, valores numéricos
            print("No es un número válido, intenta de nuevo.") # Si se ingresa un valor que no sea un número, se muestra el texto de error, para que se ingrese de nuevo un número valido
    numeros = [a, b, c, d, e] # Poner los números en una lista
    return numeros 
# Crear función para hacer las operaciones con el vector.
def operaciones_vector(numeros):
    suma = sum(numeros) # Para que se sumen los números del vector.
    promedio = suma / len(numeros) # De la suma del vector, dividir por el número de elementos que tenga el vector, en este caso 5.
    numeros.sort() # Para ordenar el vector
    mediana = numeros[len(numeros) // 2] # Para encontrar el valor del medio, división entera a 5 = 2, es decir el indice 2.
    promedio_multiplicativo = (numeros[0] * numeros[1] * numeros[2] * numeros[3] * numeros[4]) ** 0.5 # Formula para el promedio multiplicativo con los indices
    lista_ordenada = sorted(numeros, reverse=True) # Para ordenar en orden descendente los números
    mayor = max(numeros) # Para el número mayor
    menor = min(numeros) # Para el número menor
    pot = mayor ** menor # Elevar el mayor número al menor número.
    raíz_cúbica = menor ** (1/3)  # calcular la raíz cúbica del menor
    print(f"El promedio de los números es: {promedio}")
    print(f"La mediana de los números es: {mediana}")
    print(f"El promedio multiplicativo es: {promedio_multiplicativo}")
    print(f"La lista de números ordenados de menor a mayor es: {numeros}")
    print(f"La lista de números ordenados de mayor a menor es {lista_ordenada}")
    print(f"La potencia del mayor número elevado al menor es: {pot}")
    print(f"La raíz cúbica del menor número es: {raíz_cúbica}")
# Iniciar programa.
if __name__ == '__main__':
    numeros = pedir_numeros() # Convertir en variable la función de pedir números.
    operaciones_vector(numeros) # Llamar la función
