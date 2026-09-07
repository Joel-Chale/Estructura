def mostrar_vector(datos):
    for i in range(len(datos)):
        print(datos[i])

def media(datos):
    n = len(datos)
    suma = 0
    for i in range(n):
        suma = suma + datos[i]
    return suma / n


if __name__ == "__main__":
    pares = [2, 4, 6, 8, 10]
    impares = [1, 3, 5, 7, 9]

    mostrar_vector(pares)
    print("Media= " + str(media(pares)))
    
    mostrar_vector(impares)
    print("Media= " + str(media(impares)))

    
