text=input("Enter a string: ")
wrd=input("Enter the word to count: ")
str=[i for i in text.split()]
occ=0
for i in str:
    if i==wrd:
        occ+=1
print("Occurence of ",wrd, ": ",occ)
