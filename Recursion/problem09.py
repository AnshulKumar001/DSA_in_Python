#HCF(Highest Common Factor)(GCD) of two numbers using Recursion
def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)
print(hcf(12,15))   #output: 3
print(hcf(100,10))  #output: 10
print(hcf(7,5))     #output: 1