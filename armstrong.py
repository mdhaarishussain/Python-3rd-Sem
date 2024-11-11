import math
a=int(input("Enter number: "));
b=a;
p=a;
ar=0
c=0
while(p!=0):
    c=c+1
    p=(int)(p/10)
while(b!=0):
    d=b%10
    ar=ar+(int)(math.pow(d,c))
    b=(int)(b/10)
if ar==a:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")