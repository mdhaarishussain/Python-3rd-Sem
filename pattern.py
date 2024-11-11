
c=1
for i in range(1,5):
    for j in range(i+1):
        if(i==j):
            print(j)
        else:
            print(c,end=",")
        c+=1
        
