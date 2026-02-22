list=[1,2,3,4,5, 100]
print(f"La longitud de la lista es: {len(list)}")

suma=0
for i in list:
    suma+=i

print(f"La suma de los elementos de la lista es: {suma}")


multipliacion=1
for i in list:
    multipliacion*=i
print(f"El valor de la multiplicación de los elementos de lista es: {multipliacion}")


list.append(4)
print(f"La longitud de la lista es: {len(list)}")