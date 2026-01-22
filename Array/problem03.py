#Armstrong

n=153
num=n
power=len(str(n))
total=0
while num>0:
    last_digit=num%10
    total=total+(last_digit**power)
    num=num//10
if total==n:
    print("yes")

else:
    print("no")   