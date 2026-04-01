#problem no 1470

arr=[1,2,3,4,5,6]
n=3
#x=[1,2,3]
#y=[4,5,6]
#output=[1,4,2,5,3,6]
x=[]
for i in range(n):
    x.append(arr[i])
    x.append(arr[i+n])
print(x)    
