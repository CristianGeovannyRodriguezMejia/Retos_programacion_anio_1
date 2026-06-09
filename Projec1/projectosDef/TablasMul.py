def Mul(a:int)->int :
   
    it=range(0,11);
    for o in it :
     resul = print(f"{a}  X {o} = {a*o}");
    return resul;

b =int(input("Ingrese el numero para crear la tabla de multiplicar: "))
resu=Mul(b);
print(resu)