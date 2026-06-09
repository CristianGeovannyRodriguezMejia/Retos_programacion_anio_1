def Rusa(num1:int,num2:int)->int :
    suma = 0
    while num1 > 0:
        if num1%2!=0:
            suma = suma + num2
        num1 = num1// 2
        num2 = num2*2
    return suma;

Num1=int(input("digite el numero: "));
Num2=int(input("digite el numero: "));
resul=Rusa(Num1,Num2);
print(f'el resultado es {resul}');
