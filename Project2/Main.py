from Module import Inverso
from Module import Rusa 
from Module import Perfecto 
from Module import Primo
from Module import Tabla 
from Module import FechaValida
from Module import Vocales
from Module import MayMin
from Module import CalcularDescuentos
from Module import Factorial
import os 
opc = 0;
opciones = """MENU DE OPCIONES
1. Capturar una palabra
2. Cadena Inversa
3. Multiplicacion Rusa
4. Determinacion Numero Perfecto 
5. Determinacion Numero Primo
6. Tablas de Multiplicacion
7. Validacion Fecha
8. Determinacion de Vocales
9. Convercion a Mayusculas
10. Calculo total a pagar
11. Calculo del factorial
12. salir
Digite la Opcion:  """

palabra = "";


while opc != 12 :
    opc = int(input(opciones));
    os.system("clear");
    if opc == 1 : 
        palabra = input("Digite la palabra: ");
        h = palabra;
        input("\Pulse enter para continuar")   
    elif opc== 2 :
            resultado = Inverso(palabra);
            print(f"Su palabra a la inversa es: {resultado} ");
            input("\Pulse enter para continuar")
    elif opc == 3 :
            n1 = int(input("Digite el primer numero : "))
            n2 = int(input("Digite el segundo numero : "))
            resultado = Rusa(n1,n2)
            print(f"Su Produto es :{resultado} ");
            input("\Pulse enter para continuar")
    elif opc == 4 :
            num = int(input("Digite el numero : "))
            resultado =Perfecto(num);
            print(f"resultado es : {resultado}");
            input("\Pulse enter para continuar")
    elif opc == 5 :
            pr = int(input("Digite el numero : "))
            resultado = Primo(pr)
            print("Es Primo") if resultado else ("No es Primo")
            input("\Pulse enter para continuar")

    elif opc == 6 :
           num = int(input("Digite el numero : "))
           resultado = Tabla(num)
           print(f"resultado es : {resultado}");
           input("\Pulse enter para continuar")       
    elif opc == 7 :
            d = int(input("Digite el dia : "))
            m = int(input("Digite el mes : "))
            a = int(input("Digite el anio : "))
            resultado =FechaValida(d,m,a)
            print("Es valida " if resultado else "No es Valida")
            input("\Pulse enter para continuar")
    elif opc == 8 :
           resultado =Vocales(palabra)
           print(f"Vocales : {resultado}");
           input("\Pulse enter para continuar")
    elif opc == 9 :
        resultado=MayMin(palabra)
        print(f"su palabra en mayusculas es: {resultado}")
        input("\Pulse enter para continuar")

    elif opc == 10 :
        sueldo = int(input("Digite un sueldo del empleado : "))
        resultado=CalcularDescuentos(sueldo);
        print(f"Su total seria {resultado}")
        input("\Pulse enter para continuar")
    elif opc == 11 :
        num = int(input("Digite el numero : "))
        resultado = Factorial(num)
        print(f"El Factorial es {resultado}")
        input("\Pulse enter para continuar")
        
