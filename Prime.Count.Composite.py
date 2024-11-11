p=0
co=0
while (True):
    a=int(input("Enter number: "));
    if(a==-1):
        break;
    b=int(a/2);
    c=0;
    for i in range(2,(b),1):
        if a%i==0:
            c=c+1
            break
    if(a>1):
        if(c==0 ):
            p+=1
        else:
            co+=1

print("\n")
print("\n")
print("Prime Number Count: ",p)
print("Composite Number Count: ",co)