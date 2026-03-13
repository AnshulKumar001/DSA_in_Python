arr=[2,3,4,5,90]
print(arr)
#index
print(arr[1])


#2D Array
arr2D=[[2,3,4],[3,4,5]]
print(arr2D)
#index
print(arr2D[1][1])



#Linear traverse
arr=[2,3,4,5,90]
for i in arr:
    print(i,end=" ")

print("\n")

#Reverse
arr=[2,3,4,5,90]
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")

print("\n")

arr=[2,3,4,5,90]
i=0
while i<len(arr):
    print(arr[i],end=" ")   
    i += 1 

print("\n")

#insert
arrr=[3,4,34,643]
elem=50
arrr.insert(0,elem)
print(arrr)

#Delete
arr1=[3,4,34,643]
#del arr1[0]
arr1.pop(3)
print(arr1)