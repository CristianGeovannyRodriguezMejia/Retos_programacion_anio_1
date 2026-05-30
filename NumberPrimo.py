#elabora un programa que perimiya capturar un numero y determine si es primo

num = int(input("Digite su Numero; "));
#Pues un contador 
count=2;
#Una variable bandera
numberprimo = True;

while  numberprimo and count<=num/2  :
    if num%count==0 : 
     numberprimo=False
    count=count+1;


if numberprimo :
       print("Es primo")
else:
       print("No es Primo")