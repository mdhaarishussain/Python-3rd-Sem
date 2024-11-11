def part(arr,l,h):
    p=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<p:
            i+=1
            z=arr[i]
            arr[i]=arr[j]
            arr[j]=z
    z=arr[i+1]
    arr[i+1]=arr[h]
    arr[h]=z
    return i+1
def QuickS(arr,l,h):
    if l<h:
        q=part(arr,l,h)
        QuickS(arr,l,q-1)
        QuickS(arr,q+1,h)
def printA(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print()
    print()
if __name__ == "__main__":
    arr=[int(i) for i in input("Enter array: ").split()]
    print("Array [Before Sorting]:  ")
    printA(arr)
    QuickS(arr,0,len(arr)-1)
    print("Array [After Sorting]:  ")
    printA(arr)
