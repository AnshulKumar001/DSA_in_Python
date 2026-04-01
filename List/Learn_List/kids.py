 #1431
candies=[2,3,5,1,3]
extra_candies=3
max_candies=max(candies)
n=len(candies)
for i in range(n):
    d=candies[i]+extra_candies
    if d>=max_candies:
        print("true")
    else:
        print("False")  
 