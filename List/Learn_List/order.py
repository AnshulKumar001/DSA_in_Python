#1389

index=[0,1,2,2,1]
nums=[0,1,2,3,4]
ans=[]
for i,n in zip(nums,index):
    ans.insert(i,n)
print(ans)