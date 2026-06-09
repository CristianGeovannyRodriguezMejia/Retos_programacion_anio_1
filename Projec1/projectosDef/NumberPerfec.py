def NumberPerfec(num:int)-> int :
    suma=0;
    for it in range(1,num) :
        if num%it==0 :
            suma+=it
    return suma;    

num1 =int(input("Digite el numero a evaluar: "))
resul=NumberPerfec(num1)
print("El numero es Perfecto")if num1==resul else print("el numero no es perfecto");
