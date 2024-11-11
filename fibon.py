n1=0;n2=1;
n3=1
c=0
while n3<=100:
    if(n3%2==0):
        c=c+n3
    n3=n1+n2
    n1=n2
    n2=n3
    
print("Sum: ",c)
