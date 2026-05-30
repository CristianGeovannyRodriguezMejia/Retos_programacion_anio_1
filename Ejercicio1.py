#elaborar un programa que capture un cadena de texto y que diga cuantas vocales tiene 
ex= input("ingrese alguna palabra: ");
i="aeiou"
contador=0;
for palabra in ex :
    if palabra in i :
         contador=contador+1;
else: 
    print("que?");

print(f"la cantidad de vocales es :{contador} ");
