a12=input("Enter string:  ");
a,e,i,o,u=0,0,0,0,0
for x in a12:
    if x=='a':
        a+=1
    elif x=='e':
        e+=1
    elif x=='i':
        i+=1
    elif x=='o':
        o+=1
    elif x=='u':
        u+=1
print("Count: \na: ",a,"\ne: ",e,"\ni: ",i,"\no: ",o,"\nu: ",u)