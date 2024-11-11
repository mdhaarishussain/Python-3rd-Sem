def MergeS(arr):
    if(len(arr)>1):
        m=len(arr)//2
        l=arr[:m]
        r=arr[m:]
        MergeS(l)
        MergeS(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1
def printA(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print()
    print()
if __name__ == "__main__":
    arr=[int(i) for i in input("Enter array: ").split()]
    print("Array [Before Sorting]:  ")
    printA(arr)
    MergeS(arr)
    print("Array [After Sorting]:  ")
    printA(arr)
    
