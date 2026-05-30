num=int(input("digite el numero: "));
Fact=num;

for i in range(Fact-1,0,-1):
    Fact=Fact*i;
    print(f"{num} * {i} = {Fact}")


print(f"El factorial es :{Fact }")