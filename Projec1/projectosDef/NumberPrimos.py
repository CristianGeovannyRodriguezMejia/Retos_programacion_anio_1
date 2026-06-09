def PrimoNumber(num1:int)->int: 
    count=2;
    numberprimo = True;
    while  numberprimo and count<=num1/2  :
        if num1%count==0 : 
            numberprimo=False
        count=count+1;
    return numberprimo;
num=int(input("ingrese su numero: "));
resul=PrimoNumber(num);
print("su numero si es primo")if resul else print("el numero N0 es primo");