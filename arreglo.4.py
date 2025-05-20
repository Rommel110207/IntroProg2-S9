import os
import random
import time




concursantes= list()
while True:
    os.system("cls")
    os.system("color a2")
    nombre= input("Ingrese el nombre del concursante (o 'fin' para terminar): ")
    if nombre.lower()== "fin":
        break
    concursantes.append(nombre.upper())
os.system("cls")    
print("Concursantes registrados: ")
print(concursantes)
x= input("Presione una tecla para continuar...")

cont= 10
while cont> 0:
    os.system("cls")
    print("El sorteo comienza en: ", cont)
    time.sleep(1)
    cont-= 1
fin= len(concursantes)-1
ganador= random.randint(0,fin)
print(f"El mejor admin es: {concursantes[ganador]}")

