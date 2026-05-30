#iterando un cadena 

pa =input("digite la palabra: ");
count="";
a=0;

for hola in range(len(pa) -1,-1,-1):
     count=count + pa[hola]
    

print(count);