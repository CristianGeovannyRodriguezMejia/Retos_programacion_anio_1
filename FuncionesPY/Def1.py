def Palindroma(palabra : bool) -> bool :
    Li=0;
    Ls=len(palabra) -1
    Palin=True;
    while Li < Ls and Palin:
        if palabra[Li] == palabra[Ls] :
             Ls-=1;
             Li+=1;
        else :
            Palin=False;
    return Palin

pala=input("Digite la palabra: ")
print(Palindroma(pala)) if Palindroma(pala) else print(Palindroma(pala));


# def palindroma(palabra: str)-> str :
#     Li=0;
#     Ls=len(palabra) -1
#     Palin=True;
#     while Li > Ls and Palin:
#         if palabra[Ls] == palabra[Li] :
#                 Ls+=1;
#                 Li+=1;
#         else :
#             Palin=False;
#     return print("La palabra es Palindroma") if Palin else print("La palabra no es palindroma");

# cad =input("digite la palabra: ");
# print(palindroma(cad.upper()));