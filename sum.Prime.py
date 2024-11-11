a=int(input("Enter start of Range: "));
b=int(input("Enter end of Range: "));
l=0;
print("\n")
print("Sum of all Prime Numbers: ")
for j in range(a,b+1,1):
    i=1
    for i in range(2,j,1):
        if j%i==0:
            j=i
            break;
    if j!=i:
        l=l+j
print("=",l)
