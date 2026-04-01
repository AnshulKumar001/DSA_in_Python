a=[1,2,3,4,5,6]
b=[7,8,2,9,4]
n=len(a)
m=len(b)
for i in range(n):
    for j in range(m):
        if a[i]==b[j]:
            print(i,j)
