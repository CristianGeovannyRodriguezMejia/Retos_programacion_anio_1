def par (a : int) -> bool :
    """Es funcion se usa para determinar si un numero es par"""
    r = False;
    if a%2==0 :
        r=True;
    return r


num = int(input("Digite un numero: "));
if  par(num):
    print("el numero es par");
else: 
    print("el numero es impar");