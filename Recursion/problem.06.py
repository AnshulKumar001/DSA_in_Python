#Power of Two(231)
'''Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false'''

class Solution(object):
   def isPowerOfTwo(self,n) ->bool:
      while n%2==0:
         n//=2
      return n==1  
obj=Solution()
print(obj.isPowerOfTwo(1))    #output: True 
print(obj.isPowerOfTwo(16))   #output: True
print(obj.isPowerOfTwo(3))    #output: False 



 
#class Solution2(object):
#   def isPowerOfTwo(self,n) ->bool:
#Base case
#      if n<=0:
#         return False
#      if n==1:
#         return True
#      if n%2!=0:
#         return False
#Recursive case
#      return self.isPowerOfTwo(n//2) 