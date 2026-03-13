# Missing number
arr=[3,0,1]
n=len(arr)
total_sum=n*(n+1)//2
curr_sum=sum(arr)
missing_num=total_sum-curr_sum
print(missing_num)