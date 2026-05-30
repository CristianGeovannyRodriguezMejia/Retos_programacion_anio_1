#elaborar un programa que perimita capturar un numero y mostra la tabla de multiplicacion de ese numero.

a =int(input("Ingrese el numero para crear la tabla de multiplicar: "))
if a<=10: 
    it=range(0,10);
    for o in it :
        print(f"{a}  X {o} = {a*o}");

else: 
    print("numero no valido");




