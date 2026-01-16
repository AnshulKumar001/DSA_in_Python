"""The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537"""

def tribonacci(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    t1,t2,t3=0,1,1
    for _ in range(3,n+1):
        t1,t2,t3=t2,t3,t1+t2+t3
    return t3
print(tribonacci(4))     

# def tribonacci(n):
#     #base case
#     if n==0:
#         return 0
#     if n==1 or n==2:
#         return 1
#     #recursive case
#     return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)   
# print(tribonacci(4))