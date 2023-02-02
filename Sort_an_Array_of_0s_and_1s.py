def insertionsort(n,arr):
    for i in range(1,n):
        temp=arr[i]
        for j in range(i-1,-1,-1):
            if temp<arr[j]:
                arr[j+1]=arr[j]
            else:
                arr[j+1]=temp
                break
        else:
            arr[0]=temp
n=int(input())
arr=list(map(int,input().split()))
insertionsort(n,arr)
print(*arr)
        