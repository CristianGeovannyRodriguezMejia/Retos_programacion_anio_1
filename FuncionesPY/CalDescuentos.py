def CalcularDescuento(Monto : float)-> float :
    descuento = 0;
    if Monto>=0 and Monto<= 100 :
        descuento=Monto*0.02
        descuento = Monto - descuento
    elif Monto >= 100 and Monto<=200 :
        descuento = Monto*0.1
        descuento = Monto - descuento
    elif Monto >=200:
        descuento =Monto*0.15
        descuento = Monto - descuento
    return descuento


mt = float(input("digite su Total : "))
d = CalcularDescuento(mt);
print(f"su descuento es de {d}");