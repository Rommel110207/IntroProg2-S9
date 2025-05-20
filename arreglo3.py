array_str= ["uno","dos","tres","cuatro",'cinco']
print("Array de cadenas: ", array_str)


array_str.insert(3,"cero")
print("Array de cadenas con el elemento cero agregado: ", array_str)


#Contar cuantos elementos hay en el array
cantidad= len(array_str)
print("Cantidad de elementos en el array: ", cantidad)


#Eliminar un elemento del array
array_str.remove("tres")
print("Array de cadenas con el elemento tres eliminado: ", array_str)


#Otra forma de eliminar un elemento del array
array_str.pop(2)
print("Array de cadenas con el elemento en la posicion 2 eliminado: ", array_str)