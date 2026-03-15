arr=[12,4,45,64,56,15,90]
key=45
n=len(arr)
def Search(n,key, arr):
    for i in range(n):
        if arr[i]==key:
            return i
    return -1

result = Search(n, key, arr)
print(result)