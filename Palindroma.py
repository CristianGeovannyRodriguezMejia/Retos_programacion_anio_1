palabra=input("Digite la palabra: ")
Li=0;
Ls=0;
Ls=len(palabra) -1
Palin=True;
while Li > Ls and Palin:
    if palabra[Ls] == palabra[Li] :
            Ls+=1;
            Li+=1;
    else :
            Palin=False;


print("La palabra es Palindroma") if Palin else print("La palabra no es palindroma");