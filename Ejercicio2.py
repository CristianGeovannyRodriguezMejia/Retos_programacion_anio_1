#Elaborar un programa que permita capturar un palabra y que la convierta en mayuscula 
#haciendo uso de de la codificacion ascii

pa = input("ingrese una palabra: ");
my="";
for a in pa:
   c = ord(a)
   if c>64 and c<=90  :
     h =c+90;
     my+=chr(h);
   else :
      h =c-32;
      my+=chr(h);
       
print(f"su palabra en mayuscula {my}");

