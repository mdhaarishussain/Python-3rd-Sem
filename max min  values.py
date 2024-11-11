list=[int(i) for i in input("Enter Numbers: ").split(" ")]
min=list[0]
max=list[0]
for i in range(0,len(list)):
    if max<list[i]:
        max=list[i]    
    if min>list[i]:
        min=list[i]
print("\n\nMax Value: ",max,"\nMin Value:   ",min)
