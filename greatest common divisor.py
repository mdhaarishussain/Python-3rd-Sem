p=int(input("Enter a : "));
t=int(input("Enter b : "));
hcf=0
if p>t:
    c=p
else:
    c=t
for i in range(1,c,1):
    if(p%i==0 and t%i==0):
        hcf=i

print(f"GCD of {p} and {t} is {hcf}")

    
    
