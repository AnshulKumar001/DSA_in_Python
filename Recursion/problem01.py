#diffrence b/t recursion an loop

#loop
n=5
i=1
while i<=n:
     print(i)
     i+=1


#Recursion 
def recursionunction(i,n):
#Base Case -> Stop function 
     if i>n:
          return
#Recursive case -> Function calling itself
     print(i)
     recursionunction(i+1,n)
recursionunction(1,5)

