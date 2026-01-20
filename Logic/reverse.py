#reverse number 
num=12345
res=0
while num>0:
    last_digit=num%10
    res=(res*10)+last_digit
    num=num//10
print(res)    