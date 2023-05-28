import numpy as np


def generar_matriz():
    # dimensiones de la matriz del usuario
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    # array de números aleatorios del 0 al 100
    matriz = np.random.randint(0, 101, size=(filas, columnas))

    # Mostrar la matriz original
    print("Matriz original:")
    print(matriz)

    # Obtener las nuevas dimensiones para redimensionar la matriz
    nuevas_filas = int(input("Ingrese el número de filas para redimensionar la matriz: "))
    nuevas_columnas = int(input("Ingrese el número de columnas para redimensionar la matriz: "))

    # Validar las nuevas dimensiones
    if filas * columnas != nuevas_filas * nuevas_columnas:
        print("Error: Las nuevas dimensiones no son compatibles con la matriz original.")
        return

    # Redimensionar la matriz
    matriz_redimensionada = matriz.reshape(nuevas_filas, nuevas_columnas)

    # Mostrar la matriz redimensionada
    print("Matriz redimensionada:")
    print(matriz_redimensionada)


def encontrar_numero_mas_alto(arr):
    maximo = np.max(arr)
    return maximo

matriz_generada = generar_matriz()
maximo = encontrar_numero_mas_alto(matriz_generada)
print("El número más alto en la matriz es:", maximo)