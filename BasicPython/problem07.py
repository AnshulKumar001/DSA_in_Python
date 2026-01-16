#sum of digits of a number

nums=123456
sum=0
while nums>0:
    r=nums%10
    sum+=r
    nums//=10
print(sum)