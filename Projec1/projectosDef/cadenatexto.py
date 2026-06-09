def Cadena(pa:str)->str :
    count="";
    a=0;
    for hola in range(len(pa) -1,-1,-1):
     count=count + pa[hola]
    return count

palabra =input("digite la palabra: ");
print(Cadena(palabra));