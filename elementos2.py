#Dado una lista de 10 numeros, contar cuantos son mayores que 50 

numeros = [12, 45, 67, 23, 89, 34, 56, 78, 90, 11]
mayores_50 = sum(1 for numero in numeros if numero > 50)
print(f"Cantidad de números mayores que 50: {mayores_50}")