a=input("Enter string:  ");
print("Substrings: ")
for x in range(len(a)):
    for w in range(x,len(a)):
        print(a[x:w+1],end='\n')
   