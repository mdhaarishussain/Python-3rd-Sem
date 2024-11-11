list1=[int(i) for i in input("Enter Numbers: ").split(" ")]
n1=len(list1)
print("\n\nDistinct pairs with odd product: \n")
for x in range(0,(int)(n1/2)):
    for y in range((int)((n1/2)+1),n1):
        if((list1[x]*list1[y])%2!=0):
            print("(",list1[x],",",list1[y],")",end="  ")
