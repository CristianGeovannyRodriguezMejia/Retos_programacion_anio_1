import os as e;

opc = 0;
opciones = """MENU DE OPCIONES
1. Capturar una palabra 
2. Mostrar Cantidad de vocales 
3. Comprobar si es palindroma
4. Mostrar en orden inverso 
5. Mostrar en mayuscula/miniscula
6. Salir
Digite la Opcion: """

palabra = "";

while opc != 6 :
   
    opc =int(input(opciones));
    e.system("clear")
    if opc == 1 :
        palabra = input("Ingrese la palabra: ");
        h =palabra;
        if len(palabra) == 0 :
            print("usted no ingreso un Palabra valida");
    elif opc == 2 :
            if len(palabra) == 0 :
                print("usted no ingreso un Palabra valida");

            i="aeiou"
            contador=0;
            for palabra in h :
             if palabra in i :
                contador=contador+1;

            print(f"la cantidad de vocales es :{contador} ");
            input("\Pulse enter para continuar")
    elif opc == 3 :
            if len(palabra) == 0 :
                print("usted no ingreso un Palabra valida");
            Li=0;
            Ls=0;
            Ls=len(palabra) -1
            Palin=True;
            while Li < Ls and Palin:
                if palabra[Li] == palabra[Ls] :
                    Ls+=1
                    Ls+=1
                else :
                    Palin=False;
                print("La palabra es Palindroma") if Palin else print("La palabra no es palindroma");
                input("\Pulse enter para continuar")


    elif opc== 4 :
        if len(palabra) == 0 :
            print("usted no ingreso un Palabra valida");
    
        count="";
        for hola in range(len(palabra) -1,-1,-1):
            count=count + palabra[hola]
        print(count);
        input("\Pulse enter para continuar")


    elif opc == 5 : 
        if len(palabra) == 0 :
            print("usted no ingreso un Palabra valida");
        my="";
        h=0;
        for a in palabra:
            c = ord(a)
            if c>64 and c<=90  :
                h =c+90;
                my+=chr(h);
            else :
                 h =c-32;
            my+=chr(h);
        print(f"su palabra en mayuscula {my} y su Palabra en minuscula fue {palabra}");
        input("\Pulse enter para continuar")

        