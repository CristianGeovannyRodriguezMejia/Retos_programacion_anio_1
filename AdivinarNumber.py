import random;

number =random.randint(1,5);

for i in range(5) :

    user=int(input("Intenta adivinar el numero ramdom tiene 5 intentos: "));
    if user != number :
        print("Estubiste cerca")
    else:
        print("En efecto eres la mera mera");
        break



print(f"si el numero correcto era {number} ");

