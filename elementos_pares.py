#Suma los elementos que se encuentran en posiciones pares de la lista.

elementos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
suma_pares = sum(elementos[i] for i in range(len(elementos)) if i % 2 == 0)
print(f"La suma de los elementos en posiciones pares es: {suma_pares}")