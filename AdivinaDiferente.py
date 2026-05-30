import random;
number = random.randint(1,10);

intentos=0;
User=0;
while User!=number:
 User=int(input("adivina el numero del 1 al 10: "));
intentos+=1;
if intentos <=number:
    print("tus intentos son mayores que el numero a adivinar jajaja")

else:
    print("inpresionante fueron muy pocos intentos la verdad");
   


print(f"aciertaste el numero correcto era {User}");
