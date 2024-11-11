a12=input("Enter string:  ");
wrd=input("Enter word to count:  ");
str=[i for i in a12.split()]
a=0
for x in str:
    if x==wrd:
        a+=1
print("No. of words: ",a)