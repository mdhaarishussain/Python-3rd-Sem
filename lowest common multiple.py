a=int(input("Enter number1: "));
b=int(input("Enter number2: "));
c=0;
lcm=0
if a>b:
    c=a
else:
     c=b
while (True):
    if(c%a==0 and c%b==0):
        lcm=c
        break
    c=c+1
print("LCM: ",lcm)