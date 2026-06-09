def Anio(dia:int,Anio:int,Mes:int)-> int :
    Esvalido = False;
    if m==2 :
       if(a%4==0 and a%100!=0)or (a%4==0 and a%400==0) :
        if d>0 and d <=29 :
                Esvalido=True 
        else :
            if d>0 and d<=28:
                    Esvalido=True;
    else :
     if m==4 or m==6 or m==9 or m==11 :
        if d>0 and d<=30:
            Esvalido=True;
        else:
            if m>0 and m<=12:
                if d>0 and d<=31 :
                    Esvalido=True;
    return Esvalido;

d =int(input("Digite el dia: "));
m =int(input("Digite el mes: "));
a =int(input("Digite el anio: " ));
resul =Anio(d,m,a)
print("Es valida") if resul else print("es Invalida") 