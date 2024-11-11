a=int(input("Enter number: "));
b=int(a/2);
c=0;
for i in range(2,(b),1):
    if a%i==0:
        c=c+1
        break
print("\n")
if c==0:
    print("Prime Number")
else:
    print("Not a Prime Number")