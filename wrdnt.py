a=input("Enter string:  ");
e,l=0,0
for x in a:
    if x!='':
        l=1
    if x==' ':
        e+=1
if(l==1):
    print("Word Count: ",e+1)
else:
    print("Word Count: ",e)