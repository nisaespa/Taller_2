# Crear función para ver sien una lista se encuentran cadenas con dos o más vocales
def contiene_dos_o_mas_vocales(cadena):
    contador_vocales = 0 # Iniciar contador de vocales
    for letra in cadena: # Iterar la cadena
        if letra.lower() in "aeiou": # Pasar los elementos (letras) de la cadena a minúscula, y sí los elementos son vocales
            contador_vocales += 1 # Sí son vocales, va contandolas
            if contador_vocales >= 2: # Sí son mas de dos
                return True # Sí tiene dos o mas vocales retorna verdadero
    return False # Sí no tiene dos o más vocales retorna falso
# Crear función para buscar las cadenas con vocales, usando la lista de cadenas que dio el usuario
def buscar_cadenas_con_vocales(lista):
    cadenas_con_vocales = [] # Inicializar una lista vacía para almacenar las cadenas con vocales.
    for cadena in lista: # Recorrer cada cadena en la lista.
        if contiene_dos_o_mas_vocales(cadena): # Llama a la función para verificar si la cadena tiene al menos dos vocales.
            cadenas_con_vocales.append(cadena) # Si la función devuelve True, agrega la cadena a la lista.
    # Comprueba si se encontraron cadenas con al menos dos vocales y devuelve el resultado.
    return cadenas_con_vocales if cadenas_con_vocales else 'No existen cadenas con dos o más vocales.'
# Iniciar programa
if __name__ == '__main__':
    # Bucle infinito para que se ingrese únicamente un número entero
    while True:
        try: # Para que se pida el valor
            cuantas_cadenas = int(input("Escriba cuántas cadenas quiere en la lista: "))
            if cuantas_cadenas > 0:
                break # Sí son números enteros positivos, terminar ciclo
            else:
                print("Ingrese un número entero positivo.")
        except ValueError: # Para solo esperar como tipo de dato, valores enteros
            print("Ingrese un número entero válido.")
    lista = [] # Para almacenar las cadenas
    for i in range(cuantas_cadenas): # Iterar en el rango de la cantidad de cadenas que dió el usuario
        palabra = input("Escriba una palabra: ")
        lista.append(palabra) # Para que se almacenen las palabras o cadenas
    resultado = buscar_cadenas_con_vocales(lista) # Imprimir resultado
    print(resultado)