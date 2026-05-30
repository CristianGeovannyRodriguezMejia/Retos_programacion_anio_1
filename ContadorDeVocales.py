#crea un programa que pida al usuario una palabra 
# y luego cuente cuantas vocales aparecen y muestre el todal de las vocales

palabra = input("Introduce una palabra: ")
vocales = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
           }

contador = 0
for count in palabra:
    if count in vocales :
         contador+=1
         vocales[count]+=1

print(f"El número total de vocales en '{palabra}' es: {contador} la cantidad de letra en cada uno es {vocales}")
