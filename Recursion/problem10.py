#LCM(Least Common Multiple) of two numbers using Recursion
def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)
def lcm(a,b):
    if a==0 or b==0:
        return 0
    return abs(a*b)//hcf(a,b)
print(lcm(12,15))   #output: 60
print(lcm(100,10))  #output: 100
print(lcm(7,5))     #output: 35