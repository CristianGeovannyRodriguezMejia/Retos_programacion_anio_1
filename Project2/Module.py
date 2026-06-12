#Muestra una cadena de manera invertida
def Inverso(cad : str)->bool:
    inv = ""
    for i in range(len(cad)-1, -1,-1):
        inv = inv + cad[i]
    return inv

def Rusa(num1:int, num2:int)->int:
    r = 0
    while num1 > 0:
        if num1%2!=0:
            r = r + num2
        num1 = num1//2
        num2 = num2*2
    return r

def Perfecto(num:int) -> bool:
    suma = 0
    for x in range(1,num):
        if num%x == 0:
            suma = suma + x
    return True if suma ==num else False

def Primo(num:int)->bool:
    cont = 2
    esPrimo = True
    while cont <= num/2 and esPrimo:
        if num%cont!=0:
            cont = cont+1
        else:
            esPrimo = False
    return esPrimo

def Tabla(num:int)->str:
    mensaje = ""
    for i in range(1,11):
        r = num * i
        mensaje = mensaje + str(num) + " x " + str(i) + " = " + str(r) + "\n"
    return mensaje

def FechaValida(d:int, m:int, a:int) ->bool:
    esValida = False
    if m==2:
        if (a%4==0 and a%100!=0) or (a%4==0 and a%400==0):
            if d>0 and d<=29:
                esValida = True
        else:
            if d>0 and d<=28:
                esValida =True
    else:
        if m==4 or m==6 or m==9 or m==11:
            if d>0 and d<=30:
                esValida=True
        else:
            if m>0 and m<=12:
                if d>0 and d<=31:
                    esValida=True
    return esValida

def Vocales(cadena:str)->int:
    vocales = 0
    for x in range (0,len(cadena)):
        if cadena[x] in "aeiouAEIOU":
            vocales = vocales + 1
    return vocales

def MayMin(cad : str)-> str:
    may = ""
    min = ""
    for i in cad:
        lt = ord(i)
        if lt>64 and lt<=90:
            may = may + i
            min = min + chr(lt+32)
        else:
            may = may + chr(lt-32)
            min = min + i
    return "Mayusculas : " + may + "\n" + "Minusculas : " + min


def CalcularDescuentos(s : float) -> str:
    """Funcion que permite aplicar los descuento 
    al sueldo de un empleado"""
    #Descuento Isss (3% limite hasta 1000)
    dIsss = 0
    if s > 0 and s <=1000:
        dIsss = s*0.03
    else:
        dIsss = 30
    #Descuento AFP (7.25% limite 7500)
    dAfp = 0
    if s > 0 and s<=7500:
        dAfp = s*0.0725
    else:
        dAfp = 543.75
    #Descuento Isr (Tablas)
    ri = s - (dIsss+dAfp)
    dIsr = 0
    if ri >0 and ri<=550:
        dIsr = 0
    else:
        if ri >550 and ri <=895.24:
            dIsr = (ri-550)*0.1 + 17.67
        else:
            if ri>895.24 and ri<=2038.1:
                dIsr= (ri-895.24)*0.2 + 60
            else:
                dIsr = (ri-2038.1)*0.3+ 288.57
    mensaje = "Los descuentos son:\n"
    mensaje = mensaje + f"Sueldo : {s}\n"
    mensaje = mensaje + f"Descuento Isss : {dIsss}\n"
    mensaje = mensaje + f"Descuento Afp : {dAfp}\n"
    mensaje = mensaje + f"Descuento Isr : {dIsr}\n"
    mensaje = mensaje + f"Total a pagar : {(s - (dIsss+dAfp+dIsr))}\n"
    return mensaje

def Factorial(num:int)->int:
    fact = num
    for i in range(num-1,0,-1):
        fact = fact*i
    return fact