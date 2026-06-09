num =int(input("Digite el numero a evaluar: "))
suma=0;
for it in range(1,num) :
    if num%it==0 :
        suma+=it
        print(it);

print(f"el numero es Perfecto")if num==suma else print("el numero no es perfecto");
