p=int(input("Enter Principle Amount : Rs."));
t=int(input("Enter time: "));
r=0;
if p<200000:
    r=10
elif (p>=200000 and p<=1000000):
    r=12
else:
    r=15
si=(p*r*t)/100
print("Simple Interest: Rs.",si);
