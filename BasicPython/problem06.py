'''Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.'''

class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        num=x
        rev=0
        while num>0:
            r=num%10
            num//=10
            rev=rev*10+r
        return rev==x
print(Solution().isPalindrome(121))  # output: True
print(Solution().isPalindrome(-121)) # output: False
print(Solution().isPalindrome(10))   # output: False