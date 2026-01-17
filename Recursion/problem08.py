#Power of Four(342)

'''Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true'''

class Solution(object):
    def isPowerOfFour(self,n)->bool:
        if n<=0:
            return False
        if n==1:
            return True
        if n%4!=0:
            return False
        return self.isPowerOfFour(n//4)
obj=Solution()
print(obj.isPowerOfFour(16))   #output: True
print(obj.isPowerOfFour(5))    #output: False
print(obj.isPowerOfFour(1))    #output: True
