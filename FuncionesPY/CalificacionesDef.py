def CalCalificaciones(Cal1 : float, Cal2:float,Cal3 : float,Codigo : int) -> float :
    #mire use boolean por que me sale mucho mas facil tambien uso bastante el and y or
    Calificaciones =(Cal1 + Cal2 + Cal3)/3
    bandera= True
    if Codigo == 1 and Calificaciones >= 6.0 :
        bandera = True
    elif Codigo==2 and Calificaciones >= 6.5 :
        bandera= True
    elif Codigo == 3 and Calificaciones >= 7.0 :
        bandera=True
    elif Calificaciones  < 6  and Codigo==1 or Calificaciones < 6.5 and Codigo ==2 or Calificaciones < 7.0 and Codigo==3  and bandera:
        bandera = False;
    
    return bandera

codigo=int(input("Digite su Codigo de carreras: "));
cal1 =float(input("Digite su nota 1 : "))
cal2 =float(input("Digite su nota 2 : "))
cal3 =float(input("Digite la nota 3 : "))

#Comprobacion de si la nota esta en el rango
if  cal1 >= 0.1 and cal1 <= 10.0 or cal2 >= 0.1 and cal2 <= 10.0 or cal3 >= 0.1 and cal3 <= 10.0 :
    Respuesta = CalCalificaciones(cal1,cal2,cal3,codigo);
    print(f"Usted con codigo de aula {codigo} aprovo") if Respuesta else print(f"Usted con codigo de aula {codigo} no aprovo")
else : 
    print("su notas no estan en el rango");

