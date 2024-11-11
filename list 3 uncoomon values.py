print("\n\nList1: ")
list1=[int(i) for i in input("Enter Numbers: ").split(" ")]
print("\n\nList2: ")
list2=[int(i) for i in input("Enter Numbers: ").split(" ")]
list3=[]
l=0
n1=len(list1)
n2=len(list2)
for i in range(0,n2):
    c=0
    for j in range(0,n1):
        if(list2[i]==list1[j]):
            c=1
    if c==0:
        list3.append(list2[i])
        l+=1
print("\n\nList3 Values: ")
for i in range(0,l):
    print(list3[i],end=" ")


