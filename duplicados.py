#Dada una lista con valores repetidos, crea una nueva lista sin duplicados.

valores = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8, 9, 10, 10]
def eliminar_duplicados(lista):
    return list(set(lista))
def main():
    lista_sin_duplicados = eliminar_duplicados(valores)
    print("Lista original:", valores)
    print("Lista sin duplicados:", lista_sin_duplicados)
if __name__ == "__main__":
    main()