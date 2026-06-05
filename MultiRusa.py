#ejemplo1. resolviendo la multiplicacion rusa
num1=int(input("digite el numero: "))
num2=int(input("digite el numero: "))
suma = 0
while num1 > 0:
    if num1%2!=0:
     suma = suma + num2
    num1 = num1//2
    num2 = num2*2
    print(f"valor es: {num1}")
print(f"el producto es: {suma}")