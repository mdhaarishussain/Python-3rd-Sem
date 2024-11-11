print("\n\nList1: ")
list1=[int(i) for i in input("Enter Numbers: ").split(" ")]
print("\n\nList2: ")
list2=[int(i) for i in input("Enter Numbers: ").split(" ")]
c=0;
n1=len(list1)
n2=len(list2)
list1.extend(list2)
list1=list(set(list1))
print("\n\nUnion: ",list1)

