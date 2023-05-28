import numpy as np


def generar_matriz():
    # pediremos las dimensiones de la matriz del usuario
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    # array de números aleatorios del 0 al 100
    matriz = np.random.randint(0, 101, size=(filas, columnas))

    print("Matriz original:")
    print(matriz)
    # pediremos al usuario las nuevas dimensiones para redimensionar la matriz
    nuevas_filas = int(input("Ingrese el número de filas para redimensionar la matriz: "))
    nuevas_columnas = int(input("Ingrese el número de columnas para redimensionar la matriz: "))

    # si las dimensiones no son compatibles, esto quiere decir que el total de elementos en el array no es igual al numero total de elementos de ya establecido
    if filas * columnas != nuevas_filas * nuevas_columnas:
        print("Error: Las nuevas dimensiones no son compatibles con la matriz original.")
        return

    # redimencionamos la matriz
    matriz_redimensionada = matriz.reshape(nuevas_filas, nuevas_columnas)

    print("Matriz redimensionada:")
    return matriz_redimensionada


def encontrar_numero_mas_alto(arr):
    maximo = np.max(arr)
    return 'número más alto: ', maximo


def encontrar_numero_mas_bajo(arr):
    minimo = np.min(arr)
    return 'número más bajo: ', minimo
